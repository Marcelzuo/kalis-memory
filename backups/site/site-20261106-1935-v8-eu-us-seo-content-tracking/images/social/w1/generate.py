#!/usr/bin/env python3
"""
W1 Social Media Image Generator v4 — Mammon
Changes from v3:
- Logo: removed diamond, gold line(80×1) → KALIS(large white) → TORIK(small gold), ~17% canvas h
- Text: gold #C9A96E on light overlay (white ~82% opacity)
- Updated WED copy p3/p5/p6/p7 per 米迦勒 2026-06-27
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

# === PATHS ===
OUT = "/Users/zuo/kalistorik-site/images/social/w1"
BG_DIR = os.path.join(OUT, "bg")
FONT_TTC = "/System/Library/Fonts/HelveticaNeue.ttc"

# === VI COLORS ===
GOLD = (201, 169, 110)       # #C9A96E
WHITE = (255, 255, 255)

# === CANVAS SIZES ===
IG_W, IG_H = 1080, 1350
FB_W, FB_H = 1200, 630

# ============================================================
# LOCKED COPY v4 — DO NOT MODIFY (approved by 米迦勒 2026-06-27)
# ============================================================

WED_TEXT = [
    '"CHEAPER" IS A LIE.',
    'China furniture export 2024:\nUSD 86.4 billion.\n4× Türkiye. 6× Vietnam.',
    'The largest furniture cluster on\nthe planet. Sofas, dining tables,\nbeds, office chairs.\nBut China does not make\nfurniture in one city.',
    'Dining tables come out of one\nprovince. Chairs and metal-frame\npieces come out of another.\nEach region has its own\nspecialism.',
    'Shipping Shenzhen → Rotterdam:\n28 days door-to-door.',
    'Twelve years of sourcing\nteaches you: brands that know\ntheir factory have fewer\nquality claims.',
    'Multiple times fewer claims.\nBecause you catch issues before\nthe container leaves.',
    'Stop guessing.\nStart knowing.\n→ kalistorik.com',
]

FRI_TEXT = [
    'THE FACTORY HAS A SMELL.\nYou will recognise it.',
    'Warm metal. Cut wood.\nSawdust on concrete.',
    'The floor tells you more than\nthe catalogue ever will.',
    'Real QC is the silence when\na full pallet passes inspection.',
    'It is the phone call a buyer gets\nbefore the container leaves.',
    'Not after it clears customs.\nBefore.',
    'That call changes everything.',
    'We catch it before you do.\n→ kalistorik.com',
]

FB_HEADLINE = "That call we make before\nthe container leaves."
FB_SUBTEXT = "kalistorik.com"

# === BACKGROUND PHOTOS ===
INTERIOR_PHOTOS = [
    os.path.join(BG_DIR, "w1_showroom_living.jpg"),
    os.path.join(BG_DIR, "w1_bedroom_bright.jpg"),
    os.path.join(BG_DIR, "w1_living_cozy.jpg"),
]
FACTORY_PHOTO = "/Users/zuo/kalistorik-site/images/factories/factory-hero.jpg"


# === FONT HELPERS ===
def get_font(size, weight="light"):
    indices = {"light": 4, "regular": 8, "bold": 1}
    idx = indices.get(weight, 4)
    try:
        return ImageFont.truetype(FONT_TTC, size, index=idx)
    except Exception:
        try:
            return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size, index=0)
        except Exception:
            return ImageFont.load_default()


# === IMAGE PROCESSING ===
def cover_fit(img, target_w, target_h, anchor_x=0.5, anchor_y=0.5):
    iw, ih = img.size
    scale = max(target_w / iw, target_h / ih)
    new_w, new_h = int(iw * scale), int(ih * scale)
    img = img.resize((new_w, new_h), Image.LANCZOS)
    left = int((new_w - target_w) * anchor_x)
    top = int((new_h - target_h) * anchor_y)
    return img.crop((left, top, left + target_w, top + target_h))


def warm_treatment(img):
    img = ImageEnhance.Color(img).enhance(1.10)
    img = ImageEnhance.Brightness(img).enhance(1.08)
    return img


def make_light_overlay(w, h, base_alpha=185):
    """
    Two-zone overlay:
    - Top ~83%: white overlay so gold text is readable on photo
    - Bottom ~17% (logo area): dark overlay so white KALIS + gold TORIK pop
    """
    overlay = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    logo_area_h = max(int(h * 0.17), 130)
    logo_start = h - logo_area_h

    for y in range(h):
        if y < logo_start - int(h * 0.03):
            # Text zone: white overlay, gradient top→moderate
            if y < h * 0.12:
                a = int(base_alpha * 0.50)
            elif y < h * 0.35:
                frac = (y - h * 0.12) / (h * 0.23)
                a = int(base_alpha * (0.50 + frac * 0.30))
            else:
                frac = min(1.0, (y - h * 0.35) / (logo_start - h * 0.35))
                a = int(base_alpha * (0.80 + frac * 0.10))
            a = min(a, base_alpha)
            draw.line([(0, y), (w, y)], fill=(255, 255, 255, a))
        elif y < logo_start:
            # Transition zone: white→dark, ~3% of height
            frac = (y - (logo_start - int(h * 0.03))) / (int(h * 0.03))
            # Blend from white overlay to dark overlay
            wa = int(base_alpha * (0.90 * (1 - frac)))
            da = int(100 * frac)
            r = int(255 * (1 - frac) + 25 * frac)
            g = int(255 * (1 - frac) + 20 * frac)
            b = int(255 * (1 - frac) + 15 * frac)
            draw.line([(0, y), (w, y)], fill=(r, g, b, max(wa, da)))
        else:
            # Logo zone: dark overlay for white KALIS visibility
            frac = (y - logo_start) / (h - logo_start)
            da = int(95 + frac * 35)  # dark gradient
            draw.line([(0, y), (w, y)], fill=(20, 15, 12, da))
    return overlay


# === VI LOGO RENDERING v4 ===
def draw_vi_logo(draw, canvas_w, canvas_h):
    """
    Logo at bottom center, ~17% of canvas height.
    Structure: gold line(80×1 #C9A96E) → KALIS(large white) → TORIK(small #C9A96E).
    No diamond.
    """
    logo_area_h = max(int(canvas_h * 0.17), 130)
    cx = canvas_w // 2

    # ── Gold rule: 80×1px #C9A96E ──
    rule_w = 80
    rule_h = max(1, int(canvas_h * 0.0008))
    rule_y = canvas_h - logo_area_h
    draw.rectangle(
        [cx - rule_w // 2, rule_y, cx + rule_w // 2, rule_y + rule_h],
        fill=GOLD,
    )

    # ── KALIS: large white, letter-spaced ──
    kalis_size = int(logo_area_h * 0.38)
    gap_rule_to_kalis = int(logo_area_h * 0.10)
    kalis_y = rule_y + gap_rule_to_kalis

    font_k = get_font(kalis_size, "light")
    letters_k = list("KALIS")
    ls_k = int(kalis_size * 0.35)
    widths_k = [draw.textbbox((0, 0), ch, font=font_k)[2] for ch in letters_k]
    k_total = sum(widths_k) + ls_k * (len(letters_k) - 1)
    k_x = cx - k_total // 2
    for ch in letters_k:
        draw.text((k_x, kalis_y), ch, fill=WHITE, font=font_k)
        k_x += widths_k[letters_k.index(ch)] + ls_k

    # ── TORIK: small gold, letter-spaced (breathing room below KALIS) ──
    torik_size = int(logo_area_h * 0.14)
    gap_kalis_to_torik = int(logo_area_h * 0.08)
    torik_y = kalis_y + kalis_size + gap_kalis_to_torik

    font_t = get_font(torik_size, "light")
    letters_t = list("TORIK")
    ls_t = int(torik_size * 1.1)
    widths_t = [draw.textbbox((0, 0), ch, font=font_t)[2] for ch in letters_t]
    t_total = sum(widths_t) + ls_t * (len(letters_t) - 1)
    t_x = cx - t_total // 2
    for i, ch in enumerate(letters_t):
        draw.text((t_x, torik_y), ch, fill=GOLD, font=font_t)
        t_x += widths_t[i] + ls_t


# === PAGE GENERATOR ===
def make_ig_page(bg_path, text_lines, out_path, crop_x=0.5, crop_y=0.5):
    bg = Image.open(bg_path).convert("RGB")
    bg = cover_fit(bg, IG_W, IG_H, anchor_x=crop_x, anchor_y=crop_y)
    bg = warm_treatment(bg)
    bg = bg.convert("RGBA")

    # Light overlay for gold text readability
    overlay = make_light_overlay(IG_W, IG_H, base_alpha=210)
    bg = Image.alpha_composite(bg, overlay)
    draw = ImageDraw.Draw(bg)

    # ── Text sizing ──
    lines = text_lines.split("\n")
    total_chars = sum(len(l) for l in lines)
    max_line = max(len(l) for l in lines) if lines else 0

    if len(lines) == 1 and total_chars < 30:
        font_size = 76
    elif len(lines) == 1:
        font_size = 64
    elif len(lines) == 2 and total_chars < 80:
        font_size = 56
    elif total_chars < 100:
        font_size = 48
    elif total_chars < 160:
        font_size = 42
    elif total_chars < 240:
        font_size = 38
    else:
        font_size = 34

    font = get_font(font_size, "light")
    line_h = int(font_size * 1.65)

    # ── Vertical centering above logo ──
    logo_start_y = IG_H - max(int(IG_H * 0.17), 130)
    text_area_h = logo_start_y - 60  # 60px top margin
    total_text_h = len(lines) * line_h
    y_start = max(60, (text_area_h - total_text_h) // 2)

    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font)
        tw = bbox[2] - bbox[0]
        x = (IG_W - tw) // 2
        y = y_start + i * line_h
        draw.text((x, y), line, fill=GOLD, font=font)

    # ── VI Logo at bottom ──
    draw_vi_logo(draw, IG_W, IG_H)

    bg.convert("RGB").save(out_path, "PNG", optimize=True)
    return os.path.basename(out_path)


def make_fb_post(bg_path, headline, subtext, out_path):
    bg = Image.open(bg_path).convert("RGB")
    bg = cover_fit(bg, FB_W, FB_H, anchor_x=0.5, anchor_y=0.5)
    bg = warm_treatment(bg)
    bg = bg.convert("RGBA")

    overlay = make_light_overlay(FB_W, FB_H, base_alpha=195)
    bg = Image.alpha_composite(bg, overlay)
    draw = ImageDraw.Draw(bg)

    # Headline
    lines = headline.split("\n")
    font_h = get_font(52, "light")
    lh = 68
    total_h = len(lines) * lh

    logo_start_y = FB_H - max(int(FB_H * 0.17), 130)
    text_area_h = logo_start_y - 40
    y_start = max(30, (text_area_h - total_h - 50) // 2)

    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font_h)
        tw = bbox[2] - bbox[0]
        x = (FB_W - tw) // 2
        y = y_start + i * lh
        draw.text((x, y), line, fill=GOLD, font=font_h)

    # Subtext
    font_sub = get_font(28, "light")
    sub_bbox = draw.textbbox((0, 0), subtext, font=font_sub)
    sub_w = sub_bbox[2] - sub_bbox[0]
    sub_x = (FB_W - sub_w) // 2
    sub_y = y_start + total_h + 36
    draw.text((sub_x, sub_y), subtext, fill=GOLD, font=font_sub)

    draw_vi_logo(draw, FB_W, FB_H)

    bg.convert("RGB").save(out_path, "PNG", optimize=True)
    return os.path.basename(out_path)


# === MAIN ===
def main():
    print("W1 Social Image Generator v4 — Mammon\n")

    # === IG Wednesday ===
    print("IG Wednesday (8 pages):")
    wed_config = [
        (0, 0.50, 0.30),
        (1, 0.50, 0.40),
        (2, 0.50, 0.36),
        (0, 0.60, 0.42),
        (1, 0.42, 0.48),
        (2, 0.55, 0.40),
        (0, 0.45, 0.52),
        (1, 0.50, 0.36),
    ]
    for i in range(8):
        bg_idx, cx, cy = wed_config[i]
        bg_path = INTERIOR_PHOTOS[bg_idx]
        out = os.path.join(OUT, f"w1-ig-wed-{i+1:02d}.png")
        name = make_ig_page(bg_path, WED_TEXT[i], out, crop_x=cx, crop_y=cy)
        print(f"  {name}")

    # === IG Friday ===
    print("\nIG Friday (8 pages):")
    fri_config = [
        (0.50, 0.30),
        (0.42, 0.46),
        (0.58, 0.42),
        (0.50, 0.54),
        (0.40, 0.36),
        (0.62, 0.48),
        (0.50, 0.46),
        (0.45, 0.50),
    ]
    for i in range(8):
        cx, cy = fri_config[i]
        out = os.path.join(OUT, f"w1-ig-fri-{i+1:02d}.png")
        name = make_ig_page(FACTORY_PHOTO, FRI_TEXT[i], out, crop_x=cx, crop_y=cy)
        print(f"  {name}")

    # === FB Post ===
    print("\nFB Post (1 image):")
    out = os.path.join(OUT, "w1-fb-post.png")
    name = make_fb_post(FACTORY_PHOTO, FB_HEADLINE, FB_SUBTEXT, out)
    print(f"  {name}")

    print(f"\nDone. 17 images → {OUT}/")


if __name__ == "__main__":
    main()
