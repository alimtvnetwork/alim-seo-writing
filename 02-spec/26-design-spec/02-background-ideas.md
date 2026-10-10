# 02 — Background Ideas

Twelve buildable background concepts. Each names its source DNA, its palette,
and where it fits. All are meant to be recreated as flat assets (PNG/SVG),
not photographed.

## Dark family (from backgrounds 1 + 2)

### BG-D1 "Nebula Triangle"
Purple-black gradient (bg 1) + one oversized low-opacity triangle + star
specks. Palette: `#12081f` → `#2a1145`, specks `#ffffff` at 40–70% opacity.
Use for hero banners and launch announcements.

### BG-D2 "Grid Glow"
Near-black canvas (bg 2) + faint grid + one soft radial glow behind the
headline zone. Palette: `#0b0b10`, grid `#ffffff` at 5%, glow `#3b3bd4`
at 25%. Use for stats, pricing, and quote cards.

### BG-D3 "Deep Mesh"
Two-colour dark gradient mesh — purple from bg 1 melting into the cool
black of bg 2. No shapes, no texture. Use when type is long and the
background must disappear.

### BG-D4 "Speck Field"
Flat `#140a24` with a denser scatter of star specks than bg 1 and a
vignette pulling to black at the corners. Use for night-mode social cards.

## Light family (from magnet-board reference)

### BG-L1 "Pinstripe Paper"
Very light cool grey `#f4f6f8` with faint vertical pinstripes `#dfe4ea`
at 60% — the magnet-board look, empty. Use for tutorial headers and
listicle covers.

### BG-L2 "Candy Blobs"
Pinstripe paper + two or three large soft pastel blobs (coral, mint,
sky) at 35% opacity behind the content zone. Use for friendly
explainers and kid/family topics.

### BG-L3 "Dot Grid"
Off-white `#f7f8fa` with a regular dot grid `#c9d2dc` at 50%, dots on
24px centres. Use for worksheets, checklists, step-by-step graphics.

### BG-L4 "Tile Stage"
Flat light paper with one row of faint oversized rounded-square outlines
(ghost versions of the magnet tiles) along the bottom edge. Use for
product/feature roundups.

## Hybrid family (mixing all three)

### BG-H1 "Purple Paper"
Light lavender paper `#efe9f7` + one giant low-opacity triangle (bg 1's
shape, flipped light). Use for bridging dark-brand content into a light
article layout.

### BG-H2 "Grid Paper"
Light paper + the faint grid of bg 2 rendered in light grey `#d5dbe3`.
Technical but friendly. Use for how-to and developer-adjacent articles.

### BG-H3 "Glow Card"
Any light background + one candy-coloured soft glow spot (mint or coral)
behind the headline. Use for callout banners inside articles.

### BG-H4 "Star Paper"
Pinstripe paper + a few tiny purple star specks (bg 1's texture on a
light canvas). Use for celebratory posts — milestones, wins, launches.

## Build rules

- One hero shape per background. Never combine triangle + grid + blobs.
- Texture contrast stays under 10% against the base — text must always win.
- Keep a 120px "quiet margin" at the edges of dark backgrounds; keep light
  backgrounds fully flat so cards can float on them.
- Export at 2x; name files `bg-<family>-<name>.png` in `assets/backgrounds/`.
