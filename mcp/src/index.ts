/**
 * The Cannabis White Papers - remote MCP server (Cloudflare Worker).
 *
 * Stateless Streamable-HTTP MCP server (no Durable Objects, no SDK dependency),
 * backed by a Workers KV namespace loaded from the corpus exporter.
 * Connector URL: https://<worker>.workers.dev/mcp
 *
 * KV keys (loaded via `wrangler kv bulk put`): manifest, searchdocs, glossary,
 * paper:<slug>.
 */

export interface Env {
  CORPUS: KVNamespace;
}

const SERVER = { name: "cannabis-white-papers", version: "1.0" };
const ATTRIB =
  "The Cannabis White Papers (CC BY-NC 4.0, https://creativecommons.org/licenses/by-nc/4.0/)";

const TOOLS = [
  {
    name: "search_papers",
    description:
      "Search the cannabis-cultivation white papers by keyword. Returns the best-matching papers with slug, title, stage and a snippet. Use this first, then get_paper for the full text.",
    inputSchema: {
      type: "object",
      properties: {
        query: { type: "string", description: "Search terms, e.g. 'rockwool dryback' or 'powdery mildew'" },
        limit: { type: "number", description: "Max results (default 5)" },
      },
      required: ["query"],
    },
  },
  {
    name: "get_paper",
    description:
      "Get one full white paper as clean markdown (with citations as [^id] footnotes), by its slug. Get slugs from search_papers or list_papers.",
    inputSchema: {
      type: "object",
      properties: { slug: { type: "string", description: "Paper slug, e.g. 'rockwool-crop-steering'" } },
      required: ["slug"],
    },
  },
  {
    name: "list_papers",
    description: "List all white papers (slug, title, stage, summary), grouped data for browsing.",
    inputSchema: { type: "object", properties: {} },
  },
  {
    name: "search_glossary",
    description: "Search the cultivation glossary for terms matching a query. Returns matching term/definition pairs.",
    inputSchema: {
      type: "object",
      properties: { query: { type: "string", description: "A term or part of one, e.g. 'dryback'" } },
      required: ["query"],
    },
  },
  {
    name: "get_glossary_term",
    description: "Get the plain-English definition of one glossary term (exact or closest match).",
    inputSchema: {
      type: "object",
      properties: { term: { type: "string" } },
      required: ["term"],
    },
  },
];

const CORS: Record<string, string> = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Mcp-Session-Id, Mcp-Protocol-Version, Authorization",
  "Access-Control-Max-Age": "86400",
};

function tokens(s: string): string[] {
  return (s.toLowerCase().match(/[a-z0-9]+/g) || []).filter((t) => t.length > 1);
}

async function searchPapers(env: Env, query: string, limit = 5) {
  const docs: any[] = JSON.parse((await env.CORPUS.get("searchdocs")) || "[]");
  const qs = tokens(query);
  if (!qs.length) return [];
  const scored = docs
    .map((d) => {
      const t = d.text as string;
      let score = 0;
      for (const q of qs) {
        if (d.title.toLowerCase().includes(q)) score += 5;
        const m = t.split(q).length - 1;
        score += m;
      }
      let snippet = d.summary;
      const pos = t.indexOf(qs[0]);
      if (pos >= 0) snippet = "…" + t.slice(Math.max(0, pos - 80), pos + 160).trim() + "…";
      return { slug: d.slug, title: d.title, track: d.track, summary: d.summary, snippet, score };
    })
    .filter((d) => d.score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, Math.max(1, Math.min(20, limit)));
  return scored;
}

function textResult(text: string) {
  return { content: [{ type: "text", text }] };
}

async function callTool(env: Env, name: string, args: any) {
  if (name === "search_papers") {
    const res = await searchPapers(env, String(args?.query || ""), Number(args?.limit) || 5);
    if (!res.length) return textResult(`No papers matched "${args?.query}". Try list_papers.`);
    const body = res
      .map(
        (r: any) =>
          `### ${r.title}\n- slug: \`${r.slug}\`\n- stage: ${r.track}\n- ${r.summary}\n- match: ${r.snippet}`
      )
      .join("\n\n");
    return textResult(`Top ${res.length} matching papers.\n\n${body}\n\nUse get_paper(slug) for the full text.`);
  }
  if (name === "get_paper") {
    const md = await env.CORPUS.get("paper:" + String(args?.slug || ""));
    return textResult(md || `No paper with slug "${args?.slug}". Use list_papers for valid slugs.`);
  }
  if (name === "list_papers") {
    const man: any = JSON.parse((await env.CORPUS.get("manifest")) || '{"papers":[]}');
    const body = man.papers
      .map((p: any) => `- \`${p.slug}\` [${p.track}] ${p.title} — ${p.summary}`)
      .join("\n");
    return textResult(`${man.papers.length} papers (${ATTRIB}):\n\n${body}`);
  }
  if (name === "search_glossary") {
    const g: any[] = JSON.parse((await env.CORPUS.get("glossary")) || "[]");
    const q = String(args?.query || "").toLowerCase();
    const hits = g.filter(
      (t) => t.term.toLowerCase().includes(q) || (t.defn || "").toLowerCase().includes(q)
    );
    if (!hits.length) return textResult(`No glossary terms matched "${args?.query}".`);
    return textResult(hits.slice(0, 20).map((t) => `**${t.term}** — ${t.defn}`).join("\n\n"));
  }
  if (name === "get_glossary_term") {
    const g: any[] = JSON.parse((await env.CORPUS.get("glossary")) || "[]");
    const q = String(args?.term || "").toLowerCase();
    const hit = g.find((t) => t.term.toLowerCase() === q) || g.find((t) => t.term.toLowerCase().includes(q));
    return textResult(hit ? `**${hit.term}** — ${hit.defn}` : `No glossary term "${args?.term}".`);
  }
  throw { code: -32601, message: `Unknown tool: ${name}` };
}

async function handleRpc(env: Env, msg: any): Promise<any | null> {
  const { id, method, params } = msg;
  // notifications (no id) get no response
  if (id === undefined || id === null) return null;
  try {
    let result: any;
    if (method === "initialize") {
      result = {
        protocolVersion: params?.protocolVersion || "2025-06-18",
        capabilities: { tools: {} },
        serverInfo: SERVER,
        instructions:
          "Peer-reviewed cannabis cultivation white papers. search_papers then get_paper; " +
          "search_glossary for terms. " + ATTRIB,
      };
    } else if (method === "tools/list") {
      result = { tools: TOOLS };
    } else if (method === "tools/call") {
      result = await callTool(env, params?.name, params?.arguments || {});
    } else if (method === "ping") {
      result = {};
    } else {
      return { jsonrpc: "2.0", id, error: { code: -32601, message: `Method not found: ${method}` } };
    }
    return { jsonrpc: "2.0", id, result };
  } catch (e: any) {
    return { jsonrpc: "2.0", id, error: { code: e?.code || -32603, message: e?.message || String(e) } };
  }
}

export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    const url = new URL(req.url);
    if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: CORS });

    if (req.method === "GET" && (url.pathname === "/" || url.pathname === "")) {
      return new Response(
        `${SERVER.name} MCP server. POST JSON-RPC to /mcp. Tools: ${TOOLS.map((t) => t.name).join(", ")}. ${ATTRIB}`,
        { headers: { "Content-Type": "text/plain", ...CORS } }
      );
    }
    // Streamable HTTP: this server has no server-initiated stream, so GET on the
    // MCP endpoint is not supported.
    if (req.method === "GET") return new Response("Method Not Allowed", { status: 405, headers: CORS });

    if (req.method === "POST") {
      let payload: any;
      try {
        payload = await req.json();
      } catch {
        return new Response(
          JSON.stringify({ jsonrpc: "2.0", id: null, error: { code: -32700, message: "Parse error" } }),
          { status: 400, headers: { "Content-Type": "application/json", ...CORS } }
        );
      }
      if (Array.isArray(payload)) {
        const out = (await Promise.all(payload.map((m) => handleRpc(env, m)))).filter((x) => x !== null);
        return new Response(out.length ? JSON.stringify(out) : "", {
          status: out.length ? 200 : 202,
          headers: { "Content-Type": "application/json", ...CORS },
        });
      }
      const res = await handleRpc(env, payload);
      if (res === null) return new Response("", { status: 202, headers: CORS });
      return new Response(JSON.stringify(res), {
        headers: { "Content-Type": "application/json", ...CORS },
      });
    }
    return new Response("Method Not Allowed", { status: 405, headers: CORS });
  },
};
