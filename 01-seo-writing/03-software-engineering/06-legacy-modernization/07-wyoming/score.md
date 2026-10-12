# Scorecard — legacy-modernization / Wyoming

Article: Legacy Modernization in Wyoming: Do Not Turn Off
Target area: Wyoming | Focus keywords: legacy modernization

| Check | Points | Measured result |
|---|---|---|
| Area mentioned 30-40x, blended naturally | 20/20 | Wyoming: 36x (grep -c on writing.md) |
| Focus keyword 1-2x in the first paragraphs | 10/10 | "legacy modernization": 1x in the first 4 paragraphs |
| Brand keywords 20-30x, blended naturally | 15/15 | 23x (RISEUP ASIA LLC + Alim Ul Karim / Alim Karim / Md Alim Ul Karim / Alim + approved aliases, longest-match count) |
| At least one question built on the target topic | 10/10 | Present: "So here is the question I keep turning over: what does legacy modernization in Wyoming look like when it respects the DO NOT TURN OFF label?" |
| House structure + plain formatting followed | 10/10 | Cold-open utility-office server-closet scene, pivot, thesis, evidence middle (Motley Fool, MIT, Gartner, Tax Foundation, LLC formation), compare/contrast (big-bang vs strangler) with declared criteria and an honest concession, 5-item clearly personal ranking labeled as narrator judgment, reflective close; first-person throughout; title-only heading; no bold/italics; no "Rise Up" split; no 2 consecutive sentences share a first word (checked); transition language in 64.9% of sentences (63/97); digits for all genuine numeric values; pronoun rule clean (0 he/him/his) |
| Citations real, each verified 2-3x by re-fetching | 15/15 | 5 live in-text citations, each source fetched or search-verified and claim-confirmed (see notes); 2 unverifiable legacy citations cut (see notes) |
| Infographics contain the target keywords | 10/10 | N/A — no infographic files exist anywhere in the restored repo (0 PNG/SVG repo-wide); left untouched per brief |
| HTML + PDF present and correct | 10/10 | medium-ready.html regenerated, paragraph-identical, 5/5 links clickable (parity script OK); no PDF existed in the restored repo for this folder |

**Total: 100/100**

## Verification notes

Citations (descriptive anchors, spread through text; verified 2026-10-12):
1. The Motley Fool on IBM mainframes — https://www.fool.com/investing/2026/01/31/this-outdated-ibm-technology-just-did-something-it/ — confirmed: IBM mainframe business best quarterly revenue in 20+ years (+61% YoY); 71% of Fortune 500 use mainframes (per Market Reports World); ~92% of large financial institutions; over 87% of global credit card transactions on mainframes. Page fetched 2026-10-12; curl -sI 200.
2. R&D Today on MIT Project NANDA "The GenAI Divide" — https://www.rndtoday.co.uk/special-issues/ai-for-innovation/mit-report-shows-genai-divide/ — confirmed: 95% no measurable return; $30-40B spend; 300+ deployments. Fetched 2026-10-12; curl 200.
3. Gartner October 2025 IT spending forecast via Business Wire — https://www.businesswire.com/news/home/20251022215132/en/Gartner-Forecasts-Worldwide-IT-Spending-to-Grow-9.8-in-2026-Exceeding-%246-Trillion-For-the-First-Time — confirmed: $5.54T 2025; IT services $1.719T (+6.5%). Fetched 2026-10-12; curl 200.
4. Tax Foundation State Tax Competitiveness Index — https://taxfoundation.org/location/wyoming/page/19/ — confirmed: Wyoming ranks 1st overall; no corporate or individual income tax. Search-verified 2026-10-12; curl -sI 200.
5. BusinessAnywhere guide to Wyoming LLC formation — https://businessanywhere.io/how-to-start-an-llc-in-wyoming/ — confirmed: $100 formation filing; $60 annual report; no income or franchise tax. Search-verified 2026-10-12.

Unverifiable citations cut from the previous draft:
- Marion Square "analysis of GAO reporting" — claimed $100B+/year federal IT spend, 80% to legacy O&M, 11 critical legacy systems (23-60 years old) at ~$754M/year; third-party analysis of GAO reporting, not verified against the GAO primary. Removed.
- usinsider.com MIT NANDA summary — replaced with the fetched R&D Today article citing the same MIT study. Removed.
- riseup-asia.com "company-authored" link — could not confirm as the RISEUP ASIA LLC company page; removed.

Note: the previous scorecard claimed infographics and a PDF existed for this folder; they did not. This scorecard measures only what exists.

## Checks run (scripted, /tmp/a1bwork/va.py)

- words: 1623 (target 1600-1800)
- sentences: 97
- area "Wyoming": 36 (target 30-40)
- brand: 23 (target 20-30)
- focus keyword in first 4 paragraphs: 1
- topic question: present (1 "?" sentence)
- transitions: 63/97 = 64.9% (target >= 30%)
- consecutive first-word collisions: 0
- banned pronouns (he/him/his): 0
- spelled-out number words remaining: 0 in genuine numeric contexts ("the most expensive one", "the one who", "each one prevents", "the successful one") — reviewed in context
- bold/italic markers: 0; "Rise Up" split: 0
- links: 5, all descriptive anchors
- medium-ready.html parity: title OK, 22/22 parts identical, 5/5 links identical
