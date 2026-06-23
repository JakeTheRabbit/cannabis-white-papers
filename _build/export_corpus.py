# -*- coding: utf-8 -*-
"""Export the white papers as a clean, machine-readable corpus.

Reuses the existing build modules (paper_* modules, REFS, NAV, GLOSSARY) as the
single source of truth and emits, into the repo root:
  papers/<slug>.md   one clean markdown file per paper (YAML frontmatter + body,
                     citations preserved as footnotes)
  manifest.json      index of all papers
  glossary.json      the glossary
  llms.txt           curated index (llmstxt.org spec)
  llms-full.txt      all papers concatenated
  LICENSE            CC BY-NC 4.0 + attribution

Run:  cd _build && python export_corpus.py   (or it runs at the end of build.py)
"""
import os, re, json, html, sys
sys.path.insert(0, os.path.dirname(__file__))
import build  # reuses build.PAPERS, build.REFS, build.NAV, build.GL (no render on import)

ROOT = build.ROOT
BASE = "https://jaketherabbit.github.io/cannabis-white-papers"
VERSION = "1.0"
UPDATED = "2026-06-24"
ATTRIBUTION = "The Cannabis White Papers"
LICENSE_ID = "CC BY-NC 4.0"
LICENSE_URL = "https://creativecommons.org/licenses/by-nc/4.0/"

REFS = build.REFS.REFS
GLOSSARY = build.GL.GLOSSARY

# slug -> group name, slug -> short blurb (from nav)
SLUG_GROUP, SLUG_SHORT = {}, {}
for g in build.NAV.GROUPS:
    for it in g["items"]:
        SLUG_GROUP[it["slug"]] = g["group"]
        SLUG_SHORT[it["slug"]] = it.get("short", "")

LEAK = re.compile(r"disdale|legacy ag|legacy\.ag|\bnubu\b|chill division|"
                  r"\b192\.168\.|\b10\.0\.0\.|ghp_[A-Za-z0-9]{6}|github_pat_", re.I)


# ---------------------------------------------------------------- inline HTML -> md
def inline_md(s, used):
    # citations first (they wrap an <a>)
    def _cite(m):
        used.add(m.group(1))
        return f"[^{m.group(1)}]"
    s = re.sub(r"<sup class='cite'><a href='#ref-([^']+)'>\[\d+\]</a></sup>", _cite, s)
    # links
    s = re.sub(r"<a [^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>", r"[\2](\1)", s)
    s = re.sub(r"<a [^>]*href='([^']+)'[^>]*>(.*?)</a>", r"[\2](\1)", s)
    # emphasis / code
    s = re.sub(r"</?(strong|b)>", "**", s)
    s = re.sub(r"</?(em|i)>", "_", s)
    s = re.sub(r"<code>(.*?)</code>", r"`\1`", s)
    s = re.sub(r"<br\s*/?>", "  \n", s)
    s = re.sub(r"<[^>]+>", "", s)        # strip any remaining tags
    return html.unescape(s).strip()


def _list_items(block, used):
    return [inline_md(m, used) for m in re.findall(r"<li[^>]*>(.*?)</li>", block, re.S)]


def block_to_md(block, used):
    b = block.strip()

    # figure (drop SVG, keep caption); photo figures keep the image
    if b.startswith("<figure"):
        cap = re.search(r"<figcaption>(.*?)</figcaption>", b, re.S)
        cap_txt = inline_md(re.sub(r"<span class='fignum'>.*?</span>", "", cap.group(1)), used) if cap else ""
        img = re.search(r"<img [^>]*src='([^']+)'[^>]*alt='([^']*)'", b)
        if img:
            return f"![{html.unescape(img.group(2))}]({img.group(1)})\n\n*{cap_txt}*"
        return f"> **Diagram.** {cap_txt}"

    # callout
    if b.startswith("<div class='callout"):
        kind = (re.search(r"callout (\w+)", b) or [None, "note"])[1]
        ctitle = re.search(r"<div class='ctitle'>(.*?)</div>", b, re.S)
        cbody = re.search(r"<div class='cbody'>(.*)</div>\s*</div>\s*$", b, re.S)
        title_md = inline_md(ctitle.group(1), used) if ctitle else ""
        body_inner = cbody.group(1) if cbody else b
        if ctitle:
            body_inner = body_inner.replace(ctitle.group(0), "", 1)
        body_md = "\n".join(block_to_md(x, used) for x in _split_blocks(body_inner)) or inline_md(body_inner, used)
        head = f"**{kind.upper()} — {title_md}**" if title_md else f"**{kind.upper()}**"
        return "> " + (head + "\n\n" + body_md).replace("\n", "\n> ")

    # definition
    if b.startswith("<div class='defn'"):
        t = re.search(r"<span class='defn-t'>(.*?)</span>", b, re.S)
        d = re.search(r"<span class='defn-b'>(.*?)</span>", b, re.S)
        return f"**{inline_md(t.group(1), used) if t else ''}** — {inline_md(d.group(1), used) if d else ''}"

    # table
    if b.startswith("<div class='tbl-wrap'") or b.startswith("<table"):
        heads = re.findall(r"<th[^>]*>(.*?)</th>", b, re.S)
        rows = re.findall(r"<tr>(.*?)</tr>", b, re.S)
        cap = re.search(r"<caption>(.*?)</caption>", b, re.S)
        out = []
        if heads:
            out.append("| " + " | ".join(inline_md(h, used) for h in heads) + " |")
            out.append("| " + " | ".join("---" for _ in heads) + " |")
        for r in rows:
            cells = re.findall(r"<td[^>]*>(.*?)</td>", r, re.S)
            if cells:
                out.append("| " + " | ".join(inline_md(c, used).replace("\n", " ") for c in cells) + " |")
        if cap:
            out.append("\n*" + inline_md(cap.group(1), used) + "*")
        return "\n".join(out)

    # ordered steps
    if b.startswith("<ol class='steps'"):
        items = []
        for i, m in enumerate(re.findall(r"<li class='step'>(.*?)</li>", b, re.S), 1):
            t = re.search(r"<div class='step-t'>(.*?)</div>", m, re.S)
            d = re.search(r"<div class='step-b'>(.*?)</div>", m, re.S)
            items.append(f"{i}. **{inline_md(t.group(1), used) if t else ''}** — {inline_md(d.group(1), used) if d else ''}")
        return "\n".join(items)

    # lists
    if b.startswith("<ol"):
        return "\n".join(f"{i}. {it}" for i, it in enumerate(_list_items(b, used), 1))
    if b.startswith("<ul"):
        return "\n".join(f"- {it}" for it in _list_items(b, used))

    # kv
    if b.startswith("<div class='kv'"):
        out = []
        for k, v in re.findall(r"<span class='kv-k'>(.*?)</span><span class='kv-v'>(.*?)</span>", b, re.S):
            out.append(f"- **{inline_md(k, used)}:** {inline_md(v, used)}")
        return "\n".join(out)

    # grid of cards
    if b.startswith("<div class='grid"):
        out = []
        for c in re.findall(r"<div class='card'>(.*?)</div></div>", b, re.S):
            tt = re.search(r"<div class='card-title'>(.*?)</div>", c, re.S)
            bb = re.search(r"<div class='card-body'>(.*)$", c, re.S)
            title = inline_md(tt.group(1), used) if tt else ""
            body = "\n".join(block_to_md(x, used) for x in _split_blocks(bb.group(1))) if bb else ""
            out.append(f"**{title}**\n\n{body}")
        return "\n\n".join(out)

    # stagecard
    if b.startswith("<div class='stagecard'"):
        return inline_md(b, used)

    # headings
    m = re.match(r"<h([2-4])[^>]*>(.*?)</h\1>", b, re.S)
    if m:
        return ("#" * (int(m.group(1)) + 1)) + " " + inline_md(m.group(2), used)

    # lead / paragraph
    if b.startswith("<p"):
        return inline_md(re.sub(r"^<p[^>]*>|</p>$", "", b), used)

    # fallback: strip
    return inline_md(b, used)


def _split_blocks(html_str):
    """Split a concatenated blocks string into top-level block strings."""
    blocks, depth, buf = [], 0, ""
    # tokenç by top-level tags is hard; rely on the fact that build joins blocks with no
    # separator but each block is a single top-level element. Walk tags tracking depth.
    i = 0
    s = html_str
    while i < len(s):
        if s[i] == "<":
            j = s.find(">", i)
            if j == -1:
                buf += s[i:]; break
            tag = s[i:j + 1]
            buf += tag
            name = re.match(r"</?([a-zA-Z0-9]+)", tag)
            selfclose = tag.endswith("/>") or (name and name.group(1).lower() in ("img", "br", "hr", "rect", "line", "circle", "path", "input"))
            if name and not selfclose:
                if tag.startswith("</"):
                    depth -= 1
                    if depth == 0:
                        blocks.append(buf); buf = ""
                else:
                    depth += 1
            i = j + 1
        else:
            buf += s[i]; i += 1
    if buf.strip():
        blocks.append(buf)
    return [b for b in blocks if b.strip()]


# ---------------------------------------------------------------- per-paper
def _meta(mod):
    rt = dg = ""
    for _ic, txt in getattr(mod, "META", []):
        if "read" in txt.lower():
            rt = txt
        if "diagram" in txt.lower():
            dg = txt
    return rt, dg


def paper_md(mod):
    used = set()
    body = []
    for sec in mod.SECTIONS:
        title = html.unescape(re.sub(r"<[^>]+>", "", sec["title"]))
        body.append(f"## {title}\n")
        for blk in sec["blocks"]:
            md = block_to_md(blk, used)
            if md.strip():
                body.append(md + "\n")
    # references (footnote defs for every declared ref, in order)
    refs_struct = []
    foot = ["## References\n"]
    for n, rid in enumerate(mod.REF_IDS, 1):
        r = REFS.get(rid)
        if not r:
            continue
        cite = html.unescape(re.sub(r"<[^>]+>", "", r["cite"]))
        tag = "peer-reviewed" if r.get("peer") else "industry/manufacturer source"
        url = r.get("url", "")
        foot.append(f"[^{rid}]: {cite} {url} ({tag})")
        refs_struct.append({"id": rid, "n": n, "cite": cite, "url": url, "peer": bool(r.get("peer"))})

    rt, dg = _meta(mod)
    fm = {
        "slug": mod.SLUG, "title": html.unescape(mod.TITLE),
        "eyebrow": html.unescape(mod.EYEBROW), "summary": html.unescape(mod.SUB),
        "track": SLUG_GROUP.get(mod.SLUG, ""), "read_time": rt, "diagrams": dg,
        "related": list(getattr(mod, "RELATED", [])),
        "url": f"{BASE}/{mod.SLUG}.html", "md_url": f"{BASE}/papers/{mod.SLUG}.md",
        "version": VERSION, "updated": UPDATED,
        "license": LICENSE_ID, "license_url": LICENSE_URL, "attribution": ATTRIBUTION,
        "refs": refs_struct,
    }
    front = "---\n" + "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in fm.items()) + "\n---\n"
    md = front + f"\n# {fm['title']}\n\n_{fm['eyebrow']} · {rt}_\n\n> {fm['summary']}\n\n" + "\n".join(body) + "\n" + "\n".join(foot) + "\n"
    return md, fm


# ---------------------------------------------------------------- outputs
def main():
    papers_dir = os.path.join(ROOT, "papers")
    os.makedirs(papers_dir, exist_ok=True)
    manifest, leaks, full = [], [], []

    for mod in build.PAPERS:
        md, fm = paper_md(mod)
        hits = sorted(set(LEAK.findall(md)))
        if hits:
            leaks.append((mod.SLUG, hits))
        with open(os.path.join(papers_dir, mod.SLUG + ".md"), "w", encoding="utf-8") as f:
            f.write(md)
        manifest.append({k: fm[k] for k in ("slug", "title", "summary", "track", "read_time",
                                            "diagrams", "related", "url", "md_url", "version", "updated")}
                        | {"ref_count": len(fm["refs"])})
        full.append(md.split("---\n", 2)[-1])  # body without frontmatter

    if leaks:
        print("LEAK SCAN FAILED, aborting export:")
        for slug, hits in leaks:
            print(f"  {slug}: {hits}")
        sys.exit(1)

    # manifest.json
    json.dump({"name": ATTRIBUTION, "version": VERSION, "updated": UPDATED,
               "license": LICENSE_ID, "license_url": LICENSE_URL, "base": BASE,
               "count": len(manifest), "papers": manifest},
              open(os.path.join(ROOT, "manifest.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    # glossary.json
    json.dump({"name": ATTRIBUTION + " — glossary", "count": len(GLOSSARY),
               "license": LICENSE_ID, "terms": GLOSSARY},
              open(os.path.join(ROOT, "glossary.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    # llms.txt (curated index, grouped)
    by_group = {}
    for m in manifest:
        by_group.setdefault(m["track"] or "Other", []).append(m)
    L = [f"# {ATTRIBUTION}\n",
         "> Beginner-friendly, peer-reviewed white papers on medical cannabis cultivation: "
         "propagation, crop steering, environment, plant health, precision irrigation, facility and quality.\n",
         f"Licensed {LICENSE_ID} ({LICENSE_URL}). Attribution: {ATTRIBUTION}. "
         f"Each paper has a clean markdown version under /papers/ with sources preserved as footnotes.\n"]
    order = [g["group"] for g in build.NAV.GROUPS]
    for grp in order + [k for k in by_group if k not in order]:
        items = by_group.get(grp)
        if not items:
            continue
        L.append(f"## {grp}")
        for m in items:
            desc = SLUG_SHORT.get(m["slug"]) or m["summary"][:120]
            L.append(f"- [{m['title']}]({m['md_url']}): {desc}")
        L.append("")
    L.append("## Optional")
    L.append(f"- [Full corpus (all papers)]({BASE}/llms-full.txt): every paper concatenated")
    L.append(f"- [Manifest (JSON index)]({BASE}/manifest.json): machine-readable paper index")
    L.append(f"- [Glossary (JSON)]({BASE}/glossary.json): ~270 defined terms")
    open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write("\n".join(L) + "\n")

    # llms-full.txt
    header = (f"# {ATTRIBUTION} — full corpus\n\nLicensed {LICENSE_ID} ({LICENSE_URL}). "
              f"Attribution: {ATTRIBUTION}. {len(manifest)} papers, version {VERSION}, updated {UPDATED}.\n\n")
    open(os.path.join(ROOT, "llms-full.txt"), "w", encoding="utf-8").write(
        header + "\n\n---\n\n".join(full) + "\n")

    # LICENSE
    open(os.path.join(ROOT, "LICENSE"), "w", encoding="utf-8").write(
        f"{ATTRIBUTION}\nCreative Commons Attribution-NonCommercial 4.0 International ({LICENSE_ID})\n"
        f"{LICENSE_URL}\n\n"
        "You are free to share and adapt this material for NON-COMMERCIAL purposes, with "
        f"attribution to \"{ATTRIBUTION}\". Commercial use requires permission.\n"
        "Full legal text: " + LICENSE_URL + "legalcode\n")

    print(f"corpus OK -> {len(manifest)} papers + manifest/glossary/llms.txt/llms-full.txt/LICENSE  (leak-scan clean)")


if __name__ == "__main__":
    main()
