#!/usr/bin/env python3
"""Build CRAFT-pitch.pdf from CRAFT-pitch.md + pdf-style.css + diagrams/*.svg.

Uses Python `markdown` (with the `tables` extension and raw HTML passthrough)
plus WeasyPrint. SVGs are referenced via <object> in the markdown and are
embedded by WeasyPrint when it loads the HTML with base_url set to this
directory. Copies the result to ~/Downloads/ when that directory exists.
"""
from __future__ import annotations

import pathlib
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
MD = HERE / "CRAFT-pitch.md"
CSS = HERE / "pdf-style.css"
HTML = HERE / "CRAFT-pitch.html"
PDF = HERE / "CRAFT-pitch.pdf"


def main() -> None:
    try:
        import markdown
    except ImportError:
        sys.exit("error: install markdown (pip install markdown)")
    try:
        from weasyprint import HTML as WeasyHTML
    except ImportError:
        sys.exit("error: install weasyprint (pip install weasyprint)")

    md_text = MD.read_text(encoding="utf-8")
    body_html = markdown.markdown(
        md_text,
        extensions=["tables", "attr_list", "md_in_html"],
    )
    css_text = CSS.read_text(encoding="utf-8")

    html_doc = (
        "<!doctype html><html><head><meta charset='utf-8'>"
        "<title>CRAFT — Pitch Package</title>"
        f"<style>{css_text}</style></head><body>{body_html}</body></html>"
    )
    HTML.write_text(html_doc, encoding="utf-8")

    WeasyHTML(string=html_doc, base_url=str(HERE)).write_pdf(str(PDF))
    print(f"wrote {PDF}")

    downloads = pathlib.Path.home() / "Downloads"
    if downloads.is_dir():
        dest = downloads / PDF.name
        shutil.copy2(PDF, dest)
        print(f"copied → {dest}")


if __name__ == "__main__":
    main()
