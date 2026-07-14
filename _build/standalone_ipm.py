# -*- coding: utf-8 -*-
"""Create the self-contained offline edition of the Auckland IPM blueprint."""

from __future__ import annotations

import base64
import mimetypes
import os
import re


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SLUG = "auckland-ipm-blueprint"


def _data_uri(path):
    mime = "image/webp" if path.lower().endswith(".webp") else (mimetypes.guess_type(path)[0] or "application/octet-stream")
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("ascii")
    return f"data:{mime};base64,{data}"


def build():
    src = os.path.join(ROOT, f"{SLUG}.html")
    out = os.path.join(ROOT, "dist", f"{SLUG}-standalone.html")
    html = open(src, encoding="utf-8").read()
    css = open(os.path.join(ROOT, "assets", "app.css"), encoding="utf-8").read()
    js = open(os.path.join(ROOT, "assets", "app.js"), encoding="utf-8").read()
    search_js = open(os.path.join(ROOT, "assets", "search-index.js"), encoding="utf-8").read()

    html, css_n = re.subn(
        r"<link[^>]+href=[\"']assets/app\.css(?:\?v=[^\"']+)?[\"'][^>]*>",
        lambda _match: "<style>" + css + "</style>",
        html,
        count=1,
        flags=re.I,
    )
    html, js_n = re.subn(
        r"<script[^>]+src=[\"']assets/app\.js(?:\?v=[^\"']+)?[\"'][^>]*></script>",
        lambda _match: "<script>" + js + "</script>",
        html,
        count=1,
        flags=re.I,
    )
    html, search_n = re.subn(
        r"<script[^>]+src=[\"']assets/search-index\.js(?:\?v=[^\"']+)?[\"'][^>]*></script>",
        lambda _match: "<script>" + search_js + "</script>",
        html,
        count=1,
        flags=re.I,
    )

    def inline_image(match):
        rel = match.group(1)
        path = os.path.join(ROOT, rel.replace("/", os.sep))
        if not os.path.isfile(path):
            raise FileNotFoundError(path)
        return "src='" + _data_uri(path) + "'"

    html, image_n = re.subn(
        r"src=['\"](assets/img/ipm-blueprint/[^'\"]+)['\"]",
        inline_image,
        html,
        flags=re.I,
    )

    # The standalone file is deliberately inert offline: no manifest or service-worker discovery.
    html = re.sub(r"<link[^>]+rel=[\"']manifest[\"'][^>]*>", "", html, flags=re.I)
    html = html.replace("</head>", "<style>.facility-input{display:grid;gap:6px}.facility-input input,.facility-input textarea{width:100%;padding:10px;border:1px solid #c8c8c8;border-radius:6px;font:inherit}.facility-form{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.facility-input.wide{grid-column:1/-1}@media(max-width:720px){.facility-form{grid-template-columns:1fr}}</style></head>")

    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)

    if css_n != 1 or js_n != 1 or search_n != 1:
        raise RuntimeError(f"asset inline failed: css={css_n}, js={js_n}, search={search_n}")
    if image_n != 23:
        raise RuntimeError(f"expected 23 embedded photo plates, got {image_n}")
    if re.search(r"(?:src|href)=['\"]assets/", html, flags=re.I):
        raise RuntimeError("local asset reference remains in standalone file")
    print(f"standalone OK -> {out} ({image_n} embedded images)")
    return out


if __name__ == "__main__":
    build()
