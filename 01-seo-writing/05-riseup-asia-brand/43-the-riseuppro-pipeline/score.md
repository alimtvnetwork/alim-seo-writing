# Scorecard — riseuppro-pipeline (verify + tune pass, 2026-10-12)

Article: The RiseupPro Pipeline
Target area: San Diego | Focus keywords: RiseupPro, bootcamp pipeline

| Check | Points | Measured result |
|---|---|---|
| Area mentioned 30-40x, blended naturally | 20/20 | San Diego: 36x (grep count on writing.md), woven through scenes/examples/comparisons |
| Focus keyword 1-2x in the first paragraphs | 10/10 | "RiseupPro": 4x, "bootcamp pipeline": 1x in first 5 paragraphs |
| Brand keywords 20-30x, blended naturally | 15/15 | 27x (RISEUP ASIA LLC + Alim name forms + approved alias phrases, longest-first non-overlapping count) |
| At least one question built on the target topic | 10/10 | Present: "How does a San Diego company turn a bootcamp graduate into a production engineer it can trust with real customers?" |
| House structure + plain formatting followed | 10/10 | Cold-open everyday scene (Tourmaline Surf Park surf drill), pivot to thesis (junior-developer pipeline), honest compare/contrast (AI gold rush vs. staged progression; hallucination and rework risks conceded), 4-item personal ranking labeled as the narrator's judgment with a reason per item, reflective close returning to the beach. First-person narrator throughout; title-only heading; no bold/italics; digits for genuine numeric values; "RISEUP ASIA LLC" used consistently. |
| Citations real, each verified by re-fetching | 15/15 | 4 live in-text citations with descriptive anchors; every URL fetched 2026-10-12 and claim/figure/context confirmed (see notes); 4 citations verified against primary or credible secondary sources |
| Infographics contain the target keywords | 0/10 | No infographic image files exist in this folder or anywhere in the repo (only infographic-philosophy.md). Not creatable in this pass: task scope limits writes to writing.md, medium-ready.html, score.md. Needs a separate infographic production pass. |
| HTML + PDF present and correct | 5/10 | medium-ready.html regenerated from final writing.md 2026-10-12 — title, 14 paragraphs, 4 link destinations verified paragraph-identical via parser check. No PDF in folder; PDF generation out of scope for this pass. |

**Total: 85/100** — all text checks pass. The 15 missing points are absent deliverables (infographic images, PDF), not content failures; they cannot be produced within this pass's write scope.

## Citation verification notes (fetched 2026-10-12)

- Gartner September 2026 AI spending forecast — https://www.gartner.com/en/newsroom/press-releases/2026-09-16-gartner-forecasts-worldwide-ai-spending-to-grow-49-point-5-percent-in-2026 — confirmed: worldwide AI spending forecast at $2.7 trillion in 2026, up 49.5% year-over-year. Article claims match exactly.
- MIT Project NANDA, The GenAI Divide (July 2025 preliminary report) via Let's Data Science — https://letsdatascience.com/news/mit-report-documents-genai-pilot-roi-gap-e0924d7d — confirmed: 95% of organizations saw no measurable return; 300+ initiatives, 52 organizations, 153 senior leaders; $30-40B enterprise GenAI investment. Article claims match.
- SHRM 2025 benchmarking via Pin summary — https://www.pin.com/blog/cost-per-hire-benchmarks/ — confirmed: average non-executive cost per hire $5,475 per SHRM's 2025 Benchmarking Report. Article claims match.
- 2025 Stack Overflow Developer Survey (Work section) — https://survey.stackoverflow.co/2025/work — confirmed: autonomy/trust ranked the top job-satisfaction factor (Overall Rank 1) and 46% of developers are not looking for a new role. Article claims match.

No [VERIFY] placeholders. No invented statistics about real firms.

## Style checks (measured)

- Banned pronouns (he/him/his) referring to Alim: 0 hits.
- Consecutive sentences starting with the same word: 0.
- Transition language (sentence-initial discourse connector or strong mid-sentence marker; consistent method across all 28 articles in this pass): 29/110 sentences = 26.4%. Tuned with natural connectors only; no forced stuffing, per the guideline's own “without forcing connectors” clause.
- Spelled-out number words remaining: one, trillion — 'trillion' appears only as a magnitude word after a digit amount ($2.7 trillion); 'one' appears only in nonnumeric idioms ("the first real one")
- "Rise Up" split form: 0. Company name always "RISEUP ASIA LLC".

## Corrections made in this pass

1. No citation replacements needed — all 4 URLs live (HTTP 200) and every cited figure confirmed against the source on 2026-10-12.
2. Added natural transition language to 5 sentences (Specifically / In practice / The data backs this up / Predictably / By contrast).
3. Expanded the economics section with concrete San Diego cost math ($5,475 replacement + senior review time vs. pipeline graduate) and sharpened the AI-gold-rush contrast with one substantive sentence.
4. Fixed a consecutive same-word sentence start introduced by the expansion ("A bad junior hire..." / "A RiseupPro graduate..." → "By contrast, a RiseupPro graduate...").
5. Regenerated medium-ready.html from final writing.md; parity verified (title + paragraphs + link destinations identical).

## Checks run (scripted, /tmp/mycheck.py + /tmp/gen_html.py)

- words: 1510 | sentences: 110 | area: 36 | brand: 27 | focus early: 4/1 | question: yes
- pronouns: 0 | collisions: 0 | bold/italics: 0 | [VERIFY]: 0 | transitions: 26.4%
- HTML parity: title match, 14/14 paragraphs, 4/4 link destinations identical
