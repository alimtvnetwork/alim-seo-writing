# 02 — Design System

## Palette

| Token | Value | Use |
|-------|-------|-----|
| `--paper` | `#cdbb92` | Newsprint base (warm aged beige) |
| `--paper-deep` | `#a98f63` | Vignette edges, stains |
| `--ink` | `#16130e` | All body/headline text |
| `--highlighter` | `#ffd21f` | Marker strokes behind key phrases |
| `--accent-red` | `#d63a2f` | Hand-drawn underline, urgency marks |
| `--cta-black` | `#111111` | CTA button fill |
| `--cta-arrow` | `#ffd21f` | Triangle / arrow on the CTA |

Rules: highlighter goes *behind* text, never instead of it. Red is used
exactly once per creative (the underline) — more than once and it stops
being an accent. CTA is the only pure-black solid on the page.

## Typography

- **Display (headlines, figures):** extra-bold / black weight of a
  rounded display face in the target script.
  - Bengali: Baloo Da 2 (800), Hind Siliguri (700), Noto Sans Bengali (800)
  - Latin: Fredoka (700), Archivo Black, Baloo 2 (800)
  - Arabic: Cairo (800), Tajawal (800)
  - The sample mixes scripts freely: Latin brand + Bengali sentence in
    one line. Keep that energy — don't segregate languages into zones.
- **Labels (like "স্যালারি"):** same family, 2 weights lighter, smaller.
  Their job is to set up the heavy line beneath them.
- **Numerals:** always the heaviest weight on the page. Money figures
  are the visual climax — "১ লাখ" is bigger than the role title.
- **CTA text:** bold, white on black, sentence case in the local language.

## Texture

- Base: `../../backgrounds/newsprint-texture-bg.png` (empty, no text).
- Faded multi-column newsprint, column rules visible but quiet.
- Warm vignette darkening toward all four edges — keeps the eye centred.
- Paper grain + a few stains/specks for age. No tears, no folds; the
  page reads as "old newspaper", not "damaged".
- Contrast check: `--ink` on `--paper` must stay above 7:1. If a
  generated texture comes out too dark, overlay a `--paper` wash at
  30–40% before setting type.

## Ornaments (all hand-drawn feel)

- **Highlighter strokes:** rough horizontal bands, uneven edges, slight
  rotation (1–3°), overshooting the text by ~0.5 cap-height on each side.
  Build as SVG paths or Figma vector shapes — never a clean rectangle.
- **Red underline:** one thick marker stroke under the money line,
  tapering at the ends.
- **Margin marks:** double-slashes `//` and chevrons `< >` flanking
  key lines, drawn as 6–10px strokes in `--ink`.
- **CTA button:** black fill with deliberately rough edges; yellow
  triangle/arrow pointing toward the action (down for "comment below").

## Spacing

- Generous vertical rhythm: each block separated by ~1.2x the
  preceding block's cap height. The sample breathes — nothing touches.
- Centre-aligned throughout. This is a poster, not an article.
