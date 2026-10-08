#!/usr/bin/env python3
"""seo-pdf.py — render article folders to PDF. PDF is the FINAL output step.

Run via gitmap only:
    gitmap py 03-ai-scripts/seo-pdf.py <article-dir> [<article-dir> ...]
    gitmap py 03-ai-scripts/seo-pdf.py --all --root 01-seo-writing

Renders medium-ready.html when present; falls back to converting writing.md
(frontmatter stripped) to html via the `markdown` pip package. Writes
<slug>.pdf inside the same article dir. Existing committed PDFs are never
overwritten.

Renderer: weasyprint (proven working in this environment, 2026-10-09).
"""

import argparse
import logging
import os
import sys

try:
    from weasyprint import HTML
except ImportError:
    HTML = None


def strip_frontmatter(text):
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3:].lstrip("\n")
    return text


def writing_md_to_html(title, writing_md):
    from markdown import markdown
    body = markdown(strip_frontmatter(writing_md), extensions=["extra"])
    return (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<title>%s</title>\n"
        "<style>body{font-family:Georgia,serif;max-width:760px;margin:40px auto;"
        "padding:0 24px;line-height:1.72;font-size:18px}"
        "h1{font-size:36px}img{max-width:100%%}@page{size:A4;margin:2cm}</style>\n"
        "</head>\n<body>\n<h1>%s</h1>\n%s\n</body>\n</html>\n"
        % (title, title, body)
    )


def render_dir(article_dir):
    """Render one article dir to <slug>.pdf. Returns (ok, message)."""
    if HTML is None:
        return False, "weasyprint not importable; install it first"
    slug = os.path.basename(os.path.normpath(article_dir))
    pdf_path = os.path.join(article_dir, slug + ".pdf")
    if os.path.exists(pdf_path):
        return True, "skipped (already exists): %s" % pdf_path

    html_path = os.path.join(article_dir, "medium-ready.html")
    md_path = os.path.join(article_dir, "writing.md")
    if os.path.exists(html_path):
        source = HTML(filename=html_path)
    elif os.path.exists(md_path):
        with open(md_path, encoding="utf-8") as f:
            writing = f.read()
        source = HTML(
            string=writing_md_to_html(slug.replace("-", " ").title(), writing),
            base_url=article_dir + os.sep,
        )
    else:
        return False, "no medium-ready.html and no writing.md in %s" % article_dir

    try:
        source.write_pdf(pdf_path)
    except Exception as exc:  # noqa: BLE001 - surface the real error
        return False, "render failed for %s: %s" % (article_dir, exc)
    size = os.path.getsize(pdf_path)
    return True, "wrote %s (%d bytes)" % (pdf_path, size)


def iter_article_dirs(root):
    for entry in sorted(os.listdir(root)):
        path = os.path.join(root, entry)
        if not os.path.isdir(path) or entry.startswith((".", "_")):
            continue
        if os.path.exists(os.path.join(path, "writing.md")) or os.path.exists(
            os.path.join(path, "medium-ready.html")
        ):
            yield path
        else:
            yield from iter_article_dirs(path)


def main(argv=None):
    logging.getLogger("weasyprint").setLevel(logging.ERROR)
    parser = argparse.ArgumentParser(
        description="Render article folders to PDF (final output step)."
    )
    parser.add_argument("dirs", nargs="*", help="article dir(s) to render")
    parser.add_argument("--all", action="store_true", help="render every article dir found")
    parser.add_argument(
        "--root", default="01-seo-writing", help="root to scan with --all"
    )
    args = parser.parse_args(argv)

    if args.all:
        targets = list(iter_article_dirs(args.root))
    else:
        targets = args.dirs
    if not targets:
        print("nothing to render: pass article dirs or --all --root <dir>")
        return 1

    failures = 0
    for target in targets:
        ok, message = render_dir(target)
        print(("[ok] " if ok else "[FAIL] ") + message)
        if not ok:
            failures += 1
    print("rendered %d dir(s), %d failure(s)" % (len(targets), failures))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
