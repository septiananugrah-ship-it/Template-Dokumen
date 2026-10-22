"""Gambar mockup untuk foto produk (Shopee/Lynk.id/Gumroad) dan PDF pratinjau
bertanda air, disusun dari render PNG slide."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

from .core import ROOT

FONT_DIR = ROOT / "assets" / "fonts"


def font(size, weight="Bold"):
    return ImageFont.truetype(str(FONT_DIR / f"Inter-{weight}.otf"), size)


def hex_rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rounded(im, radius):
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, *im.size), radius, fill=255)
    out = im.convert("RGBA")
    out.putalpha(mask)
    return out


def paste_card(canvas, im, xy, width, radius=14, shadow=28, angle=0, border=None):
    """Tempel slide dengan sudut membulat + bayangan lembut."""
    h = round(im.height * width / im.width)
    card = rounded(im.resize((width, h), Image.LANCZOS), radius)
    if border:
        d = ImageDraw.Draw(card)
        d.rounded_rectangle((0, 0, width - 1, h - 1), radius, outline=border, width=2)
    if angle:
        card = card.rotate(angle, expand=True, resample=Image.BICUBIC)
    pad = shadow * 2
    sh = Image.new("RGBA", (card.width + pad * 2, card.height + pad * 2), (0, 0, 0, 0))
    alpha = card.split()[3].point(lambda a: a * 0.35)
    blk = Image.new("RGBA", card.size, (10, 10, 30, 255))
    blk.putalpha(alpha)
    sh.paste(blk, (pad, pad + shadow // 2), blk)
    sh = sh.filter(ImageFilter.GaussianBlur(shadow / 2))
    x, y = xy
    canvas.alpha_composite(sh, (x - pad, y - pad))
    canvas.alpha_composite(card, (x, y))
    return card.size


def gradient(size, top, bottom):
    w, h = size
    base = Image.new("RGBA", size, top)
    grad = Image.new("L", (1, h))
    for y in range(h):
        grad.putpixel((0, y), int(255 * y / max(1, h - 1)))
    mask = grad.resize(size)
    base.paste(Image.new("RGBA", size, bottom), (0, 0), mask)
    return base


def text_center(d, cx, y, s, f, fill):
    w = d.textlength(s, font=f)
    d.text((cx - w / 2, y), s, font=f, fill=fill)


def pill(d, x, y, s, f, bg, fg, padx=22, pady=12):
    w = d.textlength(s, font=f)
    asc, desc = f.getmetrics()
    h = asc + desc
    d.rounded_rectangle((x, y, x + w + padx * 2, y + h + pady * 2), (h + pady * 2) // 2, fill=bg)
    d.text((x + padx, y + pady), s, font=f, fill=fg)
    return w + padx * 2, h + pady * 2


def wrap(d, s, f, width):
    words, lines, cur = s.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if d.textlength(t, font=f) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = wd
    lines.append(cur)
    return lines


# ---------------------------------------------------------------- mockup

INK = (24, 22, 48)
BG_TOP = (246, 244, 255)
BG_BOT = (226, 222, 250)
ACCENT = (255, 107, 74)


def cover_square(pkg, covers, out: Path, size=1080):
    """Foto utama: judul + kipas sampul semua tema."""
    im = gradient((size, size), BG_TOP + (255,), BG_BOT + (255,))
    d = ImageDraw.Draw(im)
    pill(d, 70, 64, pkg["badge"], font(26), ACCENT, (255, 255, 255))
    y = 150
    for line in pkg["headline"]:
        d.text((70, y), line, font=font(64), fill=INK)
        y += 76
    d.text((70, y + 10), pkg["tagline"], font=font(30, "Regular"), fill=(90, 86, 120))
    x = 70
    f = font(22, "SemiBold")
    for feat in pkg["chips"]:
        cw, _ = pill(d, x, y + 70, feat, f, (255, 255, 255), INK, padx=18, pady=10)
        x += cw + 14
    n = len(covers)
    w = 540
    step_x = (size - 140 - w) / max(1, n - 1)
    positions = [(round(70 + i * step_x), 560 + i * 48) for i in range(n)]
    for c, pos in zip(covers, positions):
        paste_card(im, c, pos, w, radius=16)
    im.convert("RGB").save(out, quality=92)


def theme_square(pkg, theme, slides, out: Path, size=1080):
    """Satu tema: sampul besar + 4 slide isi."""
    bg = hex_rgb(theme.colors["lt2"]) if not theme.dark else hex_rgb(theme.colors["dk2"])
    fg = hex_rgb(theme.colors["dk2"]) if not theme.dark else hex_rgb(theme.colors["lt1"])
    acc = hex_rgb(theme.colors["accent1"])
    im = Image.new("RGBA", (size, size), bg + (255,))
    d = ImageDraw.Draw(im)
    d.text((70, 60), f"Tema {theme.label}", font=font(56), fill=fg)
    d.text((70, 136), pkg["short"], font=font(28, "Regular"), fill=fg + (200,))
    paste_card(im, slides[0], (70, 215), size - 140, radius=18)
    small_w = (size - 140 - 30) // 2
    small_h = round(small_w * 9 / 16)
    big_h = round((size - 140) * 9 / 16)
    y0 = 215 + big_h + 30
    for i, s in enumerate(slides[1:3]):
        paste_card(im, s, (70 + i * (small_w + 30), y0), small_w, radius=12)
    d.rounded_rectangle((size - 250, size - 82, size - 70, size - 34), 24, fill=acc)
    text_center(d, size - 160, size - 76, "Bisa diedit", font(24, "SemiBold"),
                (255, 255, 255) if not theme.dark else hex_rgb(theme.colors["dk1"]))
    im.convert("RGB").save(out, quality=92)


def contents_square(pkg, grid_slides, out: Path, size=1080):
    """'Isi paket': daftar fitur + kisi slide."""
    im = gradient((size, size), (255, 255, 255, 255), BG_TOP + (255,))
    d = ImageDraw.Draw(im)
    d.text((70, 60), "Isi Paket", font=font(60), fill=INK)
    y = 150
    for feat in pkg["features"]:
        d.ellipse((72, y + 9, 92, y + 29), fill=ACCENT)
        d.text((110, y), feat, font=font(28, "SemiBold"), fill=INK)
        y += 50
    cols = len(grid_slides)
    gap = 18
    tw = (size - 140 - gap * (cols - 1)) // cols
    th = round(tw * 9 / 16)
    y0 = y + 30
    rows = min(len(grid_slides[0]), (size - y0 - 40) // (th + gap))
    for c, column in enumerate(grid_slides):  # satu kolom = satu tema
        for r, s in enumerate(column[:rows]):
            paste_card(im, s, (70 + c * (tw + gap), y0 + r * (th + gap)), tw, radius=6,
                       shadow=10)
    im.convert("RGB").save(out, quality=92)


def banner(pkg, covers, out: Path, w=1280, h=720):
    """Sampul Gumroad / Lynk.id (16:9)."""
    im = gradient((w, h), (36, 30, 92, 255), (20, 16, 52, 255))
    d = ImageDraw.Draw(im)
    pill(d, 70, 70, pkg["badge"], font(24), ACCENT, (255, 255, 255))
    y = 150
    for line in pkg["headline"]:
        d.text((70, y), line, font=font(58), fill=(255, 255, 255))
        y += 70
    for j, line in enumerate(wrap(d, pkg["tagline"], font(26, "Regular"), 520)):
        d.text((70, y + 16 + j * 36), line, font=font(26, "Regular"), fill=(201, 197, 236))
    for i, c in enumerate(covers[:3]):
        paste_card(im, c, (640 + i * 70, 120 + i * 150), 560, radius=14)
    im.convert("RGB").save(out, quality=92)


def preview_pdf(pages_by_theme, labels, out: Path, title):
    """PDF pratinjau: per tema satu halaman berisi 6 slide + tanda air."""
    pages = []
    W, H = 1754, 1240  # A4 lanskap ~150 dpi
    for (theme_label, slides) in zip(labels, pages_by_theme):
        pg = Image.new("RGBA", (W, H), (255, 255, 255, 255))
        d = ImageDraw.Draw(pg)
        d.text((80, 60), title, font=font(40), fill=INK)
        d.text((80, 116), f"Tema {theme_label}", font=font(28, "Regular"), fill=(90, 86, 120))
        cols, gap = 3, 30
        tw = (W - 160 - gap * (cols - 1)) // cols
        th = round(tw * 9 / 16)
        for i, s in enumerate(slides[:9]):
            r, c = divmod(i, cols)
            paste_card(pg, s, (80 + c * (tw + gap), 190 + r * (th + gap)), tw, radius=8,
                       shadow=10, border=(225, 225, 235))
        wm = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        wd = ImageDraw.Draw(wm)
        f = font(150)
        text_center(wd, W / 2, H / 2 - 90, "PRATINJAU", f, (120, 120, 140, 60))
        wm = wm.rotate(25, resample=Image.BICUBIC)
        pg.alpha_composite(wm)
        d = ImageDraw.Draw(pg)
        d.text((80, H - 60), "Pratinjau beresolusi rendah. File asli .pptx bisa diedit penuh.",
               font=font(22, "Regular"), fill=(120, 116, 150))
        pages.append(pg.convert("RGB"))
    pages[0].save(out, save_all=True, append_images=pages[1:], resolution=150)
