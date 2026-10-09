# Spec 02 — SEO infographic rollout (v4 design system)

## Goal

Regenerate all 600 infographics (200 articles x infographic-1/2/3, PNG + SVG) in the
approved v4 style: whitespace-first, label-on-top stat cards, data-proof pills,
separated segments. Themes: `warm-editorial` for 05-riseup-asia-brand and
07-engineering-culture; `navy-purple` for 01, 02, 03, 04, 06.

## Renderer

`03-ai-scripts/seo-infographic.py`, run via `gitmap py`. PIL for PNG (1200x630,
`social-og-card` closed canvas), hand-written SVG for the vector twin. Fonts:
Ubuntu 700 headings/numerals, Poppins body (spec 04-typography.md v3.2.0).
Design rules: `02-spec/07-design-system/45-ai-visual-whitespace-discipline.md`
(non-negotiable) + `37-image-specifications.md` (canvas/safe zones).

## Data schema (per render unit JSON)

```json
{
  "articles": [{"slug": "<slug>", "dir": "01-seo-writing/<group>/.../<slug>"}],
  "theme": "navy-purple",
  "cards": [
    {"layout": "stat-label-top", "n": 1, "label": "AI HIGH PERFORMERS",
     "hero": "6%", "proof": [["88% ", "accent"], ["use AI \u00b7 only ", "muted"],
     ["39% ", "accent"], ["see earnings impact", "muted"]]},
    {"layout": "model-cards", "n": 1, "eyebrow": "SOFTWARE FRANCHISE \u00b7 KUALA LUMPUR",
     "hero": "$2M", "headline": "franchise investment",
     "segments": [{"value": "$2M", "label": "INVESTMENT"},
                  {"value": "50%", "label": "PROFIT MARGIN"},
                  {"value": "5 YRS", "label": "OR BREAK-EVEN"}]},
    {"layout": "compare-2col", "n": 3, "title": "...",
     "left": {"head": "AI THEATRE", "rows": ["..."]},
     "right": {"head": "FRANCHISED ENGINEERING", "rows": ["..."]},
     "verdict": "..."},
    {"layout": "ranking-list", "n": 3, "title": "...",
     "rows": [{"rank": 1, "title": "...", "desc": "..."}]},
    {"layout": "bars", "n": 1, "title": "...",
     "bars": [{"label": "Position 1", "pct": 39.8}], "note": "..."}
  ]
}
```

Five layouts: `stat-label-top`, `model-cards`, `compare-2col`, `ranking-list`,
`bars`. Output per card: `infographic-<n>.png` + `infographic-<n>.svg` in the
article dir (overwrite in place — never delete).

## Batch plan

- Formulaic sets (12 template JSONs -> 125 articles): forward-deploy-engineers,
  franchise, 9 software topics, best-seo-company. Content repeats per area.
- Unique (75): 51 craft stories + 18 culture + 6 finance (5 finance articles have
  no infographics yet — create fresh from their philosophy docs).
- Data sources: each article's `infographic-philosophy.md` (+ `writing.md` when
  the philosophy is thin). Numbers must come from the article's cited sources.

## Acceptance

- Every article dir has infographic-1/2/3.png + .svg, all 1200x630, no overlaps
  (renderer self-checks bounding boxes), v4 whitespace rules honored.
- One atomic `gitmap cpf` per completed wave.
