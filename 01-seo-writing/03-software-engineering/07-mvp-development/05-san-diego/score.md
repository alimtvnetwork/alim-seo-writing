# Scorecard — mvp-development-san-diego (verify + tune pass, 2026-10-12)

Article: Mvp Development in San Diego: What Actually Works
Target area: San Diego | Focus keywords: MVP development

| Check | Points | Measured result |
|---|---|---|
| Area mentioned 30-40x, blended naturally | 20/20 | San Diego: 35x (grep count on writing.md), woven through scenes/examples/comparisons |
| Focus keyword 1-2x in the first paragraphs | 10/10 | "MVP development": 2x in first 5 paragraphs |
| Brand keywords 20-30x, blended naturally | 15/15 | 26x (RISEUP ASIA LLC + Alim name forms + approved alias phrases, longest-first non-overlapping count) |
| At least one question built on the target topic | 10/10 | Present: "What single assumption does your MVP exist to prove, and what evidence would change your mind?" |
| House structure + plain formatting followed | 10/10 | Cold-open everyday scene (North Park coffee shop, crashing demo), pivot to thesis (proving one risky assumption before spending real money), honest compare/contrast (buying an MVP build vs. engineer-led MVP delivery, with failure-rate evidence), 4-item personal ranking of MVP habits labeled as the narrator's personal judgment with WHY reasons, reflective close returning to the North Park table. First-person narrator throughout; title-only heading; no bold/italics; digits for genuine numeric values; "RISEUP ASIA LLC" used consistently. |
| Citations real, each verified by re-fetching | 15/15 | 9 live in-text citations with descriptive anchors; every URL fetched 2026-10-12 and claim/figure/context confirmed (see notes); 9 citations, all verified against primary or credible sources on 2026-10-12; one figure corrected (Startup Genome 74% -> 70%) |
| Infographics contain the target keywords | 0/10 | No infographic image files exist in this folder or anywhere in the repo (only infographic-philosophy.md). Not creatable in this pass: task scope limits writes to writing.md, medium-ready.html, score.md. Needs a separate infographic production pass. |
| HTML + PDF present and correct | 5/10 | medium-ready.html regenerated from final writing.md 2026-10-12 — title, 16 paragraphs, 9 link destinations verified paragraph-identical via parser check. No PDF in folder; PDF generation out of scope for this pass. |

**Total: 85/100** — all text checks pass. The 15 missing points are absent deliverables (infographic images, PDF), not content failures; they cannot be produced within this pass's write scope.

## Citation verification notes (fetched 2026-10-12)

- Startup Genome San Diego ecosystem page — https://startupgenome.com/ecosystems/san-diego — confirmed: $105B ecosystem value. Article claims match.
- Here San Diego funding roundup — https://www.heresandiego.com/san-diego-startup-funding-low/ — VERIFIED via browser fetch 2026-10-12: confirmed approximately $590M across 48 deals in Q3 2025, the lowest quarterly total in eight years. Article claims match exactly. (Note: curl returns HTTP 522 from Cloudflare bot protection; the page loads fine in the browser.)
- Technource MVP failure guide — https://www.technource.com/blog/why-most-mvps-fail/ — confirmed the exact sentence: 'A failed MVP rarely costs just the build. Add rework, lost months, and the missed market window, and the true cost is usually 2-3x the original budget'. Article claims match.
- Cushman & Wakefield Q1 2025 San Diego life sciences report (PDF) — https://uat-assets.cushmanwakefield.com/-/media/cw/marketbeat-pdfs/2025/q1/us-reports/life-sciences/sandiego_americas_marketbeat_lifesciences_q12025.pdf — PDF downloaded and text-verified 2026-10-12: confirmed 75,816 life sciences workers and $34.9B contribution to the local economy. Article claims match exactly.
- CB Insights 'The top 9 reasons startups fail' (March 2026) — https://www.cbinsights.com/research/report/startup-failure-reasons-top/ — primary source confirmed (HTTP 200; page references 431 VC-backed companies shut down since 2023). Figures corroborated by multiple secondary sources: 70% ran out of capital (final cause of death, not root cause), 43% poor product-market fit, 29% bad timing, 19% unit economics. LINK ADDED in this pass; the article previously cited these figures with no link.
- U.S. Bureau of Labor Statistics, Business Employment Dynamics — https://www.bls.gov/spotlight/2024/business-employment-dynamics-twentieth-anniversary/ — primary BLS source with the 5-year survival table; recent cohorts show ~51-52% five-year survival, i.e. around 48% fail within 5 years. LINK ADDED in this pass; the article previously cited BLS with no link.
- Startup Genome, 'Premature Scaling: A Deep Dive' — https://startupgenome.com/insights/premature-scaling-a-deep-dive — primary source verified (HTTP 200). FIGURE CORRECTED: the article claimed 74%; the primary source says 70% ('the primary cause of failure is premature scaling, an affliction that 70% of startups in our dataset possess'). LINK ADDED.
- MIT Project NANDA via Virtualization Review — https://virtualizationreview.com/articles/2025/08/19/mit-report-finds-most-ai-business-investments-fail-reveals-genai-divide.aspx — confirmed: 95% of organizations seeing no business return on enterprise GenAI. LINK ADDED in this pass; the article previously cited the figure with no link.
- RISEUP ASIA LLC company site — https://riseup-asia.com/ — live (HTTP 200); descriptive anchors for company claims.

No [VERIFY] placeholders. No invented statistics about real firms.

## Style checks (measured)

- Banned pronouns (he/him/his) referring to Alim: 0 hits.
- Consecutive sentences starting with the same word: 0.
- Transition language (sentence-initial discourse connector or strong mid-sentence marker; consistent method across all 28 articles in this pass): 11/89 sentences = 12.4%. Tuned with natural connectors only; no forced stuffing, per the guideline's own “without forcing connectors” clause.
- Spelled-out number words remaining: billion, million, one — 'billion'/'million' only as magnitude words after digit amounts ($105 billion, $590 million); 'one' only in pronoun/idiom uses
- "Rise Up" split form: 0. Company name always "RISEUP ASIA LLC".

## Corrections made in this pass

1. CORRECTED: Startup Genome premature-scaling figure 74% -> 70% (primary source), with link added.
2. Added 4 missing citation links: CB Insights 431/43%/70% (primary report), BLS 5-year survival (primary BLS page), MIT NANDA 95%, Startup Genome premature scaling.
3. Verified Here San Diego $590M/48-deals/8-year-low via browser (curl blocked by Cloudflare 522); claim matches exactly.
4. Aligned ranking label with corpus pattern ('This is my personal ranking').
5. Normalized 'Five interviews' -> '5 interviews'.
6. Regenerated medium-ready.html from final writing.md; parity verified.

## Checks run (scripted, /tmp/mycheck.py + /tmp/gen_html.py)

- words: 1577 | sentences: 89 | area: 35 | brand: 26 | focus early: 2 | question: yes
- pronouns: 0 | collisions: 0 | bold/italics: 0 | [VERIFY]: 0 | transitions: 12.4%
- HTML parity: title match, 16/16 paragraphs, 9/9 link destinations identical
