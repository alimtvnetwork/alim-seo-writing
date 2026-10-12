# Spec 04 — Blog Folder Creation and Content Strategy

Version: 1.0.0 (2026-10-13) — new blog root `04-blogs/` with two outlets,
four articles from two dictations, critical-score validation with rewrite pass.

## Goal

Stand up a dedicated blog content area in the repo — separate from the SEO
article project (`01-seo-writing/`) — with one outlet folder for the RISEUP ASIA
company blog and one for Medium. Produce four long-form articles (two per
outlet) from the two latest dictations, written to the same house standard as
the initial story writing: cold-open scene, critical scoring, and a rewrite
pass wherever the score demands it. Localize to California, San Diego, and New
York with recognizable local places; reference the company site once or twice
per article; land the target keyword cluster 30-60x per article, naturally.

## User Request (Verbatim)

> "Based on the recent dictation, you will create separate blog folders for
> Rise Up Asia properly, and also for Medium blogs. In both cases, you will
> write based on critical checking and writing the story as we have done for
> the initial story writing. So similar to this, you will have a critical
> score validating and rewrite some of the articles if required to. So based
> on the new two dictations, I want you to mainly focus on the California,
> San Diego, and New York. Any specific place that is a local place that
> everyone knows, try to include that and try to put this into this story.
> Try to refer back to the website one or two times. Make sure that the
> keywords that we are targeting, that is actually repeated at least 30 to 60
> times at a natural process."

Non-negotiable, high priority. Slug: blog-folder-creation-and-content-strategy.

## Scope

New top-level root `04-blogs/` (sibling of `01-seo-writing/`). Two outlet
folders inside it:

```
04-blogs/
  riseup-asia/            # Outlet 1 — RISEUP ASIA company blog (Worker 01)
    san-diego/
      vibe-coding-is-dead/
    california/
      cheap-h1b-vs-premium-developers/
  medium/                 # Outlet 2 — Medium blogs (Worker 02, sibling subtask)
    new-york/
      vibe-coding-is-dead/
    new-york/
      cheap-h1b-vs-premium-developers/
```

House area-subfolder convention applies: outlet / area / slug. Each article
folder carries the house file set:

- `writing.md` — the master article.
- `score.md` — the critical scorecard (rewrite gate: total >= 95/100).
- `medium-ready.html` — paragraph-identical dark-theme render of final
  writing.md (regenerated after the final rewrite pass).
- `infographic-philosophy.md` — visual brief for the infographic set.

Scaffolding via:

```
gitmap py 03-ai-scripts/seo-scaffold.py --group <outlet> --slug <slug> \
  --title <title> --area <area> --dest 04-blogs
```

Driving dictations (read both before drafting):

- `dictations/riseup-asia-llc/2026-10-12-cheap-h1b-vs-premium-developers.md`
  — cheap hiring is a false economy; premium Asian developers at H1B-level
  cost without the visa paperwork; the iPhone-vs-$100-phone analogy.
- `dictations/riseup-asia-llc/2026-10-12-vibe-coding-is-dead.md` — vibe coding
  is a magic-shop trick; AI demos are empty shells; "it was never alive —
  merely marketing for selling dreams."

## Outlet plan

| # | Article (slug) | Outlet | Area | Local anchor |
|---|---|---|---|---|
| A | vibe-coding-is-dead | riseup-asia | san-diego | Gaslamp Quarter / Balboa Park (cold-open scene) |
| B | cheap-h1b-vs-premium-developers | riseup-asia | california | Silicon Valley — Castro Street, Mountain View (cold-open scene) |
| C | vibe-coding-is-dead | medium | new-york | Manhattan / Brooklyn (cold-open scene) — sibling author scope |
| D | cheap-h1b-vs-premium-developers | medium | new-york | Manhattan / Wall Street (cold-open scene) — sibling author scope |

Articles A+B: this spec + subtask 01 (Worker 01). Articles C+D: sibling
subtask 02 (Worker 02); same dictations, same house rules, New York anchors.

## Keyword & locality strategy

Primary keyword cluster per article = exact phrase + rotated aliases, counted
combined (case-insensitive):

- Article A (riseup-asia / san-diego): `vibe coding`, `hire software
  engineers`, `AI software development`, `real software engineers`,
  `custom software development`.
- Article B (riseup-asia / california): `premium developers`, `hire software
  developers`, `H1B alternative`, `dedicated developers`,
  `premium engineering talent`.
- Articles C+D keyword sets: sibling author scope (mirror the two clusters,
  Medium-angled phrasing).

Locality anchors to weave into scenes, examples, and comparisons (riseup-asia
outlet): San Diego — Gaslamp Quarter, La Jolla / UC San Diego, Sorrento
Valley, Balboa Park; California — Palo Alto, Mountain View (Castro Street),
Menlo Park (Sand Hill Road), SOMA San Francisco, Cupertino (Apple Park).

## Density reconciliation (normative)

The user's instruction (30-60x keyword mentions) OUTRANKS the house 30-40x
area-mention norm. For these four articles:

- The primary keyword cluster (exact phrase + rotated aliases combined) must
  reach 30-60 natural mentions per article.
- No single exact phrase may exceed ~3% density on its own; rotate aliases
  and distribute mentions across the intro, 4-6 body sections, local scenes,
  and the conclusion CTA.
- score.md replaces the house "Area mentioned 30-40x" check with:
  "Keyword cluster 30-60x, blended naturally — /20". The deviation from the
  house norm is documented in the scorecard's verification notes.

## Risk handling register (normative — from content research)

Apply during drafting and the rewrite pass; each disposition lands in
score.md's verification notes:

1. DELETE the "Desi culture oversell" passage entirely (ethnic stereotype).
   Keep "metrics-based, no overselling" with zero ethnic attribution.
2. Never publish "100K USD monthly" — use "six-figure US salary" or
   "$100K+ US salary".
3. Genericize "OpenAI/Anthropic trillion-dollar" to "the largest AI labs".
4. Drop fabricated Steve Jobs quotes; keep "perception comes from using the
   product" unattributed.
5. Never state $10k/$12k/$50k as H1B salaries — reframe as a low-cost
   offshore comparison.
6. Cut the "21-day waitlist / people come begging" claim unless verified.
7. Frame "AI product does not work" as opinion, not fact.
8. Convert the $500M / 30-40% figures to the rhetorical question form with
   no numbers ("if the tool did the engineering, why not cut their own
   payroll?").
9. Cut "100x better".
10. Delete the "India/Singapore cheap companies" stereotyping.
11. Reframe "without H1B paperwork" as "without the visa sponsorship process"
    via remote engagement.

Unresolved [VERIFY] items from the dictations must be resolved (real,
re-fetched citations) or cut before the article passes the score gate.

## writing.md house style (unchanged)

- Plain title as the first line (no `#`).
- First-person; cold-open scene in a named local place; pivot to thesis.
- Evidence uses real, verified citation links (each fetched 2-3x, dispositions
  in score.md).
- Numbered compare/contrast section; clearly-personal ranked list with
  reasons; reflective close.
- NO bold/italics. NO he/him/his pronouns. Digits for all quantities. No two
  consecutive sentences starting with the same word. Brand token exactly
  `RISEUP ASIA LLC`.
- At least one question built on the target topic.
- Exactly 1-2 back-references to https://riseup-asia.com (descriptive anchor
  text, never bare URL prose).

## score.md format (adapted)

`# Scorecard — <slug> / <area>`, then Article/Target lines, then an 8-check
table (/100), a `**Total: N/100**` line, `## Verification notes` (per-URL
fetch dates + [VERIFY] dispositions + risk-register dispositions), and
`## Checks run (scripted)` (machine counts: words, cluster mentions,
consecutive same-word starts, he/him/his, topic questions, formatting, links
with HTTP status).

The 8 checks (/100): keyword cluster 30-60x /20; focus keyword early /10;
brand mentions /15; topic question /10; house structure + plain formatting
/10; citations verified /15; infographics keyword coverage /10; HTML correct
/10.

## Out of scope

- Infographic image generation (PNG/SVG) — philosophy briefs only; rendering
  is a separate rollout task.
- PDF generation for these articles.
- Publishing to Medium or to the RISEUP ASIA site.
- Any change to existing `01-seo-writing/` articles.
