#!/usr/bin/env python3
"""seo-infographic.py - v4 infographic renderer.

Renders data JSON cards as infographic-<n>.png (PIL, 1200x630 social-og-card)
AND infographic-<n>.svg (hand-written SVG twin) into an article dir.

Run: gitmap py 03-ai-scripts/seo-infographic.py --data <json> [--dir <article-dir>]

Layouts: stat-label-top, model-cards, compare-2col, ranking-list, bars.
Design rules: 02-spec/07-design-system/45-ai-visual-whitespace-discipline.md
(non-negotiable). Fonts: Ubuntu 700 headings/numerals, Poppins body.
"""
import argparse
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 630
REPO = Path.home() / "workspace" / "repos" / "alim-seo-writing"
FONT_DIR = Path.home() / ".fonts"
FONT_FILES = {
    ("Ubuntu", 700): FONT_DIR / "Ubuntu-Bold.ttf",
    ("Poppins", 400): FONT_DIR / "Poppins-Regular.ttf",
    ("Poppins", 600): FONT_DIR / "Poppins-SemiBold.ttf",
}

THEMES = {
    "warm-editorial": {
        "base": "#0B0A09", "surface": "#1D1A18",
        "accent": "#FFAD01", "accent2": "#FFAD01",
        "fg": "#F7F5F2", "muted": "#ADA8A2", "dim": "#6E6963",
        "hair": (247, 245, 242, 28), "glow": (255, 173, 1),
    },
    "navy-purple": {
        "base": "#0A0F1D", "surface": "#172036",
        "accent": "#A855F7", "accent2": "#38BDF8",
        "fg": "#F8FAFC", "muted": "#94A3B8", "dim": "#5B6B85",
        "hair": (248, 250, 252, 30), "glow": (168, 85, 247),
    },
}

_font_cache = {}


def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def font(fam, weight, size):
    key = (fam, weight, size)
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(str(FONT_FILES[(fam, weight)]), size)
    return _font_cache[key]


def strip(s):
    return s.strip()


class Ctx:
    """Layout context: collects primitives + bounding boxes for one card."""

    def __init__(self, theme_name):
        self.t = THEMES[theme_name]
        self.theme_name = theme_name
        self.prims = []          # render primitives (backend-agnostic)
        self.boxes = []         # (name, x0, y0, x1, y1, container_id|None)
        self.containers = {}    # cid -> (x0, y0, x1, y1)
        self.zones = 0
        self._cid = 0
        self._scratch = ImageDraw.Draw(Image.new("RGB", (8, 8)))

    # ---- measurement ----
    def text_w(self, s, fam, weight, size):
        f = font(fam, weight, size)
        bb = self._scratch.textbbox((0, 0), s, font=f)
        return bb[2] - bb[0]

    def text_h(self, fam, weight, size):
        f = font(fam, weight, size)
        bb = f.getbbox("Ag")
        return bb[3] - bb[1]

    def tracked_w(self, s, fam, weight, size, tracking):
        f = font(fam, weight, size)
        ws = [self._scratch.textbbox((0, 0), ch, font=f)[2] for ch in s]
        return sum(ws) + tracking * max(0, len(s) - 1)

    def wrap(self, s, fam, weight, size, max_w, max_lines=2):
        words, lines, cur = s.split(), [], ""
        for wd in words:
            trial = (cur + " " + wd).strip()
            if self.text_w(trial, fam, weight, size) <= max_w or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = wd
                if len(lines) == max_lines - 1:
                    break
        if cur:
            lines.append(cur)
        return lines[:max_lines]

    # ---- primitives ----
    def glow(self, cx, cy, r, alpha):
        self.prims.append({"t": "glow", "cx": cx, "cy": cy, "r": r,
                            "color": self.t["glow"], "alpha": alpha})

    def rect(self, x, y, w, h, rx, fill, stroke=None, stroke_w=0,
             stroke_alpha=255, name="rect", container=None):
        self.prims.append({"t": "rect", "x": x, "y": y, "w": w, "h": h,
                           "rx": rx, "fill": fill, "stroke": stroke,
                           "stroke_w": stroke_w, "stroke_alpha": stroke_alpha})
        self.boxes.append((name, x, y, x + w, y + h, container, "shape"))

    def new_container(self, name, x, y, w, h):
        self._cid += 1
        cid = f"c{self._cid}"
        self.containers[cid] = (x, y, x + w, y + h)
        self.boxes.append((name, x, y, x + w, y + h, None, "shape"))
        self._container_ids = getattr(self, "_container_ids", {})
        self._container_ids[name] = cid
        return cid

    def text(self, x, y, s, fam, weight, size, fill, anchor="ma",
             tracking=0, name="text", container=None):
        """anchor: ma (middle-top), la, ra, mm (middle-middle)."""
        f = font(fam, weight, size)
        if tracking:
            total = self.tracked_w(s, fam, weight, size, tracking)
            hgt = self.text_h(fam, weight, size)
            if anchor == "ma":
                x0 = x - total / 2
            elif anchor == "la":
                x0 = x
            elif anchor == "ra":
                x0 = x - total
            else:
                raise ValueError(f"bad anchor {anchor}")
            self.prims.append({"t": "tracked", "x": x0, "y": y, "s": s,
                               "fam": fam, "weight": weight, "size": size,
                               "fill": fill, "tracking": tracking,
                               "ax": x0, "svg_anchor": "start",
                               "baseline": y + f.getmetrics()[0]})
            self.boxes.append((name, x0, y, x0 + total, y + hgt, container, "text"))
            return (x0, y, x0 + total, y + hgt)
        bb = self._scratch.textbbox((0, 0), s, font=f)
        tw, th = bb[2] - bb[0], bb[3] - bb[1]
        if anchor == "ma":
            x0, y0 = x - tw / 2, y
        elif anchor == "la":
            x0, y0 = x, y
        elif anchor == "ra":
            x0, y0 = x - tw, y
        elif anchor == "mm":
            x0, y0 = x - tw / 2, y - th / 2
        else:
            raise ValueError(f"bad anchor {anchor}")
        # nudge by bbox origin so box matches drawn glyphs
        x0 -= bb[0]
        y0 -= bb[1]
        self.prims.append({"t": "text", "x": x0, "y": y0, "s": s,
                           "fam": fam, "weight": weight, "size": size,
                           "fill": fill, "anchor": "la",
                           "ax": x,
                           "svg_anchor": {"ma": "middle", "la": "start",
                                          "ra": "end", "mm": "middle"}[anchor],
                           "baseline": y0 + f.getmetrics()[0]})
        self.boxes.append((name, x0, y0, x0 + tw, y0 + th, container, "text"))
        return (x0, y0, x0 + tw, y0 + th)

    def zone(self):
        self.zones += 1

    # ---- self-check ----
    def check(self):
        errs = []
        if self.zones > 5:
            errs.append(f"text-zone budget exceeded: {self.zones} > 5")
        # perimeter safe zone 55px; text keeps 80px side margins.
        # The single tiny footer attribution line may sit low (approved v4).
        for name, x0, y0, x1, y1, _, kind in self.boxes:
            if kind == "text":
                if name == "footer":
                    lim = (80, 55, W - 80, H - 6)
                else:
                    lim = (80, 55, W - 80, H - 55)
            else:
                lim = (55, 55, W - 55, H - 55)
            if x0 < lim[0] or y0 < lim[1] or x1 > lim[2] or y1 > lim[3]:
                errs.append(f"{name} breaches safe zone {lim}: "
                            f"({x0:.0f},{y0:.0f},{x1:.0f},{y1:.0f})")
        # pairwise overlap (containment inside own container is fine)
        n = len(self.boxes)
        for i in range(n):
            for j in range(i + 1, n):
                ni, a, ci = self.boxes[i][0], self.boxes[i][1:5], self.boxes[i][5]
                nj, b, cj = self.boxes[j][0], self.boxes[j][1:5], self.boxes[j][5]
                # shrink by 3px tolerance
                ax0, ay0, ax1, ay1 = a[0] + 3, a[1] + 3, a[2] - 3, a[3] - 3
                bx0, by0, bx1, by1 = b[0] + 3, b[1] + 3, b[2] - 3, b[3] - 3
                inter = not (ax1 <= bx0 or bx1 <= ax0 or ay1 <= by0 or by1 <= ay0)
                if not inter:
                    continue
                # containment: inner registered to outer container
                a_in_b = (cj is not None and self._contains(self.containers.get(cj), a))
                b_in_a = (ci is not None and self._contains(self.containers.get(ci), b))
                if a_in_b or b_in_a:
                    # padding check: inner must sit >=10px inside
                    outer = self.containers[cj] if a_in_b else self.containers[ci]
                    inner = a if a_in_b else b
                    if (tuple(round(v) for v in inner)
                            == tuple(round(v) for v in outer)):
                        continue  # the container's own shape visual
                    pad = min(inner[0] - outer[0], inner[1] - outer[1],
                              outer[2] - inner[2], outer[3] - inner[3])
                    if pad < 10:
                        errs.append(f"{ni}/{nj}: padding {pad:.0f}px < 10 inside container")
                    continue
                errs.append(f"OVERLAP: {ni} {tuple(round(v) for v in a)} vs "
                            f"{nj} {tuple(round(v) for v in b)}")
        if errs:
            raise ValueError("self-check failed:\n  " + "\n  ".join(errs))

    @staticmethod
    def _contains(outer, inner):
        if outer is None:
            return False
        return (inner[0] >= outer[0] and inner[1] >= outer[1]
                and inner[2] <= outer[2] and inner[3] <= outer[3])

# ---------------------------------------------------------------- layouts ---

def layout_stat_label_top(ctx, card):
    t = ctx.t
    ctx.glow(600, 260, 430, 22)
    # zone 1: label on top (no brand kicker)
    ctx.text(600, 140, card["label"], "Poppins", 600, 30, t["accent"],
             anchor="ma", tracking=8, name="label")
    ctx.zone()
    # zone 2: hero numeral
    ctx.text(600, 212, card["hero"], "Ubuntu", 700, 170, t["fg"],
             anchor="ma", name="hero")
    ctx.zone()
    # zone 3: data-proof pill (two-tone segments)
    segs = []
    for text, tone in card["proof"]:
        if tone == "accent":
            segs.append((text, t["accent"], ("Poppins", 600)))
        elif tone == "fg":
            segs.append((text, t["fg"], ("Poppins", 600)))
        else:
            segs.append((text, t["muted"], ("Poppins", 400)))
    fs = 34
    widths = [ctx.text_w(s, fam, wt, fs) for s, _, (fam, wt) in segs]
    total = sum(widths)
    pw, ph, py = total + 150, 104, 420
    px = (W - pw) / 2
    cid = ctx.new_container("proof-pill", px, py, pw, ph)
    ctx.rect(px, py, pw, ph, 52, t["surface"], stroke=t["accent"],
             stroke_w=2, stroke_alpha=110, name="proof-pill-shape",
             container=cid)
    th = ctx.text_h("Poppins", 600, fs)
    ty = py + (ph - th) / 2
    x = (W - total) / 2
    for (s, col, (fam, wt)), wch in zip(segs, widths):
        ctx.text(x, ty, s, fam, wt, fs, col, anchor="la",
                 name="proof-seg", container=cid)
        x += wch
    ctx.zone()


def layout_model_cards(ctx, card):
    t = ctx.t
    ctx.glow(600, 140, 430, 26)
    # zone 1: eyebrow kicker
    ctx.text(600, 92, card["eyebrow"], "Poppins", 600, 26, t["accent2"],
             anchor="ma", tracking=7, name="eyebrow")
    ctx.zone()
    # zone 2: hero
    hb = ctx.text(600, 158, card["hero"], "Ubuntu", 700, 190, t["fg"],
                  anchor="ma", name="hero")
    ctx.zone()
    # zone 3: headline (1-2 lines)
    lines = ctx.wrap(card["headline"], "Ubuntu", 700, 56, 1040, 2)
    hy = 378
    for i, ln in enumerate(lines):
        ctx.text(600, hy + i * 66, ln, "Ubuntu", 700, 56, t["fg"],
                 anchor="ma", name=f"headline-{i}")
    ctx.zone()
    # zone 4: separated segment cards
    segs = card["segments"]
    assert 2 <= len(segs) <= 3, "model-cards needs 2-3 segments"
    cw = 440 if len(segs) == 2 else 322
    gap = 36 if len(segs) == 2 else 32
    chh, y0 = 96, hy + 66 * len(lines) + 32
    x0 = (W - (cw * len(segs) + gap * (len(segs) - 1))) / 2
    for i, sg in enumerate(segs):
        x = x0 + i * (cw + gap)
        cid = ctx.new_container(f"seg-{i}", x, y0, cw, chh)
        ctx.rect(x, y0, cw, chh, 16, t["surface"], stroke=t["hair"][:3],
                 stroke_w=2, stroke_alpha=t["hair"][3],
                 name=f"seg-{i}-shape", container=cid)
        ctx.text(x + cw / 2, y0 + 14, sg["value"], "Ubuntu", 700, 40,
                 t["fg"], anchor="ma", name=f"seg-{i}-value", container=cid)
        ctx.text(x + cw / 2, y0 + 62, sg["label"], "Poppins", 600, 20,
                 t["muted"], anchor="ma", tracking=3,
                 name=f"seg-{i}-label", container=cid)
    ctx.zone()
    # zone 5 (optional): tiny footer
    if card.get("footer"):
        ctx.text(600, 600, card["footer"], "Poppins", 400, 22, t["dim"],
                 anchor="ma", name="footer")
        ctx.zone()


def layout_compare_2col(ctx, card):
    t = ctx.t
    ctx.glow(600, 120, 400, 20)
    # zone 1: title (1-2 lines)
    lines = ctx.wrap(card["title"], "Ubuntu", 700, 52, 1040, 2)
    tb = 0
    for i, ln in enumerate(lines):
        _, _, _, b = ctx.text(600, 70 + i * 62, ln, "Ubuntu", 700, 52,
                              t["fg"], anchor="ma", name=f"title-{i}")
        tb = max(tb, b)
    ctx.zone()
    # optional subtitle (template key): small muted line under the title
    if card.get("subtitle"):
        _, _, _, sb = ctx.text(600, tb + 10, card["subtitle"], "Poppins", 400,
                               26, t["muted"], anchor="ma", name="subtitle")
        tb = sb
        ctx.zone()
    # two cards
    y0 = tb + 36
    card_h = min(300, 575 - 32 - 84 - y0)
    if card_h < 240:
        raise ValueError("compare-2col: title too long, no room for cards")
    cw, gap = 500, 40
    x0 = (W - (cw * 2 + gap)) / 2
    sides = [("left", card["left"], t["dim"]), ("right", card["right"], t["accent2"])]
    for i, (side, data, head_col) in enumerate(sides):
        x = x0 + i * (cw + gap)
        cid = ctx.new_container(f"col-{side}", x, y0, cw, card_h)
        ctx.rect(x, y0, cw, card_h, 18, t["surface"], stroke=t["hair"][:3],
                 stroke_w=2, stroke_alpha=t["hair"][3],
                 name=f"col-{side}-shape", container=cid)
        ctx.text(x + cw / 2, y0 + 28, data["head"], "Poppins", 600, 24,
                 head_col, anchor="ma", tracking=4,
                 name=f"col-{side}-head", container=cid)
        rows = data["rows"]
        max_rows = min(4, int((card_h - 68 - 20) // 52))
        if len(rows) > max_rows:
            raise ValueError(f"compare-2col {side}: {len(rows)} rows > {max_rows} fit")
        ry = y0 + 68
        for r, row in enumerate(rows):
            rlines = ctx.wrap(row, "Poppins", 400, 25, cw - 60, 2)
            for k, ln in enumerate(rlines):
                ctx.text(x + 30, ry + r * 52 + k * 30, ln, "Poppins", 400,
                         25, t["muted"], anchor="la",
                         name=f"col-{side}-row{r}", container=cid)
    ctx.zone()
    ctx.zone()
    # zone 4: verdict pill
    v = card["verdict"]
    vw = ctx.text_w(v, "Poppins", 600, 30) + 150
    if vw > 1040:
        raise ValueError("compare-2col: verdict too long, shorten it")
    vy, vh = y0 + card_h + 32, 84
    px = (W - vw) / 2
    cid = ctx.new_container("verdict", px, vy, vw, vh)
    ctx.rect(px, vy, vw, vh, 42, t["surface"], stroke=t["accent"],
             stroke_w=2, stroke_alpha=110, name="verdict-shape", container=cid)
    ctx.text(W / 2, vy + vh / 2, v, "Poppins", 600, 30, t["fg"],
             anchor="mm", name="verdict-text", container=cid)
    ctx.zone()


def layout_ranking_list(ctx, card):
    t = ctx.t
    ctx.glow(600, 120, 400, 20)
    # zone 1: title
    lines = ctx.wrap(card["title"], "Ubuntu", 700, 50, 1040, 2)
    tb = 0
    for i, ln in enumerate(lines):
        _, _, _, b = ctx.text(600, 70 + i * 60, ln, "Ubuntu", 700, 50,
                              t["fg"], anchor="ma", name=f"title-{i}")
        tb = max(tb, b)
    ctx.zone()
    # zones 2-5: ranked rows. "factors" (template key): 5 bare labels -> compact rows.
    rows = card.get("rows")
    if card.get("factors"):
        rows = [{"rank": i + 1, "title": f, "desc": ""}
                for i, f in enumerate(card["factors"])]
    if rows is None:
        raise ValueError("ranking-list needs 'rows' or 'factors'")
    if len(rows) > 5:
        raise ValueError(f"ranking-list: {len(rows)} rows > 5 max")
    rh, gap = (78, 10) if len(rows) == 5 else (100, 13)
    y = tb + 24
    if y + len(rows) * rh + (len(rows) - 1) * gap > 575:
        raise ValueError("ranking-list: rows do not fit, shorten titles")
    if y + len(rows) * rh + (len(rows) - 1) * gap > 575:
        raise ValueError("ranking-list: rows do not fit, shorten titles")
    for i, row in enumerate(rows):
        ry = y + i * (rh + gap)
        rsize = 54 if len(rows) == 5 else 62
        ctx.text(195, ry + 14, str(row["rank"]), "Ubuntu", 700, rsize,
                 t["accent"], anchor="ra", name=f"rank-{i}")
        tsize = 27 if len(rows) == 5 else 28
        ctx.text(235, ry + 12, row["title"], "Poppins", 600, tsize,
                 t["fg"], anchor="la", name=f"row-{i}-title")
        dlines = ctx.wrap(row.get("desc", ""), "Poppins", 400, 22, 850, 2)
        for k, ln in enumerate(dlines):
            ctx.text(235, ry + 48 + k * 27, ln, "Poppins", 400, 22,
                     t["muted"], anchor="la", name=f"row-{i}-desc")
    ctx.zone()  # the ranked rows read as one visual block


def layout_bars(ctx, card):
    t = ctx.t
    ctx.glow(600, 120, 400, 20)
    # zone 1: title
    lines = ctx.wrap(card["title"], "Ubuntu", 700, 50, 1040, 2)
    tb = 0
    for i, ln in enumerate(lines):
        _, _, _, b = ctx.text(600, 70 + i * 60, ln, "Ubuntu", 700, 50,
                              t["fg"], anchor="ma", name=f"title-{i}")
        tb = max(tb, b)
    ctx.zone()
    # zone 2: bars
    bars = card["bars"]
    rh, gap, y = 64, 26, tb + 32
    max_bars = 5 if y + 5 * rh + 4 * gap <= 575 else 4
    if len(bars) > max_bars:
        raise ValueError(f"bars: {len(bars)} bars > {max_bars} fit")
    for i, b in enumerate(bars):
        by = y + i * (rh + gap)
        cid = ctx.new_container(f"bar-{i}", 110, by, 940, rh)
        lab = ctx.wrap(b["label"], "Poppins", 400, 28, 290, 1)[0]
        ctx.text(110, by + 16, lab, "Poppins", 400, 28, t["fg"],
                 anchor="la", name=f"bar-{i}-label", container=cid)
        tx, tw, thh = 430, 600, 26
        ctx.rect(tx, by + 19, tw, thh, 13, t["surface"],
                 name=f"bar-{i}-track", container=cid)
        fw = max(8, tw * min(100, b["pct"]) / 100)
        ctx.rect(tx, by + 19, fw, thh, 13, t["accent"],
                 name=f"bar-{i}-fill", container=cid)
        ctx.text(1042, by + 14, f"{b['pct']:g}%", "Poppins", 600, 26,
                 t["fg"], anchor="la", name=f"bar-{i}-pct", container=cid)
    ctx.zone()
    # zone 3 (optional): note
    if card.get("note"):
        ny = y + len(bars) * rh + (len(bars) - 1) * gap + 22
        if ny > 600:
            raise ValueError("bars: note does not fit, shorten bars")
        ctx.text(600, ny, card["note"], "Poppins", 400, 22, t["dim"],
                 anchor="ma", name="note")
        ctx.zone()


LAYOUTS = {
    "stat-label-top": layout_stat_label_top,
    "model-cards": layout_model_cards,
    "compare-2col": layout_compare_2col,
    "ranking-list": layout_ranking_list,
    "bars": layout_bars,
}

# ------------------------------------------------------------- backends ---

def render_png(ctx):
    t = ctx.t
    img = Image.new("RGBA", (W, H), t["base"] + "FF")
    for p in ctx.prims:
        if p["t"] == "glow":
            layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            d = ImageDraw.Draw(layer)
            cx, cy, r = p["cx"], p["cy"], p["r"]
            d.ellipse([cx - r, cy - r, cx + r, cy + r],
                      fill=p["color"] + (p["alpha"],))
            img = Image.alpha_composite(
                img, layer.filter(ImageFilter.GaussianBlur(r / 2)))
        elif p["t"] == "rect":
            d = ImageDraw.Draw(img)
            outline = None
            if p.get("stroke"):
                sc = p["stroke"]
                rgb = hex_rgb(sc) if isinstance(sc, str) else sc[:3]
                outline = rgb + (p.get("stroke_alpha", 255),)
            d.rounded_rectangle(
                [p["x"], p["y"], p["x"] + p["w"], p["y"] + p["h"]],
                radius=p["rx"], fill=hex_rgb(p["fill"]),
                outline=outline, width=p.get("stroke_w", 0))
        elif p["t"] == "text":
            d = ImageDraw.Draw(img)
            d.text((p["x"], p["y"]), p["s"],
                   font=font(p["fam"], p["weight"], p["size"]),
                   fill=hex_rgb(p["fill"]), anchor="la")
        elif p["t"] == "tracked":
            d = ImageDraw.Draw(img)
            f = font(p["fam"], p["weight"], p["size"])
            x = p["x"]
            for ch in p["s"]:
                d.text((x, p["y"]), ch, font=f, fill=hex_rgb(p["fill"]))
                x += d.textbbox((0, 0), ch, font=f)[2] + p["tracking"]
    return img.convert("RGB")


def _esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_svg(ctx):
    t = ctx.t
    gr, gg, gb = t["glow"]
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"'
        f' viewBox="0 0 {W} {H}">',
        '<defs><radialGradient id="gl">'
        f'<stop offset="0%" stop-color="rgb({gr},{gg},{gb})" stop-opacity="0.10"/>'
        f'<stop offset="100%" stop-color="rgb({gr},{gg},{gb})" stop-opacity="0"/>'
        '</radialGradient></defs>',
        f'<rect width="{W}" height="{H}" fill="{t["base"]}"/>',
    ]
    for p in ctx.prims:
        if p["t"] == "glow":
            out.append(f'<circle cx="{p["cx"]}" cy="{p["cy"]}" r="{p["r"]}"'
                       ' fill="url(#gl)"/>')
        elif p["t"] == "rect":
            s = (f'<rect x="{p["x"]:.1f}" y="{p["y"]:.1f}"'
                 f' width="{p["w"]:.1f}" height="{p["h"]:.1f}" rx="{p["rx"]}"'
                 f' fill="{p["fill"]}"')
            if p.get("stroke"):
                sc = p["stroke"]
                sc = sc if isinstance(sc, str) else "#%02x%02x%02x" % sc[:3]
                s += (f' stroke="{sc}" stroke-width="{p["stroke_w"]}"'
                      f' stroke-opacity="{p.get("stroke_alpha", 255) / 255:.2f}"')
            out.append(s + "/>")
        elif p["t"] in ("text", "tracked"):
            fam = "Ubuntu" if p["fam"] == "Ubuntu" else "Poppins"
            # SVG letter-spacing applies after every glyph (incl. last);
            # PNG adds it only between glyphs -> nudge left by half a unit
            # so the centered start position matches.
            ax = p["ax"] - (p["tracking"] / 2 if p["t"] == "tracked" else 0)
            ls = (f' letter-spacing="{p["tracking"]}"'
                  if p["t"] == "tracked" else "")
            out.append(
                f'<text x="{ax:.1f}" y="{p["baseline"]:.1f}"'
                f' font-family="{fam}, sans-serif" font-weight="{p["weight"]}"'
                f' font-size="{p["size"]}" fill="{p["fill"]}"'
                f' text-anchor="{p["svg_anchor"]}"{ls}>{_esc(p["s"])}</text>')
    out.append("</svg>")
    return "\n".join(out)


# ------------------------------------------------------------------- cli ---

import re  # noqa: E402


def area_from_dir(adir):
    leaf = Path(adir).name
    slug = re.sub(r"^\d+-", "", leaf)
    words = slug.replace("-", " ")
    return {"AREA": words.upper(),
            "Area": words.title().replace(" Dc", " DC")}


def substitute(cards, area):
    s = json.dumps(cards)
    s = s.replace("{{AREA}}", area["AREA"]).replace("{{Area}}", area["Area"])
    return json.loads(s)


def render_card(theme, card, out_dir, n):
    ctx = Ctx(theme)
    LAYOUTS[card["layout"]](ctx, card)
    ctx.check()
    out_dir.mkdir(parents=True, exist_ok=True)
    render_png(ctx).save(out_dir / f"infographic-{n}.png")
    (out_dir / f"infographic-{n}.svg").write_text(render_svg(ctx))
    print(f"wrote infographic-{n}.png/.svg -> {out_dir}")


def main():
    ap = argparse.ArgumentParser(description="v4 infographic renderer")
    ap.add_argument("--data", required=True, help="data JSON path")
    ap.add_argument("--dir", default=None, help="article dir override")
    args = ap.parse_args()

    data = json.loads(Path(args.data).read_text())
    theme = data["theme"]
    if theme not in THEMES:
        raise SystemExit(f"unknown theme {theme}")
    articles = data.get("articles")
    if not articles:
        d = args.dir or data.get("dir")
        if not d:
            raise SystemExit("no article dir: pass --dir or set dir/articles in JSON")
        articles = [{"dir": d}]
    for art in articles:
        adir = Path(args.dir or art.get("dir") or data.get("dir"))
        if not adir.is_absolute():
            adir = REPO / adir
        area = area_from_dir(adir)
        cards = substitute(data["cards"], area)
        for card in cards:
            if card["layout"] not in LAYOUTS:
                raise SystemExit(f"unknown layout {card['layout']}")
            render_card(theme, card, adir, card["n"])


if __name__ == "__main__":
    main()
