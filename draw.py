"""Draw the front page for 23 November 2026 as a single 1024x1024 PNG.

No network, no clock, no randomness: the same run always writes the same
bytes. Reads nothing but the DejaVu fonts shipped on this machine.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 36

PAPER = (250, 246, 236)
INK = (25, 25, 25)
SOFT = (84, 84, 78)
RED = (179, 38, 30)
NAVY = (20, 33, 61)
CARD = (255, 255, 255)
LINE = (206, 200, 186)
TEAL = (15, 118, 110)
BLUE = (29, 78, 150)
PLUM = (122, 54, 120)
RUST = (190, 96, 20)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns a list of lines that fit `width` pixels."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def block(draw, x, y, text, fnt, width, fill, leading):
    """Draw wrapped text; returns the y just below the last line."""
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x0, y, x1, fill=INK, width=2):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def draw_globe(draw, cx, cy, r):
    """A small cracked globe: teal disc, latitude lines, red crack."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(223, 238, 234),
                 outline=TEAL, width=4)
    draw.arc([cx - r, cy - r, cx + r, cy + r], 20, 160, fill=TEAL, width=2)
    draw.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=TEAL, width=2)
    draw.line([(cx - r + 8, cy - r // 3), (cx + r - 8, cy - r // 3)],
              fill=TEAL, width=2)
    draw.line([(cx - r + 8, cy + r // 3), (cx + r - 8, cy + r // 3)],
              fill=TEAL, width=2)
    draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=TEAL)
    crack = [(cx - 18, cy - r + 6), (cx + 2, cy - r // 2), (cx - 12, cy),
             (cx + 10, cy + r // 3), (cx - 4, cy + r - 8)]
    draw.line(crack, fill=RED, width=5, joint="curve")


def chip_house(draw, x, y, s, color):
    draw.polygon([(x, y + s * 0.45), (x + s / 2, y), (x + s, y + s * 0.45)],
                 fill=color)
    draw.rectangle([x + s * 0.14, y + s * 0.45, x + s * 0.86, y + s * 0.95],
                   fill=color)
    draw.rectangle([x + s * 0.42, y + s * 0.62, x + s * 0.58, y + s * 0.95],
                   fill=PAPER)


def chip_check(draw, x, y, s, color):
    draw.rectangle([x, y, x + s, y + s], fill=color)
    draw.line([(x + s * 0.18, y + s * 0.52), (x + s * 0.42, y + s * 0.76),
               (x + s * 0.84, y + s * 0.26)], fill=(255, 255, 255), width=7,
              joint="curve")


def chip_cross(draw, x, y, s, color):
    draw.rectangle([x + s * 0.38, y + s * 0.12, x + s * 0.62, y + s * 0.88],
                   fill=color)
    draw.rectangle([x + s * 0.12, y + s * 0.38, x + s * 0.88, y + s * 0.62],
                   fill=color)


def chip_wave(draw, x, y, s, color):
    pts = []
    for i in range(9):
        px = x + i * (s / 8)
        py = y + s / 2 + (s * 0.28 if i % 2 == 0 else -s * 0.28)
        pts.append((px, py))
    draw.line(pts, fill=color, width=6, joint="curve")


def story_card(draw, x, y, w, h, chip, color, kicker, headline, summary):
    draw.rectangle([x, y, x + w, y + h], fill=CARD, outline=LINE, width=2)
    pad = 16
    chip(draw, x + pad, y + pad, 54, color)
    tx = x + pad + 54 + 14
    tw = x + w - pad - tx  # width from the text column to the inner edge
    f_kick = font(SANS_BOLD, 15)
    f_head = font(SANS_BOLD, 24)
    f_sum = font(SANS, 18)
    draw.text((tx, y + pad + 2), kicker, font=f_kick, fill=RED)
    hy = y + pad + 24
    hy = block(draw, tx, hy, headline, f_head, tw, INK, 29)
    block(draw, tx, hy + 6, summary, f_sum, tw, SOFT, 23)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # ---- masthead ------------------------------------------------------
    f_title = font(SERIF, 60)
    title = "THE WORLD TODAY"
    tw = draw.textlength(title, font=f_title)
    draw.text(((W - tw) / 2, 26), title, font=f_title, fill=INK)
    f_date = font(SANS_BOLD, 25)
    date = "M O N D A Y ,  2 3  N O V E M B E R  2 0 2 6"
    dw = draw.textlength(date, font=f_date)
    draw.text(((W - dw) / 2, 104), date, font=f_date, fill=RED)
    rule(draw, MARGIN, 148, W - MARGIN, INK, 3)
    rule(draw, MARGIN, 154, W - MARGIN, INK, 1)

    # ---- lead story: COP31 ---------------------------------------------
    ly = 172
    f_kick = font(SANS_BOLD, 17)
    draw.text((MARGIN, ly), "CLIMATE  —  ANTALYA, TURKEY", font=f_kick, fill=RED)
    f_head = font(SERIF, 47)
    hy = ly + 28
    hy = block(draw, MARGIN, hy,
               "COP31 COLLAPSES: NO CLIMATE DEAL",
               f_head, 660, INK, 52)
    f_sum = font(SANS, 21)
    block(draw, MARGIN, hy + 10,
          "Two weeks of UN talks end without agreement after the EU and "
          "island states reject a text that never mentions fossil fuels — "
          "the first COP breakdown since 2009.",
          f_sum, 660, SOFT, 27)
    draw_globe(draw, 862, 268, 92)

    rule(draw, MARGIN, 402, W - MARGIN, LINE, 2)

    # ---- four story cards ----------------------------------------------
    gx, gy = MARGIN, 418
    cw, ch = 464, 186
    gap = 24
    story_card(draw, gx, gy, cw, ch, chip_house, TEAL,
               "UKRAINE",
               "Boy, 7, pulled alive from rubble",
               "Nine killed as Russian drones hit a Kyiv home; "
               "rescuers keep digging for the missing.")
    story_card(draw, gx + cw + gap, gy, cw, ch, chip_check, BLUE,
               "UNITED STATES",
               "Democrats take biggest House majority since 1992",
               "A North Carolina flip hands them the chamber "
               "in the midterms.")
    story_card(draw, gx, gy + ch + gap, cw, ch, chip_cross, PLUM,
               "HEALTH",
               "NHS launches biggest AI cancer trial",
               "700,000 women to have breast scans read by AI "
               "in a world-first screening study.")
    story_card(draw, gx + cw + gap, gy + ch + gap, cw, ch, chip_wave, RUST,
               "PACIFIC",
               "Magnitude 6.5 quake strikes Vanuatu",
               "Deep tremor shakes the island region; "
               "no tsunami warning issued.")

    # ---- markets band: sixth story --------------------------------------
    by = 830
    draw.rectangle([MARGIN, by, W - MARGIN, by + 76], fill=NAVY)
    f_band = font(SANS_BOLD, 25)
    draw.text((MARGIN + 18, by + 10),
              "MARKETS REEL AS AI SELL-OFF SPREADS",
              font=f_band, fill=(255, 255, 255))
    f_band2 = font(SANS, 20)
    draw.text((MARGIN + 18, by + 42),
              "KOSPI falls 5%  ·  Taiwan shares swing 1,578 points in a day",
              font=f_band2, fill=(200, 210, 230))

    # ---- footer strip ----------------------------------------------------
    rule(draw, MARGIN, 922, W - MARGIN, INK, 2)
    f_foot = font(SANS, 16)
    block(draw, MARGIN, 936,
          "Manchester arena evacuated after suspected tear-gas release  ·  "
          "Mets sign Skubal in record $450m deal  ·  FIFA to confirm UK "
          "as 2035 Women's World Cup host  ·  India v New Zealand Test "
          "reaches a Day 5 decider",
          f_foot, W - 2 * MARGIN, SOFT, 21)

    img.save("entry.png")


if __name__ == "__main__":
    main()
