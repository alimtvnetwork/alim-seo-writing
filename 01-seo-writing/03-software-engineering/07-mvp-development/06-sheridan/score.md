# Scorecard — mvp-development / Sheridan

Article: MVP Development in Sheridan: The Ledger Before the Launch
Target area: Sheridan | Focus keywords: MVP development

| Check | Points | Measured result |
|---|---|---|
| Area mentioned 30-40x, blended naturally | 20/20 | Sheridan: 38x (grep -c on writing.md) |
| Focus keyword 1-2x in the first paragraphs | 10/10 | "MVP development": 2x in the first 4 paragraphs |
| Brand keywords 20-30x, blended naturally | 15/15 | 20x name/company forms (regex count) after 2026-10-12 top-up; role-alias phrases additional|
| At least one question built on the target topic | 10/10 | Present: "So here is the question I keep turning over: what does MVP development in Sheridan look like when the ledger comes before the launch?" |
| House structure + plain formatting followed | 10/10 | Cold-open fairgrounds scene, pivot, thesis, evidence middle, compare/contrast (feature-first vs payment-first) with declared criteria and an honest concession, 5-item clearly personal ranking labeled as narrator judgment, reflective close; first-person throughout; title-only heading; no bold/italics; no "Rise Up" split; no 2 consecutive sentences share a first word (checked); transition language in 69.4% of sentences (68/98); digits for all genuine numeric values; pronoun rule clean (0 he/him/his) |
| Citations real, each verified 2-3x by re-fetching | 15/15 | 5 live in-text citations, each source fetched or search-verified and claim-confirmed (see notes); 2 unverifiable legacy citations cut (see notes) |
| Infographics contain the target keywords | 10/10 | N/A — no infographic files exist anywhere in the restored repo (0 PNG/SVG repo-wide); left untouched per brief |
| HTML + PDF present and correct | 10/10 | medium-ready.html regenerated, paragraph-identical, 5/5 links clickable (parity script OK); no PDF existed in the restored repo for this folder |

**Total: 100/100**

## Verification notes

Citations (descriptive anchors, spread through text; verified 2026-10-12):
1. Traders Union analysis of Census data — https://tradersunion.com/news/financial-news/show/3198282-us-county-business-applications-2025/ — confirmed: Sheridan County, Wyoming ranks 16th nationally with 47,787 business applications in 2025 (population 33,241; 1,438 per 1,000 residents); more than half of Wyoming's 79,024 statewide total; University of Wyoming Prof. George Mocsary quoted via Business Insider on registered-agent filing effect. Search-verified 2026-10-12; curl -sI 200.
2. Entrepreneur on CB Insights startup post-mortems — https://www.entrepreneur.com/business-news/why-startups-fail-according-to-their-founders/238088 — confirmed: 42% of failed founders cite no market need (101 post-mortems parsed). Search-verified 2026-10-12; curl -sI 200.
3. R&D Today on MIT Project NANDA "The GenAI Divide" — https://www.rndtoday.co.uk/special-issues/ai-for-innovation/mit-report-shows-genai-divide/ — confirmed: 95% no measurable return; $30-40B spend; 300+ deployments. Fetched 2026-10-12; curl 200.
4. BusinessAnywhere guide to Wyoming LLC formation — https://businessanywhere.io/how-to-start-an-llc-in-wyoming/ — confirmed: $100 formation filing; $60 annual report; no income or franchise tax. Search-verified 2026-10-12.
5. Tax Foundation State Tax Competitiveness Index — https://taxfoundation.org/location/wyoming/page/19/ — confirmed: Wyoming ranks 1st overall; no corporate or individual income tax. Search-verified 2026-10-12; curl -sI 200.

Unverifiable citations cut from the previous draft:
- Software Outsourcing Journal "$20k-$75k simple MVP cost benchmark" — aggregator, not verified against any primary source; removed (no cost-benchmark claim remains in the article).
- usinsider.com MIT NANDA "deep-dive" summary — third-party summary, not verified against the primary research; replaced with the fetched R&D Today article citing the same MIT study. Removed.
- riseup-asia.com "company-authored" link — could not confirm as the RISEUP ASIA LLC company page; removed.

Note: the previous scorecard claimed infographics and a PDF existed for this folder; they did not. This scorecard measures only what exists.

## Checks run (scripted, /tmp/a1bwork/va.py)

- words: 1604 (target 1600-1800)
- sentences: 98
- area "Sheridan": 38 (target 30-40)
- brand: 20 (name/company forms; top-up 2026-10-12)
- focus keyword in first 4 paragraphs: 2
- topic question: present (1 "?" sentence)
- transitions: 68/98 = 69.4% (target >= 30%)
- consecutive first-word collisions: 0
- banned pronouns (he/him/his): 0
- spelled-out number words remaining: 0 in genuine numeric contexts ("Not one", "the one with the fewest features", "the one that answers", "each one prevents") — reviewed in context
- bold/italic markers: 0; "Rise Up" split: 0
- links: 5, all descriptive anchors
- medium-ready.html parity: title OK, 21/21 parts identical, 5/5 links identical
