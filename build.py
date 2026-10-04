#!/usr/bin/env python3
"""Genera index.html a partir de slides-src/ (diapositivas 1920x1080 con estilos inline)."""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "slides-src"

deck = json.loads((SRC / "deck.json").read_text())
blobmap = json.loads((SRC / "blobmap.json").read_text())
start_to_section = {s["start"]: s["description"] for s in deck["sections"].values()}

slides = []
for i, sid in enumerate(deck["order"]):
    raw = (SRC / f"{sid}.html").read_text()
    raw = re.sub(r"/_blob/([0-9a-f]{32})", lambda m: blobmap[m.group(1)], raw)
    notes = re.search(r"<aside>(.*?)</aside>", raw, re.S)
    raw = re.sub(r"<aside>.*?</aside>", "", raw, flags=re.S)
    raw = raw.replace("<img ", '<img loading="lazy" decoding="async" ' if i > 1 else "<img ", -1)
    title = re.search(r"<h[123][^>]*>(.*?)</h[123]>", raw, re.S)
    title = re.sub(r"<[^>]+>", " ", title.group(1)) if title else sid
    title = " ".join(html.unescape(title).split())
    slides.append({
        "id": sid,
        "html": raw,
        "title": title,
        "section": start_to_section.get(sid),
        "notes": notes.group(1).strip() if notes else "",
    })

menu = []
for i, s in enumerate(slides):
    if s["section"]:
        menu.append(f'<li><button data-go="{i}">{html.escape(s["section"])}</button></li>')

body = "\n".join(
    f'<div class="slide" data-index="{i}" data-title="{html.escape(s["title"])}" aria-roledescription="diapositiva" '
    f'aria-label="{i + 1} de {len(slides)}: {html.escape(s["title"])}">{s["html"]}</div>'
    for i, s in enumerate(slides)
)

page = (ROOT / "template.html").read_text()
page = page.replace("{{TITLE}}", html.escape(deck["title"]))
page = page.replace("{{SLIDES}}", body)
page = page.replace("{{MENU}}", "\n".join(menu))
page = page.replace("{{COUNT}}", str(len(slides)))
(ROOT / "index.html").write_text(page)
print(f"index.html: {len(slides)} diapositivas")
