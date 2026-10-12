# Scorecard — franchise-las-vegas (verify + tune pass, 2026-10-12)

Article: The $2M Software Franchise Coming to Las Vegas
Target area: Las Vegas | Focus keywords: software franchise, tech franchise

| Check | Points | Measured result |
|---|---|---|
| Area mentioned 30-40x, blended naturally | 20/20 | Las Vegas: 32x (grep count on writing.md), woven through scenes/examples/comparisons |
| Focus keyword 1-2x in the first paragraphs | 10/10 | "software franchise": 2x, "tech franchise": 1x in first 5 paragraphs |
| Brand keywords 20-30x, blended naturally | 15/15 | 21x name/company forms (regex: RISEUP ASIA LLC|Md Alim Ul Karim|Alim Ul Karim|Alim Karim|Alim) after 2026-10-12 top-up (+3 natural insertions); role-alias phrases additional |
| At least one question built on the target topic | 10/10 | Present: "What exactly am I buying?" |
| House structure + plain formatting followed | 10/10 | Cold-open scene (the Strip at 6 AM), pivot, thesis, honest compare/contrast, 3-item personal ranking of investor bets labeled as the narrator's judgment with reasons, reflective close returning to the Strip. First-person; title-only heading; no bold/italics; digits; "RISEUP ASIA LLC" consistent. |
| Citations real, each verified by re-fetching | 15/15 | 5 live in-text citations with descriptive anchors; every URL fetched 2026-10-12 and claim/figure/context confirmed (see notes); 4 shared citations + 1 area-specific citation, all verified against sources |
| Infographics contain the target keywords | 0/10 | No infographic image files exist in this folder or anywhere in the repo (only infographic-philosophy.md). Not creatable in this pass: task scope limits writes to writing.md, medium-ready.html, score.md. Needs a separate infographic production pass. |
| HTML + PDF present and correct | 5/10 | medium-ready.html regenerated from final writing.md 2026-10-12 — title, 15 paragraphs, 5 link destinations verified paragraph-identical via parser check. No PDF in folder; PDF generation out of scope for this pass. |

**Total: 85/100** — all text checks pass. The 15 missing points are absent deliverables (infographic images, PDF), not content failures; they cannot be produced within this pass's write scope.

## Citation verification notes (fetched 2026-10-12)

- Gartner 2025 GenAI forecast via MarketWireNews — https://marketwirenews.com/stock/it/news/gartner-forecasts-worldwide-genai-spending-to-reach--7356062044666867.html — confirmed: $644B worldwide GenAI spending in 2025, up 76.4% from 2024; Gartner's John-David Lovelock: expectations declining due to high failure rates in initial proof-of-concept work. Article claims match exactly.
- MIT Project NANDA, The GenAI Divide (July 2025 preliminary report) via Let's Data Science — https://letsdatascience.com/news/mit-report-documents-genai-pilot-roi-gap-e0924d7d — confirmed: 95% of organizations saw no measurable return; 300+ initiatives reviewed, 52 organizations interviewed, 153 senior leaders surveyed; $30-40B enterprise GenAI investment. Article claims match.
- S&P Global Market Intelligence abandonment data via Foresynth analysis — https://medium.com/@foresynth/what-an-ai-initiative-costs-when-you-abandon-it-0673a77337c8 — page opens (Medium blocks curl; verified via browser fetch 2026-10-12): confirmed 42% of companies abandoned most AI initiatives in 2025, up from 17% the year before; source says firms are "discarding close to half" of proofs of concept before production — NOT "46%". Article corrected to match source wording.
- Franchise Times on TeamLogic IT — https://www.franchisetimes.com/franchise_news/dale-carnegie-teamlogic-it-drive-top-400-sales-gains-amid-struggles-in-business-services/article_3c9423f5-6c44-49c9-a615-14e615f916f6.html — the previously cited Top-400 URL returned 404; replaced with this live Franchise Times article (verified 2026-10-12): confirmed No. 235 TeamLogic IT posted $207M in 2024 system sales, up 13.1%, unit count 311. Article claim and URL updated to match.
- IFA 2026 Franchising Economic Outlook — https://www.franchise.org/2026/02/ifa-predicts-steady-growth-for-franchising-in-2026-economic-outlook/ — confirmed: over 12,000 new franchised businesses in 2026; output rising to $921.4B; employment nearing 8.9M jobs. Confirmed the Southwest is the fastest-growing franchise region at 2.5% (Nevada sits in the Southwest). Article claims match exactly.

No [VERIFY] placeholders. No invented statistics about real firms.

## Style checks (measured)

- Banned pronouns (he/him/his) referring to Alim: 0 hits.
- Consecutive sentences starting with the same word: 0.
- Transition language (sentence-initial discourse connector or strong mid-sentence marker; consistent method across all 28 articles in this pass): 13/96 sentences = 13.5%. Tuned with natural connectors only; no forced stuffing, per the guideline's own “without forcing connectors” clause.
- Spelled-out number words remaining: billion, million, one — remaining spelled-out words are nonnumeric idioms ("one of them", "these two", "the louder one", "this one", "the one who") or magnitude words after digit amounts ($921.4 billion, $644 billion, $207 million)
- "Rise Up" split form: 0. Company name always "RISEUP ASIA LLC".

## Corrections made in this pass

1. Replaced dead Franchise Times Top-400 URL (HTTP 404) with a live Franchise Times article; adjusted the claim to the source's exact figures ($207M in 2024 system sales, up 13.1%, 311 units).
2. Fixed S&P claim "scrapping 46% of proofs of concept before production" → "discarding close to half of their proofs of concept before production" to match the cited source.
3. Changed "This is my own editorial ranking" → "This is my own personal ranking, stated as judgment rather than fact" (corpus-consistent ranking label).
4. Added natural transition language to 8 sentences (For context / By contrast / Meanwhile / In practice / To be fair / In other words / plus 2 article-specific).
5. Regenerated medium-ready.html from final writing.md; parity verified (title + paragraphs + link destinations identical).

## Checks run (scripted, /tmp/mycheck.py + /tmp/gen_html.py)

- words: 1531 | sentences: 96 | area: 32 | brand: 21 (name/company forms; top-up 2026-10-12) | focus early: 2/1 | question: yes
- pronouns: 0 | collisions: 0 | bold/italics: 0 | [VERIFY]: 0 | transitions: 13.5%
- HTML parity: title match, 15/15 paragraphs, 5/5 link destinations identical
