#!/usr/bin/env python3
"""seo-scaffold.py — scaffold a new SEO article folder from the house pattern.

Run via gitmap only:
    gitmap py 03-ai-scripts/seo-scaffold.py --group 05-riseup-asia-brand \
        --slug my-article --title "My Article" [--area "San Diego"] \
        [--keywords "AI,software engineers"] [--dest 01-seo-writing]

Creates <dest>/<group>[/<area-seq>-<area>]/<slug>/ containing:
    writing.md               master markdown article with yaml frontmatter
    medium-ready.html        standalone styled html rendering the body
    score.md                 100-point checklist skeleton (see seo-rules.md)
    infographic-philosophy.md  template for the visual rationale

Never writes PDF — PDF is the final step via seo-pdf.py.
"""

import argparse
import datetime
import os
import sys

MEDIUM_CSS = (
    "body{font-family:Georgia,serif;color:#1f1f1f;max-width:760px;"
    "margin:40px auto;padding:0 24px;line-height:1.72;font-size:20px}"
    "h1{font-size:44px;line-height:1.12;margin-bottom:32px}"
    "p{margin:0 0 24px}ol{margin:0 0 28px;padding-left:30px}"
    "li{margin-bottom:18px}a{color:#1f1f1f;text-decoration:underline;"
    "text-decoration-thickness:1px;text-underline-offset:3px}"
    "figure{margin:36px 0}img{display:block;max-width:100%;height:auto}"
    "figcaption{font-size:14px;line-height:1.4;color:#666;margin-top:10px}"
    "@page{size:A4;margin:2cm}"
)

WRITING_SKELETON = """{title}

<!-- SECTION 1: cold-open scene. Place the reader in a real street, cafe, or
     office in {area}. Concrete sensory detail: weather, sounds, one small
     human moment. First-person voice. No bold, no italics. -->
[Write the cold-open scene here.]

<!-- SECTION 2: pivot to thesis. Connect the scene to the AI / software /
     business question this article answers. State the tension honestly:
     what looks true from a distance vs what the evidence shows up close. -->
[Write the thesis pivot here.]

<!-- SECTION 3: RISEUP ASIA LLC contrast. Bring in the company's engineering
     method — retrieval grounded in controlled sources, evaluations before
     release, cost-per-run budgets, fallback behavior, accountable ownership.
     Frame it as a working method, not a boast. -->
[Write the RISEUP ASIA LLC contrast here.]

<!-- SECTION 4: compare and contrast. Test the claim against opposing
     evidence. Acknowledge what challenges your own argument — that honesty
     is what gives the article its credibility. -->
[Write the compare-and-contrast section here.]

<!-- SECTION 5: ranking. Numbered list of 3-5 entries, each with a cited
     reason. Declare the criteria; justify every position; state the limits
     of the evidence. -->
[Write the ranked list here.]

<!-- SECTION 6: reflective close. Return to the opening scene or a final
     image. End on a judgment the reader must make, not on a slogan. -->
[Write the reflective close here.]

![{title} infographic: describe the visual and its argument here.](infographic-1.png)
"""

SCORE_TEMPLATE = """# Score: {title}

## Score table

| Category | Score | Validation |
|---|---:|---|
| Area mentioned 30-40 times, blended naturally | /20 | |
| Focus keyword 1-2x in the first paragraphs | /10 | |
| Brand keywords 20-30x, blended naturally | /15 | |
| At least one question built on the target topic | /10 | |
| House structure + plain formatting followed | /10 | |
| Citations real, each verified 2-3x by re-fetching | /15 | |
| Infographics contain the target keywords | /10 | |
| HTML + PDF present and correct | /10 | |

Deduct 5 points per `[VERIFY]` placeholder left in the text.

## Overall score

| Calculation | Result |
|---|---:|
| Sum of 8 category scores | /100 |

## Evidence corrections applied

| Rough-draft idea | Published treatment |
|---|---|
| | |

## Measured checks

| Check | Result |
|---|---:|
| Sentences checked | |
| Area mentions (target 30-40) | |
| Brand keyword mentions (target 20-30) | |
| Descriptive external links | |
| Article images | |
| [VERIFY] placeholders remaining | |

## Source notes

-
"""

PHILOSOPHY_TEMPLATE = """# Infographic philosophy: {title}

## Central metaphor
[What single image or contrast carries the article's argument? Keep it to one idea.]

## Evidence pairs
[Which 2 pairs of sourced numbers or claims does the visual compare? Label every scope and period.]

## Engineering channel
[How does the visual show the RISEUP ASIA LLC method: problem, data, evaluation, cost, accountable owner?]

## Color behavior
[What does each color mean? No promotional gradients; neutral charcoal for labels.]

## Typography
[Only large factual labels get display type. Area and keyword text must be readable at Medium width.]

## Constraints
[Legible margins, no unsupported rankings, no logos, no unverified claims.]
"""


def slugify_area(area):
    return area.strip().lower().replace(" ", "-")


def body_to_html(body_md):
    """Minimal markdown -> html for the medium wrapper (fallback when the
    `markdown` pip package is unavailable)."""
    out = []
    in_list = False
    for line in body_md.splitlines():
        stripped = line.strip()
        if stripped.startswith("!["):
            # ![alt](src)
            alt = stripped[2:stripped.index("]")]
            src = stripped[stripped.index("(") + 1:stripped.index(")")]
            out.append(
                '<figure><img src="%s" alt="%s">'
                "<figcaption>%s</figcaption></figure>" % (src, alt, alt)
            )
            continue
        if stripped and stripped[0].isdigit() and ". " in stripped[:4]:
            if not in_list:
                out.append("<ol>")
                in_list = True
            item = stripped.split(". ", 1)[1]
            out.append("<li>%s</li>" % inline_md(item))
            continue
        if in_list:
            out.append("</ol>")
            in_list = False
        if stripped.startswith("#"):
            out.append("<h2>%s</h2>" % inline_md(stripped.lstrip("#").strip()))
        elif stripped:
            out.append("<p>%s</p>" % inline_md(stripped))
    if in_list:
        out.append("</ol>")
    return "\n".join(out)


def inline_md(text):
    import html as html_mod
    import re
    text = html_mod.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def render_html(title, body_md):
    try:
        import markdown
        body_html = markdown.markdown(body_md, extensions=["extra"])
    except ImportError:
        body_html = body_to_html(body_md)
    return (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "<title>%s</title>\n<style>%s</style>\n</head>\n<body>\n<article>\n"
        "<h1>%s</h1>\n%s\n</article>\n</body>\n</html>\n"
        % (title, MEDIUM_CSS, title, body_html)
    )


def strip_frontmatter(text):
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3:].lstrip("\n")
    return text


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Scaffold a new SEO article folder from the house pattern."
    )
    parser.add_argument("--group", required=True, help="group folder, e.g. 05-riseup-asia-brand")
    parser.add_argument("--slug", required=True, help="article folder name, e.g. my-article")
    parser.add_argument("--title", required=True, help="article title")
    parser.add_argument("--area", default="", help='target area, e.g. "San Diego"')
    parser.add_argument("--keywords", default="", help="comma-separated focus keywords")
    parser.add_argument("--dest", default="01-seo-writing", help="root output dir")
    args = parser.parse_args(argv)

    group_dir = args.group.strip().lower().replace(" ", "-")
    slug = args.slug.strip().lower().replace(" ", "-")
    area = args.area.strip()
    if area:
        article_dir = os.path.join(args.dest, group_dir, "01-" + slugify_area(area), slug)
    else:
        article_dir = os.path.join(args.dest, group_dir, slug)
    os.makedirs(article_dir, exist_ok=False)

    today = datetime.date.today().isoformat()
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    kw_yaml = "[" + ", ".join('"%s"' % k for k in keywords) + "]"

    frontmatter = (
        "---\ntitle: \"%s\"\nslug: \"%s\"\narea: \"%s\"\nkeywords: %s\n"
        "date: %s\nstatus: draft\n---\n\n" % (args.title, slug, area, kw_yaml, today)
    )
    body_md = WRITING_SKELETON.format(title=args.title, area=area or "[AREA]")

    paths = {
        "writing.md": frontmatter + body_md,
        "medium-ready.html": render_html(args.title, body_md),
        "score.md": SCORE_TEMPLATE.format(title=args.title),
        "infographic-philosophy.md": PHILOSOPHY_TEMPLATE.format(title=args.title),
    }
    for name, content in paths.items():
        with open(os.path.join(article_dir, name), "w", encoding="utf-8") as f:
            f.write(content)

    rel = os.path.relpath(article_dir)
    print("scaffolded: %s" % rel)
    for name in sorted(paths):
        print("  - %s/%s" % (rel, name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
