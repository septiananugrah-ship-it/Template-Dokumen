"""Desain konten media sosial (feed 1:1 dan story 9:16) di PowerPoint.

Ukuran slide: feed 8 × 8 in, story 6 × 10.667 in. Ekspor ke PNG/JPG dari
PowerPoint/Canva menghasilkan gambar 1080 px. Warna & font mengikuti tema
elegan (satu warna utama + netral) supaya feed terlihat seragam.
"""
from __future__ import annotations

from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches

from . import core as k
from .themes_elegan import _photo

FEED = (8.0, 8.0)
STORY = (6.0, 10.66667)


class SocialBuilder:
    def __init__(self, theme, size, brand, handle):
        self.t = theme
        self.W, self.H = size
        self.brand = brand
        self.handle = handle
        self.prs = k.new_presentation(theme)
        self.prs.slide_width = Inches(self.W)
        self.prs.slide_height = Inches(self.H)

    def build(self, specs, path):
        for spec in specs:
            spec = dict(spec)
            kind = spec.pop("type")
            getattr(self, kind)(**spec)
        self.prs.core_properties.title = self.brand
        self.prs.save(path)
        return path

    # ------------------------------------------------------------ dasar
    def _slide(self, bg=None):
        return k.blank_slide(self.prs, self.t, bg)

    @property
    def light(self):
        return self.t.bg

    @property
    def deep(self):
        return "dk2" if not self.t.dark else "dk1"

    @property
    def hi(self):
        """Warna sorotan di atas latar gelap (kicker, tombol, bingkai)."""
        return getattr(self.t, "hi", None) or ("accent1" if self.t.dark else "accent3")

    @property
    def hi_ink(self):
        return getattr(self.t, "hi_ink", None) or "dk1"

    def on(self, dark_bg):
        return "lt1" if dark_bg else self.t.primary

    def head(self, s, x, y, w, h, txt, size, color=None, **kw):
        kw.setdefault("bold", self.t.title_bold)
        return k.text(s, x, y, w, h, txt, size=size, color=color or self.t.primary,
                      font="+mj-lt", line_spacing=kw.pop("line_spacing", 1.0), **kw)

    def tag(self, s, dark_bg=False, y=None):
        """Nama toko + akun di tepi bawah (merek konsisten di setiap unggahan)."""
        y = self.H - 0.62 if y is None else y
        col = "lt1" if dark_bg else self.t.primary
        sub = (self.t.divider_sub if dark_bg else self.t.muted)
        k.text(s, 0.5, y, self.W / 2, 0.35, self.brand, size=12, bold=True, color=col,
               caps=True, spacing=2.5)
        k.text(s, self.W / 2, y, self.W / 2 - 0.5, 0.35, self.handle, size=12, color=sub,
               align="r")

    def pill(self, s, x, y, w, h, txt, fill, color, size=14):
        p = k.rrect(s, x, y, w, h, fill, radius=h / 2, name="Tombol")
        k.text(s, 0, 0, 0, 0, txt, size=size, bold=True, color=color, align="c", anchor="m",
               shape_obj=p, caps=True, spacing=1.5)
        return p

    def photo(self, s, x, y, w, h, label="Foto produk", kind=MSO_SHAPE.RECTANGLE):
        return _photo(s, self.t, x, y, w, h, kind=kind, label=label)

    # ------------------------------------------------------------ feed
    def new_arrival(self, kicker, name, price, note=""):
        s = self._slide()
        W, H = self.W, self.H
        self.photo(s, 0, 0, W, H * 0.68)
        k.text(s, 0.5, H * 0.68 + 0.35, 4, 0.35, kicker, size=13, bold=True,
               color=self.t.accent, caps=True, spacing=3)
        self.head(s, 0.5, H * 0.68 + 0.7, W - 3.2, 1.0, name, 32)
        k.text(s, W - 2.9, H * 0.68 + 0.75, 2.4, 0.6, price, size=24, bold=True,
               color=self.t.primary, align="r", font="+mj-lt")
        if note:
            k.text(s, W - 2.9, H * 0.68 + 1.3, 2.4, 0.4, note, size=12, color=self.t.muted,
                   align="r")
        self.tag(s)

    def promo(self, kicker, big, sub, period, cta):
        s = self._slide(self.deep)
        W, H = self.W, self.H
        k.rect(s, 0.35, 0.35, W - 0.7, H - 0.7, None, line=self.hi, line_w=1.0,
               name="Bingkai")
        k.text(s, 0.8, 1.2, W - 1.6, 0.4, kicker, size=15, bold=True, color=self.hi,
               align="c", caps=True, spacing=4)
        self.head(s, 0.6, 1.8, W - 1.2, 2.6, big, 120, color="lt1", align="c", anchor="m",
                  bold=True)
        k.text(s, 0.8, 4.4, W - 1.6, 0.9, sub, size=22, color="lt1", align="c",
               font="+mj-lt")
        k.text(s, 0.8, 5.3, W - 1.6, 0.4, period, size=14, color=self.t.divider_sub,
               align="c")
        self.pill(s, W / 2 - 1.6, 6.0, 3.2, 0.6, cta, self.hi,
                  self.hi_ink)
        self.tag(s, dark_bg=True, y=H - 0.95)

    def grid4(self, title, items):
        s = self._slide()
        W, H = self.W, self.H
        self.head(s, 0.5, 0.45, W - 1, 0.8, title, 30, align="c")
        gap = 0.3
        cw = (W - 1.0 - gap) / 2
        ch = (H - 1.6 - 0.8 - gap) / 2
        for i, (name, price) in enumerate(items):
            r, c = divmod(i, 2)
            x, y = 0.5 + c * (cw + gap), 1.45 + r * (ch + gap)
            self.photo(s, x, y, cw, ch - 0.65, label="Foto")
            k.text(s, x, y + ch - 0.6, cw * 0.62, 0.5, name, size=15, bold=True,
                   color=self.t.primary)
            k.text(s, x + cw * 0.6, y + ch - 0.6, cw * 0.4, 0.5, price, size=15,
                   color=self.t.accent, bold=True, align="r")
        self.tag(s)

    def testimonial(self, quote, name, detail, stars=5):
        s = self._slide(self.t.surface if not self.t.dark else "dk2")
        W, H = self.W, self.H
        k.icon(s, self.t, "quote", W / 2 - 0.4, 0.9, 0.8, self.t.accent)
        self.head(s, 0.8, 1.95, W - 1.6, 3.0, quote, 26, align="c", anchor="m",
                  line_spacing=1.2, bold=False)
        for i in range(stars):
            k.icon(s, self.t, "star", W / 2 - stars * 0.22 + i * 0.44, 5.15, 0.36,
                   self.t.accent)
        self.photo(s, W / 2 - 0.45, 5.75, 0.9, 0.9, label="", kind=MSO_SHAPE.OVAL)
        k.text(s, 0.8, 6.72, W - 1.6, 0.4, name, size=15, bold=True, color=self.t.primary,
               align="c")
        k.text(s, 0.8, 7.05, W - 1.6, 0.35, detail, size=12, color=self.t.muted, align="c")

    def carousel_cover(self, kicker, title, hint="Geser"):
        s = self._slide(self.deep)
        W, H = self.W, self.H
        k.text(s, 0.7, 1.0, W - 1.4, 0.4, kicker, size=14, bold=True, color=self.hi,
               caps=True, spacing=3)
        self.head(s, 0.7, 1.6, W - 1.4, 3.6, title, 54, color="lt1", line_spacing=1.02)
        k.text(s, 0.7, 6.25, 3, 0.45, hint, size=15, bold=True, color="lt1", caps=True,
               spacing=2)
        k.icon(s, self.t, "arrow-right", 2.05, 6.27, 0.42, self.hi)
        self.tag(s, dark_bg=True)

    def carousel_item(self, num, total, title, body, icon="lightbulb"):
        s = self._slide()
        W, H = self.W, self.H
        k.text(s, 0.7, 0.7, 3, 1.6, f"{num:02d}", size=96, color="accent1", font="+mj-lt",
               name="Nomor")
        self.t.icon_disc(s, icon, W - 1.7, 0.95, 1.0)
        self.head(s, 0.7, 2.6, W - 1.4, 1.5, title, 36, line_spacing=1.05)
        k.text(s, 0.7, 4.25, W - 1.4, 2.2, body, size=18, color=self.t.text, line_spacing=1.35)
        for i in range(total):
            d = 0.14
            k.oval(s, W / 2 - total * 0.14 + i * 0.28, 6.75, d, d,
                   "accent1" if i == num - 1 else self.t.grid, name="Indikator")
        self.tag(s)

    def price_list(self, title, rows, note=""):
        s = self._slide()
        W, H = self.W, self.H
        self.head(s, 0.7, 0.6, W - 1.4, 0.9, title, 34, align="c")
        y = 1.8
        step = (H - 1.6 - y - (0.5 if note else 0)) / len(rows)
        for name, desc, price in rows:
            k.text(s, 0.7, y, W - 3.4, 0.45, name, size=17, bold=True, color=self.t.primary)
            k.text(s, 0.7, y + 0.42, W - 3.4, 0.4, desc, size=12, color=self.t.muted)
            k.text(s, W - 2.7, y, 2.0, 0.45, price, size=17, bold=True, color=self.t.accent,
                   align="r")
            k.line(s, 0.7, y + step - 0.12, W - 0.7, y + step - 0.12, self.t.grid, 0.75,
                   name="Garis")
            y += step
        if note:
            k.text(s, 0.7, H - 1.45, W - 1.4, 0.4, note, size=12, italic=True,
                   color=self.t.muted, align="c")
        self.tag(s)

    def before_after(self, title, left="Sebelum", right="Sesudah"):
        s = self._slide()
        W, H = self.W, self.H
        self.head(s, 0.5, 0.5, W - 1, 0.8, title, 30, align="c")
        cw = (W - 1.0 - 0.25) / 2
        for i, lbl in enumerate((left, right)):
            x = 0.5 + i * (cw + 0.25)
            self.photo(s, x, 1.5, cw, H - 3.0, label="Foto")
            self.pill(s, x + cw / 2 - 0.9, H - 1.35, 1.8, 0.45, lbl,
                      self.deep if i else self.t.surface, "lt1" if i else self.t.primary,
                      size=12)
        self.tag(s)

    def giveaway(self, title, prize, steps, deadline):
        s = self._slide(self.deep)
        W, H = self.W, self.H
        k.text(s, 0.7, 0.75, W - 1.4, 0.4, "Giveaway", size=15, bold=True, color=self.hi,
               align="c", caps=True, spacing=4)
        self.head(s, 0.7, 1.2, W - 1.4, 1.6, title, 40, color="lt1", align="c", anchor="m")
        k.text(s, 0.7, 2.85, W - 1.4, 0.5, prize, size=18, color=self.t.divider_sub,
               align="c")
        y = 3.6
        for i, st in enumerate(steps, 1):
            c = k.oval(s, 1.3, y, 0.6, 0.6, None, line=self.hi, line_w=1.25,
                       name=f"Langkah {i}")
            k.text(s, 0, 0, 0, 0, str(i), size=16, bold=True, color=self.hi, align="c",
                   anchor="m", shape_obj=c)
            k.text(s, 2.15, y, W - 3.0, 0.6, st, size=17, color="lt1", anchor="m")
            y += 0.85
        self.pill(s, W / 2 - 1.9, H - 1.55, 3.8, 0.55, deadline, self.hi,
                  self.hi_ink, size=13)
        self.tag(s, dark_bg=True)

    def how_to_order(self, title, steps, contact):
        s = self._slide()
        W, H = self.W, self.H
        self.head(s, 0.7, 0.6, W - 1.4, 0.9, title, 34, align="c")
        y = 1.85
        for i, (ic, head, desc) in enumerate(steps, 1):
            self.t.icon_disc(s, ic, 0.8, y, 0.75)
            k.text(s, 1.8, y - 0.02, W - 2.6, 0.45, f"{i}. {head}", size=18, bold=True,
                   color=self.t.primary)
            k.text(s, 1.8, y + 0.42, W - 2.6, 0.45, desc, size=13, color=self.t.muted)
            y += 1.12
        self.pill(s, W / 2 - 2.0, H - 1.45, 4.0, 0.6, contact, self.deep,
                  "lt1" if not self.t.dark else "accent1", size=14)
        self.tag(s)

    def quote(self, text, author=""):
        s = self._slide(self.deep)
        W, H = self.W, self.H
        self.head(s, 0.9, 1.4, W - 1.8, 4.2, text, 40, color="lt1", align="c", anchor="m",
                  line_spacing=1.15, bold=False)
        if author:
            k.text(s, 0.9, 5.8, W - 1.8, 0.4, author, size=14, color=self.t.divider_sub,
                   align="c", caps=True, spacing=3)
        self.tag(s, dark_bg=True)

    def announcement(self, kicker, title, body, date_text):
        s = self._slide()
        W, H = self.W, self.H
        k.rect(s, 0.35, 0.35, W - 0.7, H - 0.7, None, line=self.t.grid, line_w=1.0,
               name="Bingkai")
        self.t.icon_disc(s, "megaphone", W / 2 - 0.55, 1.0, 1.1)
        k.text(s, 0.8, 2.45, W - 1.6, 0.4, kicker, size=14, bold=True, color=self.t.accent,
               align="c", caps=True, spacing=3)
        self.head(s, 0.8, 2.95, W - 1.6, 1.4, title, 40, align="c")
        k.text(s, 1.0, 4.45, W - 2.0, 1.4, body, size=17, color=self.t.text, align="c",
               line_spacing=1.35)
        k.text(s, 0.8, 6.0, W - 1.6, 0.4, date_text, size=15, bold=True, color=self.t.primary,
               align="c")
        self.tag(s, y=H - 1.0)

    def bundle(self, kicker, name, items, old, new):
        s = self._slide()
        W, H = self.W, self.H
        self.photo(s, 0, 0, W * 0.52, H)
        x = W * 0.52 + 0.4
        w = W - x - 0.45
        k.text(s, x, 0.9, w, 0.4, kicker, size=13, bold=True, color=self.t.accent,
               caps=True, spacing=3)
        self.head(s, x, 1.35, w, 1.6, name, 32, line_spacing=1.05)
        k.bullets(s, x, 3.1, w, 1.8, items, size=14, color=self.t.text,
                  bullet_color=self.t.accent, para_after=6)
        k.text(s, x, 5.05, w, 0.4, old, size=16, color=self.t.muted, name="Harga coret")
        k.text(s, x, 5.45, w, 0.8, new, size=34, bold=True, color=self.t.primary,
               font="+mj-lt")
        k.text(s, x, H - 0.62, w, 0.35, self.handle, size=12, color=self.t.muted)

    def faq(self, title, items):
        s = self._slide()
        W, H = self.W, self.H
        self.head(s, 0.7, 0.6, W - 1.4, 0.9, title, 34)
        y = 1.75
        step = (H - 1.4 - y) / len(items)
        for q, a in items:
            k.text(s, 0.7, y, W - 1.4, 0.45, "Q: " + q, size=16, bold=True,
                   color=self.t.primary)
            k.text(s, 0.7, y + 0.45, W - 1.4, step - 0.55, a, size=14, color=self.t.text,
                   line_spacing=1.2)
            y += step
        self.tag(s)

    def thanks(self, title, sub):
        s = self._slide(self.deep)
        W, H = self.W, self.H
        self.head(s, 0.7, 2.4, W - 1.4, 1.6, title, 54, color="lt1", align="c")
        k.text(s, 0.9, 4.1, W - 1.8, 1.0, sub, size=18, color=self.t.divider_sub, align="c",
               line_spacing=1.3)
        self.pill(s, W / 2 - 1.6, 5.5, 3.2, 0.6, "Ikuti " + self.handle, self.hi,
                  self.hi_ink, size=13)

    # ------------------------------------------------------------ story (9:16)
    def story_promo(self, kicker, big, sub, cta):
        s = self._slide(self.deep)
        W, H = self.W, self.H
        self.photo(s, 0.5, 0.9, W - 1.0, 4.6)
        k.text(s, 0.5, 5.9, W - 1.0, 0.4, kicker, size=14, bold=True, color=self.hi,
               caps=True, spacing=3, align="c")
        self.head(s, 0.4, 6.35, W - 0.8, 1.6, big, 84, color="lt1", align="c", bold=True)
        k.text(s, 0.5, 8.0, W - 1.0, 0.6, sub, size=18, color=self.t.divider_sub, align="c")
        self.pill(s, W / 2 - 1.5, 8.9, 3.0, 0.6, cta, self.hi,
                  self.hi_ink)
        self.tag(s, dark_bg=True, y=H - 0.75)

    def story_product(self, kicker, name, price):
        s = self._slide()
        W, H = self.W, self.H
        self.photo(s, 0, 0, W, H * 0.66)
        k.text(s, 0.5, H * 0.66 + 0.4, W - 1, 0.4, kicker, size=13, bold=True,
               color=self.t.accent, caps=True, spacing=3)
        self.head(s, 0.5, H * 0.66 + 0.8, W - 1, 1.2, name, 34)
        k.text(s, 0.5, H * 0.66 + 2.0, W - 1, 0.6, price, size=26, bold=True,
               color=self.t.primary, font="+mj-lt")
        self.tag(s, y=H - 0.75)

    def story_question(self, title, prompt):
        s = self._slide(self.t.surface if not self.t.dark else "dk2")
        W, H = self.W, self.H
        self.head(s, 0.6, 1.6, W - 1.2, 2.2, title, 40, align="c", anchor="b")
        box = k.rrect(s, 0.7, 4.3, W - 1.4, 2.4, "lt1" if not self.t.dark else "dk1",
                      radius=0.3, name="Area stiker pertanyaan", line=self.t.grid)
        k.text(s, 0.9, 4.45, W - 1.8, 0.5, prompt, size=15, bold=True, color=self.t.muted,
               align="c")
        k.text(s, 0.9, 5.4, W - 1.8, 0.6, "Tempel stiker Pertanyaan / Polling di sini",
               size=12, color=self.t.muted, align="c", italic=True)
        self.tag(s, y=H - 0.75)

    def story_testimonial(self, quote, name):
        s = self._slide(self.deep)
        W, H = self.W, self.H
        self.photo(s, 0.6, 1.0, W - 1.2, 4.4, label="Tangkapan layar ulasan")
        k.icon(s, self.t, "quote", W / 2 - 0.35, 5.8, 0.7, self.hi)
        self.head(s, 0.6, 6.6, W - 1.2, 2.0, quote, 24, color="lt1", align="c",
                  line_spacing=1.2, bold=False)
        k.text(s, 0.6, 8.7, W - 1.2, 0.4, name, size=14, bold=True, color=self.hi,
               align="c", caps=True, spacing=2)
        self.tag(s, dark_bg=True, y=H - 0.75)

    def story_countdown(self, kicker, title, date_text):
        s = self._slide()
        W, H = self.W, self.H
        k.text(s, 0.6, 2.0, W - 1.2, 0.4, kicker, size=14, bold=True, color=self.t.accent,
               caps=True, spacing=3, align="c")
        self.head(s, 0.6, 2.5, W - 1.2, 2.2, title, 48, align="c")
        for i, lbl in enumerate(("Hari", "Jam", "Menit")):
            x = 0.7 + i * ((W - 1.4) / 3)
            w = (W - 1.4) / 3 - 0.2
            box = self.t.card(s, x, 5.0, w, 1.6, name=f"Kotak {lbl}")
            k.text(s, x, 5.05, w, 1.0, "00", size=40, bold=True, color=self.t.primary,
                   align="c", font="+mj-lt")
            k.text(s, x, 6.05, w, 0.4, lbl, size=12, color=self.t.muted, align="c",
                   caps=True, spacing=2)
        k.text(s, 0.6, 7.1, W - 1.2, 0.5, date_text, size=16, bold=True,
               color=self.t.primary, align="c")
        k.text(s, 0.6, 7.6, W - 1.2, 0.5, "Tempel stiker Hitung Mundur Instagram di atas",
               size=11, italic=True, color=self.t.muted, align="c")
        self.tag(s, y=H - 0.75)

    def story_link(self, title, sub, cta):
        s = self._slide(self.deep)
        W, H = self.W, self.H
        self.head(s, 0.6, 2.6, W - 1.2, 2.4, title, 46, color="lt1", align="c", anchor="b")
        k.text(s, 0.6, 5.2, W - 1.2, 1.0, sub, size=18, color=self.t.divider_sub,
               align="c", line_spacing=1.3)
        k.icon(s, self.t, "arrow-down", W / 2 - 0.3, 6.6, 0.6, self.hi)
        self.pill(s, W / 2 - 1.7, 7.5, 3.4, 0.65, cta, self.hi,
                  self.hi_ink)
        self.tag(s, dark_bg=True, y=H - 0.75)
