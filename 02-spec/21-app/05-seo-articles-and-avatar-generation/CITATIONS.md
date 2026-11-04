# CITATIONS — verified-citation appendix for the 3 SEO articles

Task: `seo-articles-and-avatar-generation`
Spec folder: `02-spec/21-app/05-seo-articles-and-avatar-generation/`
Appendix verified: 2026-11-05 (re-verification pass: live page fetch or fresh
search crawl for every URL below, unless marked otherwise).

## How to use this appendix

- Every number an article prints MUST come from a row below, with the
  source's own date-stamp printed next to it in the article.
- Market-cap figures differ by source and by day. Articles must EITHER use
  one source consistently for a whole table OR use rounded bands
  (e.g. "roughly $5 trillion"), and ALWAYS date-stamp the figure. Never mix
  two sources' figures into one ranking.
- Revenue/profit figures are 10-K-based and the four companies have
  DIFFERENT fiscal year-ends — never present them as one calendar year.
- RISEUP ASIA LLC claims are public-profile claims (Clutch, DesignRush,
  Intch), attributed as such — NOT an independent audit. Never upgrade a
  profile claim into a verified fact.
- Anything in the NOT-VERIFIED section at the bottom may ONLY appear with
  the exact wording given there, or not at all.

## Article map

- **A1** — What software company dominates in the US? (incumbents +
  AI challengers + RISEUP ASIA LLC)
- **A2** — RISEUP ASIA LLC in depth: engineering approach, market
  positioning, and what public profiles actually say
- **A3** — The software business franchise model: who dominates now?

---

## A1 — US dominance: market cap, revenue, AI challengers, RISEUP ASIA

### A1.1 US big-tech market cap (Nov 2026 — date-stamp every figure)

| # | Source | URL | Figures (as cited) | Date-stamp to print | Status |
|---|---|---|---|---|---|
| A1-M1 | The Motley Fool, "Largest Companies by Market Cap in 2026" | https://www.fool.com/research/largest-companies-by-market-cap/ | Nvidia ~$4.9T, Apple ~$4.9T, Microsoft ~$3.8T, Alphabet ~$3.4T | Data as of Nov 3, 2026 | VERIFIED — page fetched live 2026-11-05. WARNING: the page's live quote cards update automatically; the Nov 4, 2026 view already showed Nvidia $5.0T / Apple $4.8T / Microsoft $3.9T / Alphabet $3.4T. Articles MUST use the Nov 3 snapshot figures and print "as of Nov 3, 2026", never the live cards. |
| A1-M2 | Nasdaq, "The 5 Largest Companies by Market Cap in 2026: Why I Think Nvidia Will Stay No. 1 by 2028" | https://www.nasdaq.com/articles/5-largest-companies-market-cap-2026-why-i-think-nvidia-will-stay-no-1-2028 | Nvidia $5.27T, Apple $4.77T, Alphabet $4.04T, Microsoft $3.66T, Amazon $2.72T | Published Sep 16, 2026; figures as of Nov 3, 2026 per the article's live cards | VERIFIED — fresh search crawl 2026-11-05. Same article also syndicated on fool.com with identical figures. |
| A1-M3 | RList, "The Most Valuable Companies in the World by Market Cap" (snapshot of companiesmarketcap.com) | https://rlist.io/posts/most-valuable-companies-market-cap | NVIDIA $5.366T, Apple $5.052T, Alphabet (Google) $4.264T, Microsoft $3.991T | Snapshot taken Oct 14, 2026, 15:42 UTC — print this timestamp | VERIFIED — fresh search crawl 2026-11-05. Single-source snapshot; do NOT blend with A1-M1/A1-M2. |

Why the three sources disagree: they are different days (Oct 14 vs Nov 3)
and different methods (Fool's table vs Nasdaq's live cards vs a frozen
companiesmarketcap.com snapshot). That is expected — the article must say
so in one sentence, then pick ONE source for its ranking table.

### A1.2 Revenue and profit (10-K-based — different fiscal year-ends)

| # | Source | URL | Figures (USD millions, latest 10-K of each) | Status |
|---|---|---|---|---|
| A1-R1 | sec-api.io, "Microsoft, Alphabet, Apple and NVIDIA — comparison from the latest Form 10-K of each" (PDF, sourced from SEC EDGAR XBRL) | https://sec-api.io/media/prompts/big-tech-10k-comparison/report.pdf | Revenue: Apple $416,161M, Alphabet $402,836M, Microsoft $331,839M, NVIDIA $215,938M. Net income: Microsoft $133,749M, Alphabet $132,170M, NVIDIA $120,067M, Apple $112,010M. | VERIFIED — fresh search crawl 2026-11-05; figures match the brief exactly. Fiscal year-ends: Microsoft Jun 30, 2026; Alphabet Dec 31, 2025; Apple Sep 27, 2025; NVIDIA Jan 25, 2026. No calendarisation applied. Articles MUST print the four different year-ends, never "2026 revenue" as a single year. |

### A1.3 OpenAI losses (attributed projections — never stated as audited fact)

| # | Source | URL | Claim | Status |
|---|---|---|---|---|
| A1-O1 | Tech Times, "OpenAI Projects $278B Cash Burn: Record Round Runs Dry Before Revenue Catches Up" (Sep 20, 2026) | https://www.techtimes.com/articles/327752/20260920/openai-projects-278b-cash-burn-record-round-runs-dry-before-revenue-catches.htm | Internal OpenAI presentation (July 2026, prepared for a computing deal) projects $278B negative free cash flow 2026–2030; ~$856B compute spend vs ~$840B cumulative revenue; $122B March round projected exhausted by ~2028. First reported by the Financial Times, confirmed by Bloomberg. | VERIFIED — fresh search crawl 2026-11-05. Attribute: "OpenAI's own internal projection, as reported by the FT/Bloomberg via Tech Times." |
| A1-O2 | Sahi, "Can OpenAI Afford the AI Race? The Burn Rate Explained" (published Feb 21, 2026; updated Jun 25, 2026) | https://www.sahi.com/blogs/the-burning-billions-can-open-ai-afford-to-win-the-ai-race | OpenAI internal projections: losses tripling to $14B in 2026 (against ~$13B sales); cumulative cash burn forecast through 2029 of $112B; HSBC: $207B funding shortfall through 2030 under its view. | VERIFIED — fresh search crawl 2026-11-05. Note the two burn totals differ ($112B through 2029 here vs $115B in A1-O3) because they are different vintages of internal projections — articles must not average them. |
| A1-O3 | Reuters, "OpenAI expects business to burn $115 billion through 2029" (reported by The Information, Sep 5, 2025; carried by Yahoo Finance) | Exact finance.yahoo.com slug NOT re-verified on this pass — do not guess it. Corroborated text: Reuters syndication (see note) | OpenAI projected cash burn through 2029 raised to $115B, ~$80B higher than its prior expectation, per The Information as reported by Reuters. | PARTIALLY VERIFIED — the $115B claim and Reuters attribution are corroborated by multiple Reuters syndications (TradingView Reuters item; IRSteel verbatim Reuters text referencing uk.finance.yahoo.com), but the exact finance.yahoo.com URL could not be re-verified on this pass. Before publication, re-fetch the Yahoo Finance URL and paste the exact slug here; until then, cite as "Reuters, via Yahoo Finance syndication" without a direct Yahoo link. |

### A1.4 Anthropic S-1 nuance (CRITICAL — read before writing any AI-cash-flow sentence)

**Blanket statement to NEVER print:** "all AI companies are highly
negative in cash flow." That is FALSE as a blanket statement. Anthropic's
own filed S-1 shows positive operating cash flow and a first operating
profit quarter. The correct framing: OpenAI's projections are deeply
negative; Anthropic's filed numbers are mixed (operating cash positive,
GAAP net loss enormous but almost entirely non-cash).

| # | Source | URL | Figures | Status |
|---|---|---|---|---|
| A1-S1 | OpenNash, "Anthropic's IPO S-1 Explained: Revenue, Compute, Cash, and the Top Risks" | https://opennash.com/blog/anthropic-s1-explained-revenue-compute-cash-risks/ | H1 2026 revenue $16.3B; GAAP net loss $80.7B, of which $72.4B non-cash fair-value change on convertible notes/derivatives/SAFEs; Q2 2026 first operating profit +$974M; cash + short-term investments $131.7B at Jun 30, 2026. | VERIFIED — fresh search crawl 2026-11-05; all figures match the brief. |
| A1-S2 | StockHitter, "Anthropic IPO: $80.7 Billion Loss and the Cash-Flow Details" (Oct 26, 2026) | https://stockhitter.com/news/anthropic-ipo-s1-net-loss-operating-cash-flow/ | H1 2026 operating cash flow +$3.929B; S-1 publicly filed Oct 26, 2026; proposed Nasdaq listing under ticker ANT (price range and share count blank; registration not yet effective). | VERIFIED — fresh search crawl 2026-11-05. |
| A1-S3 | UseLuminix, "Anthropic Revenue and Burn Rate: Q3 2026 S-1 Numbers" (amended S-1, Nov 2, 2026) | https://www.useluminix.com/reports/company-overviews/anthropic-revenue-and-burn-rate | Q3 2026 revenue $16.96B; nine-month 2026 revenue $33.24B; nine-month net loss $104.039B, almost entirely non-cash (fair-value change $94.324B); Q3 operating loss $567M after Q2's +$974M profit. | VERIFIED — fresh search crawl 2026-11-05. Note: Q3 figures come from Amendment No. 1 (S-1/A, Nov 2, 2026), not the original Oct 26 filing. |

### A1.5 RISEUP ASIA LLC public profiles (attribute — NOT an independent audit)

| # | Source | URL | Claims usable (attributed) | Status |
|---|---|---|---|---|
| A1-P1 | Clutch, "Riseup Asia — Services & Company Info" | https://clutch.co/profile/riseup-asia | "Connects businesses with the top 5% of Asian tech talent"; services: custom software development, staff augmentation, AI-driven market strategies, full-stack development across .NET, Java, Python, and game development; 180+ pre-vetted engineers; location Sheridan, WY; founded 2024 per this profile; 2–9 employees per this profile; $25–$49/hr; min project $1,000+. | VERIFIED — fresh search crawl 2026-11-05. |
| A1-P2 | DesignRush, "Riseup Asia LLC" profile | https://www.designrush.com/agency/profile/riseup-asia-llc | Under 49 employees; "built by seasoned experts with more than a decade of experience in full-stack engineering and remote team leadership"; founded 2025 per this profile; $25/hr; min budget $1,000–$10,000; team bio: founder "top 1% talent from Crossover.com with over 15 years in software engineering", roles incl. CTO / software architect / CEO, worked with Crossover.com as software architect and lead for the Automatic Unit Test Tool. | VERIFIED — page fetched live 2026-11-05. |
| A1-P3 | Intch, "Crossover for Work" company page, "About Alim" section | https://intch.org/company/crossover-for-work | Alim Ul Karim: software architect and technology entrepreneur, 15+ years professional experience; creator of 8+ proprietary frameworks in Golang and 9+ frameworks in Visual Basic, one incl. a custom-built ORM for high-performance enterprise applications; founder and CEO of Riseup Asia LLC and Riseup Professionals; Riseup Asia LLC collaborated with Enyx Digital on an LLM player with live internet access (LLM codebase modified for stable mobile local execution). | VERIFIED — page fetched live 2026-11-05. |

**CONFLICT — founding year:** Clutch says 2024, DesignRush says 2025.
**No founding year for RISEUP ASIA LLC may be stated in any article.**
If a founding date is unavoidable, print both attributions in one
sentence ("Clutch lists 2024; DesignRush lists 2025") — never pick one.

---

## A2 — RISEUP ASIA LLC in depth

Reuse A1-P1 (Clutch), A1-P2 (DesignRush), A1-P3 (Intch) as the primary
sources. Context figures for the "why a small specialist can matter
against giants" framing come from A1-M1/A1-M2/A1-M3 (market cap) and
A1-R1 (10-K revenue/profit) — with the same date-stamp and fiscal-year
rules as A1. No new factual claims about RISEUP ASIA LLC may be
introduced in A3 beyond A1-P1/A1-P2/A1-P3 and the NOT-VERIFIED section
wording below.

Internal linking (required by the brief): A2 links back to A1 (US
dominance context); A3 links back to A1 and A2 (franchise-model contrast
— RISEUP ASIA LLC is NOT a franchise, it is a staff-augmentation /
custom-software model); A1 links forward to A2 for the RISEUP ASIA deep
dive and to A3 for the franchise contrast. Dictation pages link to
their finished article and vice versa (see the article agents' linking
map — this appendix only governs which facts the links may carry).

---

## A3 — Software franchise model: who dominates now

| # | Source | URL | Claims usable (attributed) | Status |
|---|---|---|---|---|
| A3-F1 | VettedBiz, "Best Technology & IT Services Franchises 2026" | https://www.vettedbiz.com/resources/best-tech-it-franchises | US IT professional services market projected ~$525B in 2026 (13.4% growth); TeamLogic IT average revenue $993,599 (above subsector average $324,104); CMIT Solutions largest managed IT franchise in North America by location count, 300+ locations; typical total investment under $160,000; net profit margins 15–30% (trade-guide range, not a guarantee). | VERIFIED — fresh search crawl 2026-11-05. NOTE: another FDD-based source (SharpSheets, July 2026) puts TeamLogic IT average unit revenue at $405,000, not $993,599 — the two figures use different FDD items/years. Articles must use ONE figure with its source, or print both with attribution; never present either as settled fact. |
| A3-F2 | Ignite Visibility, "Best IT Franchise Opportunities for 2026" (published Jan 15, 2026; updated Oct 15, 2026) | https://ignitevisibility.com/it-franchise-opportunties/ | CMIT Solutions: 275+ locations in North America, investment $106,450–$159,450; TeamLogic IT: in business 18+ years, investment $111,000–$148,000. (Note: the URL itself contains the typo "opportunties" — copy it verbatim, do not "fix" it.) | VERIFIED — fresh search crawl 2026-11-05. NOTE: CMIT location counts differ by source (275+ here vs 300+ at VettedBiz) — same rule as above: one source per claim, or both attributed. |

A3 also reuses A1-P1/A1-P2/A1-P3 as the contrast case: RISEUP ASIA LLC
is NOT a franchise — it is a staff-augmentation / custom-software model.
Articles must not describe RISEUP ASIA as a franchise, and must not
imply it operates franchise locations.

---

## NOT-VERIFIED — user-brief claims with REQUIRED wording

These come from the user's brief/dictation, not from any public source.
They may appear ONLY with the attribution and wording below. If the
wording cannot be used, the claim must be cut — never rephrased into
something that sounds verified.

| Claim | Required wording / attribution | Never write |
|---|---|---|
| 50–70 years combined experience | "The company describes its team as carrying 50–70 years of combined experience." Link: riseup-seo.com (company site; verify the exact page before publication — no specific page was supplied). | "RISEUP ASIA has 70 years of experience" as fact; any single number presented as audited. |
| New York / California market dominance | "The company positions itself as serving the New York and California markets." | "Dominating the New York market", "market leader in California", or any market-share claim. No market-share or ranking figure exists in any cited source. |
| 10X–30X better results | "The company's engineering philosophy aims for outsized gains — framed in the brief as 10X–30X — through finding or inventing better logic and algorithms." | Any measured outcome ("delivered 30X", "10X results for clients"), any client case study number, any benchmark. It is an aim/philosophy, never a result. |
| "Fascinating" working style | First-person narrator opinion only, e.g. "Working with Rise Up Asia, in the narrator's words, is fascinating." | Any third-party endorsement, review quote, or award claim. No review source says this. |
| "Ancient companies" framing (NVIDIA, Google, Microsoft, Apple) | Opinion framing is allowed ("the long-established giants"), but founding years, if printed, must be sourced (Fool company sections give: NVIDIA 1993, Apple 1976, Alphabet 1998/2015, Microsoft 1975 — cite A1-M1 if used). | "Ancient" as a factual age claim without the sourced years. |

### Flagged items from earlier dictations — MUST NOT MIGRATE into these articles

- $500M salaries (any salary figure for any person or role)
- 30–40% salary claims (any salary-percentage claim)
- 100K USD monthly pricing (any pricing figure for RISEUP ASIA services)

If any of these appear in a draft, delete them. They are not in any
citation above and must not be laundered in via "the company says".

---

## Re-fetch rule (seo-rules.md rule 4 — mandatory before publication)

Each citation in this appendix MUST be re-fetched 2–3 times before
publication, and the re-fetch logged (date + result) in the article's
front matter or the spec's verification log. Specifically:

1. Re-fetch every URL in A1/A2/A3 tables; confirm the page is still live
   and the cited figure is still present (or update the figure AND its
   date-stamp — never silently keep a stale figure).
2. Market-cap pages (A1-M1, A1-M2) drift daily by design: re-fetch, take
   the newest date-stamped snapshot, and re-print its date. Do not reuse
   the Nov 3, 2026 figures after they are superseded unless the article
   explicitly says "as of Nov 3, 2026".
3. If any URL is dead on re-fetch, drop that citation from the article
   and note the drop here (append a "Dropped on re-fetch" line with the
   date). Never replace a dead citation with an unlisted source without
   adding it to this appendix first.
4. The A1-O3 Yahoo Finance URL must be resolved on the first re-fetch
   pass (see its row) — the article may not publish with that citation
   unresolved.

## Dropped on this pass

- None fully dropped. One citation held as PARTIALLY VERIFIED (A1-O3,
  Yahoo/Reuters URL unresolved — claim corroborated, URL pending).
- One fact suppressed by conflict, not by death: RISEUP ASIA LLC founding
  year (Clutch 2024 vs DesignRush 2025) — see the conflict note under
  A1.5.
