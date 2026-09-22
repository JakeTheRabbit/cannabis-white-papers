// Serves the white-papers static site under /wiki on growlabs.nz.
// The assets binding holds the repo root, so every request has the prefix stripped
// before lookup. /whitepapers is an alias that redirects to /wiki.

const PREFIX = "/wiki";
const ALIAS = "/whitepapers";

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    if (path === ALIAS || path.startsWith(`${ALIAS}/`)) {
      const rest = path.slice(ALIAS.length) || "/";
      return Response.redirect(`${url.origin}${PREFIX}${rest}${url.search}`, 301);
    }
    if (path === PREFIX) {
      return Response.redirect(`${url.origin}${PREFIX}/${url.search}`, 301);
    }
    if (!path.startsWith(`${PREFIX}/`)) {
      return new Response("Not found", { status: 404 });
    }

    let assetPath = path.slice(PREFIX.length);
    if (assetPath.endsWith("/")) assetPath += "index.html";

    const fetchAsset = (p) => {
      const u = new URL(url);
      u.pathname = p;
      return env.ASSETS.fetch(new Request(u, request));
    };

    let res = await fetchAsset(assetPath);
    if (res.status === 404 && !/\.[^/]+$/.test(assetPath)) {
      res = await fetchAsset(`${assetPath}.html`);
    }
    return res;
  },
};
