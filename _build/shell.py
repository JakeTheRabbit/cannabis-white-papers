# -*- coding: utf-8 -*-
"""Page chrome: sidebar, mobile top bar, bottom thumb-nav, on-this-page rail,
search modal, and the full HTML document wrapper. Flat site (root-relative-free)."""
from components import icon, esc
import data.nav as NAV

BRAND = "The Cannabis White Papers"
ASSET_VER = "0"  # set by build.py to a content hash, busts browser cache on deploy

def _href(slug):
    return "index.html" if slug == "index" else f"{slug}.html"

def sidebar(active):
    out = ['<aside class="sidebar" id="sidebar">']
    out.append('<div class="brandrow"><a class="brand" href="index.html"><span class="mark">C</span>'
               '<span class="nm">The Cannabis White Papers<small>FIELD GUIDE</small></span></a>'
               f'<button class="themebtn" data-action="theme" aria-label="Toggle dark mode">{icon("moon",17)}</button></div>')
    out.append('<button class="cmdk" data-action="search" aria-label="Search">'
               f'{icon("search",15)}<span class="seg">Search papers &amp; terms</span>'
               '<span class="kbd">Ctrl K</span></button>')
    out.append('<nav class="nav">')
    for t in NAV.TOP:
        on = " on" if t["slug"] == active else ""
        out.append(f'<a class="{on.strip()}" href="{_href(t["slug"])}">{icon(t["icon"],17)}<span>{t["title"]}</span></a>')
    for g in NAV.GROUPS:
        out.append(f'<div class="navgrp">{esc(g["group"])}</div>')
        for it in g["items"]:
            ic = icon(it["icon"], 17)
            if it["status"] == "live":
                on = " on" if it["slug"] == active else ""
                out.append(f'<a class="{on.strip()}" href="{_href(it["slug"])}">{ic}<span>{esc(it["title"])}</span></a>')
            else:
                out.append(f'<span class="nav-soon" style="display:flex;align-items:center;gap:11px;padding:8px 11px;'
                           f'border-radius:9px;font-size:13.5px;color:var(--faint)">{ic}'
                           f'<span class="seg">{esc(it["title"])}</span>'
                           f'<span class="badge-soon">soon</span></span>')
    out.append('</nav></aside>')
    return "".join(out)

def bottomnav(active):
    items = [
        ("index", "Home", "home"),
        ("papers", "Papers", "grid"),
        ("__search", "Search", "search"),
        ("glossary", "Terms", "book"),
        ("__menu", "Menu", "menu"),
    ]
    out = ['<nav class="bottomnav">']
    for slug, label, ic in items:
        if slug == "__search":
            out.append(f'<a data-action="search" role="button">{icon(ic,21)}{label}</a>')
        elif slug == "__menu":
            out.append(f'<a data-action="menu" role="button">{icon(ic,21)}{label}</a>')
        else:
            on = " on" if slug == active else ""
            out.append(f'<a class="{on.strip()}" href="{_href(slug)}">{icon(ic,21)}{label}</a>')
    out.append('</nav>')
    return "".join(out)

def rail(toc):
    if not toc:
        return ""
    links = "".join(f'<a href="#{tid}">{esc(label)}</a>' for tid, label in toc)
    return f'<aside class="rail"><div class="lbl">On this page</div>{links}</aside>'

def page(slug, title, body, desc="", rail_toc=None, wide=False, mobile_active=None):
    """Assemble one full HTML document."""
    macc = mobile_active or slug
    doc_class = "doc wide" if wide else "doc"
    has_rail = bool(rail_toc) and not wide
    if has_rail:
        main = f'<div class="content"><div class="{doc_class}"><div class="col">{body}</div>{rail(rail_toc)}</div></div>'
    else:
        cls = "content wide" if wide else "content"
        main = f'<div class="{cls}"><div class="col">{body}</div></div>'
    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} &middot; {esc(BRAND)}</title>
<meta name="description" content="{esc(desc)}">
<script>(function(){{try{{var t=localStorage.getItem('cwp-theme')||(window.matchMedia&&window.matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light');document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}}})();</script>
<link rel="stylesheet" href="assets/app.css?v={ASSET_VER}">
</head><body data-slug="{esc(slug)}">
<button class="drawer-mask" id="mask" aria-label="Close menu"></button>
<header class="mtopbar">
  <button class="iconbtn" data-action="menu" aria-label="Open menu">{icon('menu',22)}</button>
  <span class="mt">{esc(title)}</span>
  <button class="iconbtn" data-action="theme" aria-label="Toggle dark mode">{icon('moon',20)}</button>
  <button class="iconbtn" data-action="search" aria-label="Search">{icon('search',20)}</button>
</header>
<div class="layout">
  {sidebar(macc)}
  {main}
</div>
{bottomnav(macc)}
<div class="search-mask" id="searchMask">
  <div class="search-box">
    <input id="searchInput" type="text" placeholder="Search papers, sections and terms…" autocomplete="off" spellcheck="false">
    <div class="search-results" id="searchResults"></div>
  </div>
</div>
<script src="assets/search-index.js?v={ASSET_VER}"></script>
<script src="assets/app.js?v={ASSET_VER}"></script>
</body></html>"""
