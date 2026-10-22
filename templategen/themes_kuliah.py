"""Lima tema untuk presentasi tugas kuliah: lebih berwarna dan santai."""
from __future__ import annotations

from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.enum.shapes import MSO_SHAPE

from . import core as k
from .themes import Theme


def _rot(shp, deg):
    shp.rotation = deg
    return shp


# ===================================================================== CERIA
class Ceria(Theme):
    key = "ceria"
    name = "Ceria"
    label = "Ceria"
    colors = dict(dk1="1D2B4F", lt1="FFFFFF", dk2="1D3557", lt2="FFF4D6",
                  accent1="F4A300", accent2="2A9D8F", accent3="E76F51", accent4="5C6784",
                  accent5="4F7CFF", accent6="FFE3A3", hlink="4F7CFF", folHlink="5C6784")
    surface = "lt2"
    grid = "accent6"
    card_radius = 0.22
    on_accent = "dk1"
    series = ("accent5", "accent1", "accent2", "accent3")
    FILLS = ("lt2", "accent2+82", "accent3+82", "accent5+85")
    INK = ("accent1-15", "accent2", "accent3", "accent5")
    neutral_panel = True

    def card(self, slide, x, y, w, h, i=0, fill=None, name="Kartu"):
        return k.rrect(slide, x, y, w, h, fill or self.FILLS[i % 4], radius=self.card_radius,
                       name=name)

    def badge(self, slide, x, y, d, label, i=0, fill=None, color=None, size=None):
        return super().badge(slide, x, y, d, label, i, fill or self.INK[i % 4],
                             color or "lt1", size)

    def icon_disc(self, slide, name, x, y, d, i=0, fill=None, color=None):
        k.rrect(slide, x, y, d, d, fill or "lt1", radius=d * 0.3, name="Latar ikon")
        pad = d * 0.24
        k.icon(slide, self, name, x + pad, y + pad, d - 2 * pad, color or self.INK[i % 4])

    def _confetti(self, slide, spots):
        for (x, y, s, c, r) in spots:
            _rot(k.rrect(slide, x, y, s, s, c, radius=s * 0.28, name="Dekorasi"), r)

    def frame(self, slide, title, kicker, page, meta):
        self._confetti(slide, [(12.15, 0.35, 0.55, "accent1", 18), (12.75, 1.05, 0.3, "accent2", -12)])
        if kicker:
            k.text(slide, 0.7, 0.45, 9, 0.35, kicker, size=12, bold=True, color="accent2",
                   caps=True, spacing=1.5, name="Kicker")
        self.head(slide, 0.7, 0.75, 10.8, 0.85, title, name="Judul slide")
        k.text(slide, 0.7, 6.92, 8, 0.3, meta, size=10, color=self.muted, name="Footer")
        self.badge(slide, 12.18, 6.82, 0.45, f"{page:02d}", size=10, fill="dk2")
        return 1.95

    def cover(self, slide, d):
        k.rect(slide, 7.9, 0, 5.433, 7.5, "lt2", name="Panel")
        self._confetti(slide, [(8.6, 0.9, 1.6, "accent1", 14), (10.9, 1.7, 1.1, "accent2", -10),
                               (9.4, 3.6, 2.2, "accent5", 8), (11.9, 4.6, 0.9, "accent3", 22),
                               (8.4, 5.9, 0.7, "accent3", -18), (12.2, 0.4, 0.5, "accent5", 30)])
        k.icon(slide, self, "book-open", 9.95, 4.15, 1.1, "lt1")
        self.logo_slot(slide, 0.8, 0.7, 0.85)
        k.text(slide, 1.85, 0.8, 5, 0.7, [[dict(text=d["kampus"], bold=True)], d["fakultas"]],
               size=12, color="accent4")
        pill = k.rrect(slide, 0.8, 2.0, 3.6, 0.44, "accent1", radius=0.22, name="Label")
        k.text(slide, 0, 0, 0, 0, d["jenis"], size=12, bold=True, color="dk1", align="c",
               anchor="m", shape_obj=pill, caps=True, spacing=1)
        self.head(slide, 0.8, 2.65, 6.8, 2.3, d["judul"], size=40, line_spacing=1.0)
        k.text(slide, 0.8, 5.15, 6.8, 1.5,
               [[dict(text=d["nama"], bold=True, size=18, color="dk2")], d["nim"],
                d["pembimbing"]], size=13, color="accent4", line_spacing=1.2)

    def divider(self, slide, num, title, subtitle):
        k.rect(slide, 0, 0, 13.333, 7.5, "lt2", name="Latar")
        self._confetti(slide, [(9.0, 1.2, 3.4, "accent1", 12), (11.6, 4.4, 1.3, "accent2", -14),
                               (8.4, 4.9, 0.9, "accent3", 20)])
        k.text(slide, 9.0, 1.2, 3.4, 3.4, num, size=110, bold=True, color="dk1", align="c",
               anchor="m", font="+mj-lt", name="Nomor bagian")
        k.text(slide, 0.8, 2.7, 6, 0.4, "Bagian " + num, size=14, bold=True, color="accent2",
               caps=True, spacing=2)
        self.head(slide, 0.8, 3.15, 7.2, 1.5, title, size=46, line_spacing=1.0)
        k.text(slide, 0.8, 4.75, 6.5, 1.0, subtitle, size=17, color="accent4")

    def closing(self, slide, d):
        self._confetti(slide, [(0.7, 0.8, 1.0, "accent1", 14), (11.4, 0.9, 1.3, "accent5", -10),
                               (1.6, 5.4, 0.7, "accent2", 20), (11.9, 5.3, 0.9, "accent3", -16)])
        self.head(slide, 1.5, 2.2, 10.333, 1.4, d["judul"], size=66, align="c")
        k.text(slide, 2.0, 3.6, 9.333, 0.6, d["sub"], size=18, color="accent4", align="c")
        x0 = 6.67 - 4.65
        for i, (ic, label) in enumerate(d["kontak"]):
            x = x0 + i * 3.1
            pill = k.rrect(slide, x, 4.75, 2.9, 0.6, self.FILLS[i % 4], radius=0.3, name="Kontak")
            k.icon(slide, self, ic, x + 0.22, 4.89, 0.32, self.INK[i % 4])
            k.text(slide, x + 0.65, 4.75, 2.2, 0.6, label, size=12, color="dk1", anchor="m")


# ===================================================================== NEO BRUTAL
class NeoBrutal(Theme):
    key = "neo-brutal"
    name = "Neo Brutal"
    label = "Neo Brutal"
    head_font = "Arial"
    body_font = "Arial"
    colors = dict(dk1="111111", lt1="FFFFFF", dk2="111111", lt2="F4F1FF",
                  accent1="7C5CFF", accent2="FFD43B", accent3="3DDC97", accent4="555555",
                  accent5="FF6B6B", accent6="DDDDDD", hlink="7C5CFF", folHlink="555555")
    primary = "dk1"
    surface = "lt1"
    grid = "accent6"
    card_radius = 0.12
    series = ("accent1", "accent2", "accent3", "accent5")
    FILLS = ("accent2+40", "accent3+55", "accent1+70", "accent5+60")
    neutral_panel = True

    def _block(self, slide, x, y, w, h, fill, name="Kartu", off=0.09, radius=None):
        r = self.card_radius if radius is None else radius
        k.rrect(slide, x + off, y + off, w, h, "dk1", radius=r, name="Bayangan")
        return k.rrect(slide, x, y, w, h, fill, radius=r, name=name, line="dk1", line_w=2.0)

    def card(self, slide, x, y, w, h, i=0, fill=None, name="Kartu"):
        return self._block(slide, x, y, w - 0.09, h - 0.09, fill or self.FILLS[i % 4], name)

    def badge(self, slide, x, y, d, label, i=0, fill=None, color=None, size=None):
        c = k.oval(slide, x, y, d, d, fill or "lt1", line="dk1", line_w=2.0,
                   name=f"Penanda {label}")
        k.text(slide, x, y, d, d, label, size=size or d * 24, color=color or "dk1", bold=True,
               align="c", anchor="m", shape_obj=c)
        return c

    def icon_disc(self, slide, name, x, y, d, i=0, fill=None, color=None):
        k.oval(slide, x, y, d, d, fill or "lt1", line="dk1", line_w=2.0, name="Latar ikon")
        pad = d * 0.24
        k.icon(slide, self, name, x + pad, y + pad, d - 2 * pad, color or "dk1")

    def frame(self, slide, title, kicker, page, meta):
        if kicker:
            w = 0.4 + len(kicker) * 0.12
            sh = self._block(slide, 0.7, 0.4, w, 0.4, "accent2", name="Kicker", off=0.05,
                             radius=0.08)
            k.text(slide, 0, 0, 0, 0, kicker, size=11, bold=True, color="dk1", align="c",
                   anchor="m", shape_obj=sh, caps=True)
        self.head(slide, 0.7, 0.95, 10.8, 0.85, title, name="Judul slide")
        k.oval(slide, 12.0, 0.45, 0.6, 0.6, "accent3", line="dk1", line_w=2.0, name="Dekorasi")
        k.text(slide, 0.7, 6.92, 8, 0.3, meta, size=10, color=self.muted, name="Footer")
        sh = self._block(slide, 11.95, 6.82, 0.65, 0.4, "lt1", name="Nomor slide", off=0.05,
                         radius=0.08)
        k.text(slide, 0, 0, 0, 0, f"{page:02d}", size=10, bold=True, color="dk1", align="c",
               anchor="m", shape_obj=sh)
        return 2.1

    def cover(self, slide, d):
        k.rect(slide, 0, 0, 13.333, 7.5, "lt2", name="Latar")
        self._block(slide, 8.2, 0.9, 4.3, 4.3, "accent1", name="Blok", radius=0.3, off=0.15)
        k.icon(slide, self, "presentation", 9.35, 2.05, 2.0, "lt1")
        self._block(slide, 10.6, 4.6, 2.2, 1.0, "accent2", name="Stiker", off=0.08)
        k.text(slide, 10.6, 4.6, 2.11, 0.92, "TUGAS\nKELOMPOK", size=14, bold=True,
               color="dk1", align="c", anchor="m", line_spacing=0.95)
        k.oval(slide, 7.7, 5.4, 1.0, 1.0, "accent3", line="dk1", line_w=2.0, name="Dekorasi")
        self.logo_slot(slide, 0.8, 0.7, 0.85, fill="dk1", color="dk1")
        k.text(slide, 1.85, 0.8, 5, 0.7, [[dict(text=d["kampus"], bold=True)], d["fakultas"]],
               size=12, color="dk1")
        k.text(slide, 0.8, 2.05, 6, 0.4, d["jenis"], size=13, bold=True, color="accent1",
               caps=True)
        self.head(slide, 0.8, 2.5, 6.9, 2.5, d["judul"], size=40, line_spacing=1.0)
        card = self._block(slide, 0.8, 5.2, 5.8, 1.4, "lt1", name="Kartu identitas")
        k.text(slide, 1.1, 5.33, 5.3, 1.2,
               [[dict(text=d["nama"], bold=True, size=17)], d["nim"], d["pembimbing"]],
               size=12, color="dk1", line_spacing=1.15)

    def divider(self, slide, num, title, subtitle):
        k.rect(slide, 0, 0, 13.333, 7.5, "accent2", name="Latar")
        self._block(slide, 8.3, 1.3, 3.8, 3.8, "lt1", name="Blok", radius=0.3, off=0.15)
        k.text(slide, 8.3, 1.3, 3.8, 3.8, num, size=120, bold=True, color="dk1", align="c",
               anchor="m", name="Nomor bagian")
        k.oval(slide, 11.7, 4.8, 0.9, 0.9, "accent5", line="dk1", line_w=2.0, name="Dekorasi")
        k.text(slide, 0.8, 2.7, 6, 0.4, "Bagian " + num, size=14, bold=True, color="dk1",
               caps=True)
        self.head(slide, 0.8, 3.15, 7.2, 1.5, title, size=48, line_spacing=1.0)
        k.text(slide, 0.8, 4.8, 6.5, 1.0, subtitle, size=17, color="dk1")

    def closing(self, slide, d):
        k.rect(slide, 0, 0, 13.333, 7.5, "accent1", name="Latar")
        self._block(slide, 2.4, 1.5, 8.5, 2.4, "lt1", name="Blok", radius=0.25, off=0.15)
        self.head(slide, 2.4, 1.6, 8.4, 1.4, d["judul"], size=62, align="c", anchor="m")
        k.text(slide, 2.4, 2.95, 8.4, 0.6, d["sub"], size=17, color="accent4", align="c")
        x0 = 6.67 - 4.65
        for i, (ic, label) in enumerate(d["kontak"]):
            x = x0 + i * 3.1
            self._block(slide, x, 4.8, 2.9, 0.6, self.FILLS[i % 4], name="Kontak", off=0.06)
            k.icon(slide, self, ic, x + 0.22, 4.94, 0.32, "dk1")
            k.text(slide, x + 0.65, 4.8, 2.2, 0.6, label, size=12, color="dk1", anchor="m")


# ===================================================================== ALAM
class Alam(Theme):
    key = "alam"
    name = "Alam Hijau"
    label = "Alam"
    head_font = "Cambria"
    body_font = "Calibri"
    colors = dict(dk1="243B2E", lt1="FFFFFF", dk2="2F4F3A", lt2="EEF3EC",
                  accent1="5E8B67", accent2="C8553D", accent3="D9A441", accent4="667A6C",
                  accent5="8FB996", accent6="D5E2D3", hlink="5E8B67", folHlink="667A6C")
    surface = "lt2"
    grid = "accent6"
    card_radius = 0.2
    series = ("dk2", "accent5", "accent2", "accent3")

    def _leaf(self, slide, x, y, w, h, color, rot):
        return _rot(k.oval(slide, x, y, w, h, color, name="Daun"), rot)

    def badge(self, slide, x, y, d, label, i=0, fill=None, color=None, size=None):
        return super().badge(slide, x, y, d, label, i, fill or "dk2", color, size)

    def frame(self, slide, title, kicker, page, meta):
        self._leaf(slide, 11.9, -0.4, 0.9, 2.0, "accent5+40", 35)
        self._leaf(slide, 12.6, 0.1, 0.6, 1.4, "accent1+20", -20)
        if kicker:
            k.text(slide, 0.7, 0.45, 9, 0.35, kicker, size=12, bold=True, color="accent2",
                   caps=True, spacing=1.5, name="Kicker")
        self.head(slide, 0.7, 0.75, 10.8, 0.85, title, name="Judul slide")
        k.text(slide, 0.7, 6.92, 8, 0.3, meta, size=10, color=self.muted, name="Footer")
        k.text(slide, 11.63, 6.92, 1.0, 0.3, f"{page:02d}", size=11, bold=True, color="accent1",
               align="r", font="+mj-lt", name="Nomor slide")
        return 1.95

    def cover(self, slide, d):
        k.rect(slide, 7.6, 0, 5.733, 7.5, "dk2", name="Panel")
        for (x, y, w, h, c, r) in [(8.4, 0.6, 1.6, 3.8, "accent1", 25), (10.3, 0.2, 1.3, 3.2,
                                                                     "accent5", -15),
                                   (11.4, 2.9, 1.5, 3.6, "accent1+20", 30),
                                   (9.0, 3.8, 1.2, 3.0, "accent5+30", -25),
                                   (8.0, 5.6, 0.8, 1.8, "accent3", 40)]:
            self._leaf(slide, x, y, w, h, c, r)
        k.oval(slide, 10.7, 4.9, 0.6, 0.6, "accent2", name="Dekorasi")
        self.logo_slot(slide, 0.8, 0.7, 0.85)
        k.text(slide, 1.85, 0.8, 5, 0.7, [[dict(text=d["kampus"], bold=True)], d["fakultas"]],
               size=12, color="accent4")
        k.text(slide, 0.8, 2.1, 6, 0.4, d["jenis"], size=13, bold=True, color="accent2",
               caps=True, spacing=2)
        self.head(slide, 0.8, 2.55, 6.5, 2.5, d["judul"], size=38, line_spacing=1.05)
        k.text(slide, 0.8, 5.2, 6.4, 1.5,
               [[dict(text=d["nama"], bold=True, size=18, color="dk2")], d["nim"],
                d["pembimbing"]], size=13, color="accent4", line_spacing=1.2)

    def divider(self, slide, num, title, subtitle):
        k.rect(slide, 0, 0, 13.333, 7.5, "dk2", name="Latar")
        self._leaf(slide, 9.6, 0.6, 2.2, 5.0, "accent1", 25)
        self._leaf(slide, 11.2, 2.4, 1.6, 3.8, "accent5", -20)
        self._leaf(slide, 9.0, 4.6, 1.0, 2.4, "accent3", 40)
        k.text(slide, 0.8, 1.7, 4, 1.8, num, size=110, color="accent3", font="+mj-lt",
               name="Nomor bagian")
        self.head(slide, 0.8, 3.7, 8, 1.3, title, size=46, color="lt1")
        k.text(slide, 0.8, 4.95, 7.5, 1.0, subtitle, size=17, color="accent6")

    def closing(self, slide, d):
        k.rect(slide, 0, 0, 13.333, 7.5, "dk2", name="Latar")
        self._leaf(slide, -0.4, -0.6, 1.8, 4.2, "accent1", 30)
        self._leaf(slide, 1.0, -0.8, 1.2, 2.8, "accent5", -15)
        self._leaf(slide, 11.6, 4.2, 1.8, 4.2, "accent1", -30)
        self._leaf(slide, 11.0, 5.4, 1.0, 2.4, "accent3", 20)
        self.head(slide, 1.5, 2.3, 10.333, 1.4, d["judul"], size=64, color="lt1", align="c")
        k.text(slide, 2.0, 3.7, 9.333, 0.6, d["sub"], size=18, color="accent6", align="c")
        x0 = 6.67 - 4.6
        for i, (ic, label) in enumerate(d["kontak"]):
            x = x0 + i * 3.1
            k.icon(slide, self, ic, x, 5.0, 0.36, "accent3")
            k.text(slide, x + 0.5, 4.97, 2.6, 0.45, label, size=13, color="lt1", anchor="m")


# ===================================================================== TEKNO
class Tekno(Theme):
    key = "tekno"
    name = "Tekno Neon"
    label = "Tekno"
    head_font = "Arial"
    body_font = "Calibri"
    colors = dict(dk1="0B1020", lt1="EAF2FF", dk2="141B33", lt2="1E2747",
                  accent1="22D3EE", accent2="8B5CF6", accent3="F472B6", accent4="94A3B8",
                  accent5="34D399", accent6="2A355E", hlink="22D3EE", folHlink="94A3B8")
    dark = True
    bg = "dk1"
    surface = "dk2"
    text = "lt1"
    primary = "lt1"
    on_accent = "dk1"
    grid = "accent6"
    card_radius = 0.14
    series = ("accent1", "accent2", "accent3", "accent5")

    def card(self, slide, x, y, w, h, i=0, fill=None, name="Kartu"):
        return k.rrect(slide, x, y, w, h, fill or "dk2", radius=self.card_radius, name=name,
                       line="accent6", line_w=1.0)

    def icon_disc(self, slide, name, x, y, d, i=0, fill=None, color=None):
        c = self.series[i % 4]
        k.rrect(slide, x, y, d, d, fill or "lt2", radius=d * 0.25, name="Latar ikon")
        pad = d * 0.24
        k.icon(slide, self, name, x + pad, y + pad, d - 2 * pad, color or c)

    def _grid(self, slide, x, y, cols, rows, gap=0.32):
        for r in range(rows):
            for c in range(cols):
                k.rect(slide, x + c * gap, y + r * gap, 0.04, 0.04, "accent6", name="Grid")

    def frame(self, slide, title, kicker, page, meta):
        self._grid(slide, 11.3, 0.4, 5, 3)
        if kicker:
            k.text(slide, 0.7, 0.45, 9, 0.35, "// " + kicker, size=12, bold=True,
                   color="accent1", name="Kicker")
        self.head(slide, 0.7, 0.75, 10.4, 0.85, title, name="Judul slide")
        k.text(slide, 0.7, 6.92, 8, 0.3, meta, size=10, color=self.muted, name="Footer")
        k.text(slide, 10.9, 6.92, 1.73, 0.3, f"[ {page:02d} ]", size=10, bold=True,
               color="accent1", align="r", name="Nomor slide")
        return 1.95

    def cover(self, slide, d):
        self._grid(slide, 7.6, 0.6, 17, 20, gap=0.33)
        k.oval(slide, 8.6, 1.2, 4.2, 4.2, "accent2", name="Cahaya", transparency=55)
        k.oval(slide, 10.2, 3.0, 2.6, 2.6, "accent1", name="Cahaya", transparency=45)
        k.rrect(slide, 8.9, 2.3, 3.0, 2.0, "dk2", radius=0.15, line="accent1", line_w=1.5,
                name="Jendela")
        k.icon(slide, self, "code", 9.85, 2.75, 1.1, "accent1")
        self.logo_slot(slide, 0.8, 0.7, 0.85, fill="accent4", color="accent4")
        k.text(slide, 1.85, 0.8, 5, 0.7, [[dict(text=d["kampus"], bold=True, color="lt1")],
                                          d["fakultas"]], size=12, color="accent4")
        k.text(slide, 0.8, 2.1, 6, 0.4, "> " + d["jenis"], size=13, bold=True,
               color="accent1")
        self.head(slide, 0.8, 2.55, 6.6, 2.5, d["judul"], size=38, line_spacing=1.02)
        k.text(slide, 0.8, 5.2, 6.4, 1.5,
               [[dict(text=d["nama"], bold=True, size=18, color="lt1")], d["nim"],
                d["pembimbing"]], size=13, color="accent4", line_spacing=1.2)

    def divider(self, slide, num, title, subtitle):
        self._grid(slide, 0.8, 0.6, 38, 2)
        k.oval(slide, 8.8, 1.4, 4.0, 4.0, "accent2", name="Cahaya", transparency=60)
        k.text(slide, 8.8, 1.4, 4.0, 4.0, num, size=120, bold=True, color="accent1",
               align="c", anchor="m", name="Nomor bagian")
        k.text(slide, 0.8, 2.7, 6, 0.4, f"// bagian_{num}", size=14, bold=True,
               color="accent3")
        self.head(slide, 0.8, 3.15, 7.4, 1.5, title, size=46, line_spacing=1.0)
        k.text(slide, 0.8, 4.75, 6.6, 1.0, subtitle, size=17, color="accent4")

    def closing(self, slide, d):
        self._grid(slide, 0.8, 0.6, 38, 2)
        self._grid(slide, 0.8, 6.5, 38, 2)
        k.oval(slide, 4.9, 1.4, 3.6, 3.6, "accent2", name="Cahaya", transparency=65)
        self.head(slide, 1.5, 2.2, 10.333, 1.4, d["judul"], size=64, align="c")
        k.text(slide, 2.0, 3.6, 9.333, 0.6, d["sub"], size=18, color="accent4", align="c")
        x0 = 6.67 - 4.6
        for i, (ic, label) in enumerate(d["kontak"]):
            x = x0 + i * 3.1
            k.icon(slide, self, ic, x, 5.0, 0.36, self.series[i % 4])
            k.text(slide, x + 0.5, 4.97, 2.6, 0.45, label, size=13, color="lt1", anchor="m")


# ===================================================================== RETRO
class Retro(Theme):
    key = "retro"
    name = "Retro 70an"
    label = "Retro"
    head_font = "Cambria"
    body_font = "Calibri"
    colors = dict(dk1="3B2A20", lt1="FFFFFF", dk2="5C3D2E", lt2="FCEBDD",
                  accent1="E07A1F", accent2="1B998B", accent3="E9B44C", accent4="7D6457",
                  accent5="C8553D", accent6="F3D2B8", hlink="1B998B", folHlink="7D6457")
    surface = "lt2"
    grid = "accent6"
    card_radius = 0.3
    series = ("accent1", "accent2", "accent3", "accent5")

    def _rainbow(self, slide, cx, cy, r, colors, band=0.38, hole="lt1", mask=None):
        """Pelangi retro: lingkaran konsentris; bagian bawah ditutup `mask`
        (x, y, w, h, warna) atau berada di luar slide."""
        for i, c in enumerate(colors + [hole]):
            rr = r - i * band
            k.oval(slide, cx - rr, cy - rr, 2 * rr, 2 * rr, c, name="Pelangi retro")
        if mask:
            k.rect(slide, *mask[:4], mask[4], name="Penutup pelangi")

    def frame(self, slide, title, kicker, page, meta):
        self._rainbow(slide, 12.55, 1.25, 1.0, ["accent1", "accent3", "accent2"], band=0.25,
                      mask=(11.4, 1.25, 2.0, 1.2, "lt1"))
        if kicker:
            k.text(slide, 0.7, 0.45, 9, 0.35, kicker, size=12, bold=True, color="accent5",
                   caps=True, spacing=2, name="Kicker")
        self.head(slide, 0.7, 0.75, 10.4, 0.85, title, name="Judul slide")
        k.text(slide, 0.7, 6.92, 8, 0.3, meta, size=10, color=self.muted, name="Footer")
        self.badge(slide, 12.18, 6.82, 0.45, f"{page:02d}", size=10, fill="dk2")
        return 1.95

    def cover(self, slide, d):
        self._rainbow(slide, 10.3, 5.9, 3.0, ["accent5", "accent1", "accent3", "accent2"],
                      band=0.55)
        k.rect(slide, 0, 5.9, 13.333, 1.6, "lt2", name="Lantai")
        k.oval(slide, 9.75, 1.2, 1.1, 1.1, "accent3", name="Matahari")
        self.logo_slot(slide, 0.8, 0.7, 0.85)
        k.text(slide, 1.85, 0.8, 5, 0.7, [[dict(text=d["kampus"], bold=True)], d["fakultas"]],
               size=12, color="accent4")
        k.text(slide, 0.8, 1.95, 6, 0.4, d["jenis"], size=13, bold=True, color="accent5",
               caps=True, spacing=2)
        self.head(slide, 0.8, 2.4, 6.6, 2.5, d["judul"], size=38, line_spacing=1.02)
        k.text(slide, 0.8, 6.05, 7.5, 1.3,
               [[dict(text=d["nama"], bold=True, size=17, color="dk2")],
                d["nim"] + "  ·  " + d["pembimbing"]], size=12, color="accent4",
               line_spacing=1.2)

    def divider(self, slide, num, title, subtitle):
        k.rect(slide, 0, 0, 13.333, 7.5, "dk2", name="Latar")
        self._rainbow(slide, 10.4, 7.5, 3.6, ["accent5", "accent1", "accent3", "accent2"],
                      band=0.6, hole="dk2")
        k.text(slide, 0.8, 1.6, 4, 1.8, num, size=110, color="accent3", font="+mj-lt",
               bold=True, name="Nomor bagian")
        self.head(slide, 0.8, 3.65, 7.4, 1.3, title, size=46, color="lt1")
        k.text(slide, 0.8, 4.9, 6.6, 1.0, subtitle, size=17, color="accent6")

    def closing(self, slide, d):
        k.rect(slide, 0, 0, 13.333, 7.5, "dk2", name="Latar")
        self._rainbow(slide, 6.67, 7.5, 2.6, ["accent5", "accent1", "accent3", "accent2"],
                      band=0.45, hole="dk2")
        self.head(slide, 1.5, 1.2, 10.333, 1.4, d["judul"], size=64, color="lt1", align="c")
        k.text(slide, 2.0, 2.6, 9.333, 0.6, d["sub"], size=18, color="accent6", align="c")
        x0 = 6.67 - 4.6
        for i, (ic, label) in enumerate(d["kontak"]):
            x = x0 + i * 3.1
            k.icon(slide, self, ic, x, 3.55, 0.36, "accent3")
            k.text(slide, x + 0.5, 3.52, 2.6, 0.45, label, size=13, color="lt1", anchor="m")


THEMES = [Ceria(), NeoBrutal(), Alam(), Tekno(), Retro()]
