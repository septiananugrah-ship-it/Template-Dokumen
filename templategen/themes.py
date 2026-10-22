"""Lima tema desain. Tiap tema punya palet, font, gaya kartu dan dekorasi
sendiri untuk sampul, pembatas bagian, bingkai slide isi, dan penutup."""
from __future__ import annotations

from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.enum.shapes import MSO_SHAPE

from . import core as k


class Theme:
    key = "base"
    name = "Base"
    label = "Base"
    head_font = "Calibri"
    body_font = "Calibri"
    colors: dict = {}
    # peran semantik -> spesifikasi warna
    bg = "lt1"
    surface = "lt2"
    text = "dk1"
    muted = "accent4"
    primary = "dk2"
    accent = "accent1"
    accent_b = "accent2"
    accent_c = "accent3"
    on_accent = "lt1"
    grid = "lt2-10"
    title_size = 34
    title_caps = False
    card_radius = 0.18
    series = ("accent1", "accent2", "accent3", "accent5")
    dark = False
    cover_bg = None      # None = sama dengan bg
    divider_bg = None
    closing_bg = None

    # ------------------------------------------------------------ util
    def head(self, slide, x, y, w, h, content, size=None, color=None, **kw):
        kw.setdefault("font", "+mj-lt")
        kw.setdefault("bold", True)
        return k.text(slide, x, y, w, h, content, size=size or self.title_size,
                      color=color or self.primary, **kw)

    def body(self, slide, x, y, w, h, content, size=16, color=None, **kw):
        return k.text(slide, x, y, w, h, content, size=size, color=color or self.text, **kw)

    def card(self, slide, x, y, w, h, i=0, fill=None, name="Kartu"):
        shp = k.rrect(slide, x, y, w, h, fill or self.surface, radius=self.card_radius, name=name)
        return shp

    def card_fill(self, i):
        return self.surface

    def badge(self, slide, x, y, d, label, i=0, fill=None, color=None, size=None):
        """Lingkaran berisi angka/teks — motif penanda yang dipakai berulang."""
        c = k.oval(slide, x, y, d, d, fill or self.accent, name=f"Penanda {label}")
        k.text(slide, x, y, d, d, label, size=size or d * 26, color=color or self.on_accent,
               bold=True, align="c", anchor="m", font="+mj-lt", shape_obj=c)
        return c

    def icon_disc(self, slide, name, x, y, d, i=0, fill=None, color=None):
        k.oval(slide, x, y, d, d, fill or (self.accent + "+80"), name="Latar ikon")
        pad = d * 0.25
        k.icon(slide, self, name, x + pad, y + pad, d - 2 * pad, color or self.accent)

    # ------------------------------------------------------------ bingkai
    def frame(self, slide, title, kicker, page, meta):
        """Judul slide isi + footer. Mengembalikan y awal area konten."""
        if kicker:
            k.text(slide, 0.7, 0.45, 9, 0.35, kicker, size=12, bold=True, color=self.accent,
                   spacing=2, caps=True, name="Kicker")
        self.head(slide, 0.7, 0.75, 10.5, 0.85, title, anchor="t", name="Judul slide")
        self.footer(slide, page, meta)
        return 1.95

    def footer(self, slide, page, meta):
        k.text(slide, 0.7, 6.92, 8, 0.3, meta, size=10, color=self.muted, name="Footer")
        k.text(slide, 11.63, 6.92, 1.0, 0.3, f"{page:02d}", size=10, bold=True, color=self.muted,
               align="r", name="Nomor slide")

    # ------------------------------------------------------------ halaman khusus
    def cover(self, slide, d):
        raise NotImplementedError

    def divider(self, slide, num, title, subtitle):
        raise NotImplementedError

    def closing(self, slide, d):
        raise NotImplementedError

    def logo_slot(self, slide, x, y, d, fill=None, color=None, label="LOGO"):
        c = k.oval(slide, x, y, d, d, fill=None, line=fill or self.muted, line_w=1.25,
                   dash=MSO_LINE_DASH_STYLE.DASH, name="Tempat logo (ganti dengan logo kampus)")
        k.text(slide, x, y, d, d, label, size=9, bold=True, color=color or self.muted, align="c",
               anchor="m", shape_obj=c, spacing=1)
        return c


# ===================================================================== MODERN
class Modern(Theme):
    key = "modern"
    name = "Modern Indigo"
    label = "Modern"
    head_font = "Calibri"
    body_font = "Calibri"
    colors = dict(dk1="1E1B3A", lt1="FFFFFF", dk2="241E5C", lt2="F1F0FA",
                  accent1="FF6B4A", accent2="1BB5A0", accent3="6C5CE7", accent4="6B6890",
                  accent5="FFB547", accent6="C9C5EC", hlink="6C5CE7", folHlink="6B6890")
    surface = "lt2"
    title_size = 34
    card_radius = 0.2
    grid = "accent6+40"
    series = ("accent3", "accent1", "accent2", "accent5")

    def card(self, slide, x, y, w, h, i=0, fill=None, name="Kartu"):
        shp = super().card(slide, x, y, w, h, i, fill, name)
        k.shadow(shp, blur=16, dist=3, alpha=9, color="241E5C")
        return shp

    cover_bg = divider_bg = closing_bg = "dk2"

    def frame(self, slide, title, kicker, page, meta):
        k.oval(slide, 11.75, -0.95, 2.4, 2.4, "lt2", name="Dekorasi lingkaran")
        k.oval(slide, 12.55, 0.85, 0.5, 0.5, "accent1", name="Dekorasi titik")
        y = super().frame(slide, title, kicker, page, meta)
        return y

    def footer(self, slide, page, meta):
        k.text(slide, 0.7, 6.92, 8, 0.3, meta, size=10, color=self.muted, name="Footer")
        self.badge(slide, 12.18, 6.82, 0.45, f"{page:02d}", size=10, fill="dk2")

    def cover(self, slide, d):
        k.oval(slide, 7.6, -1.6, 7.4, 7.4, "accent3", name="Dekorasi")
        k.oval(slide, 9.9, 3.6, 5.2, 5.2, "accent1", name="Dekorasi")
        k.oval(slide, 7.3, 4.9, 1.3, 1.3, "accent2", name="Dekorasi")
        k.oval(slide, 11.2, 0.9, 0.7, 0.7, "accent5", name="Dekorasi")
        self.logo_slot(slide, 0.8, 0.7, 0.85, fill="lt1+0", color="lt1")
        k.text(slide, 1.85, 0.82, 5, 0.6, [[dict(text=d["kampus"], bold=True)], d["fakultas"]],
               size=12, color="lt1", line_spacing=1.0)
        k.text(slide, 0.8, 2.05, 6.5, 0.4, d["jenis"], size=14, bold=True, color="accent1",
               caps=True, spacing=3)
        self.head(slide, 0.8, 2.5, 7.2, 2.3, d["judul"], size=36, color="lt1", line_spacing=1.0)
        k.rrect(slide, 0.8, 5.25, 5.6, 1.35, "lt1", radius=0.2, name="Kartu identitas", transparency=88)
        k.text(slide, 1.1, 5.42, 5.2, 1.1,
               [[dict(text=d["nama"], bold=True, size=18)], d["nim"], d["pembimbing"]],
               size=12, color="lt1", line_spacing=1.15)

    def divider(self, slide, num, title, subtitle):
        k.oval(slide, 8.3, 0.75, 6.0, 6.0, "accent3", name="Dekorasi")
        k.oval(slide, 7.6, 4.9, 1.6, 1.6, "accent1", name="Dekorasi")
        k.text(slide, 8.3, 0.75, 6.0, 6.0, num, size=150, bold=True, color="lt1", font="+mj-lt",
               align="c", anchor="m", name="Nomor bagian")
        k.text(slide, 0.8, 2.55, 6.6, 0.4, "Bagian " + num, size=14, bold=True, color="accent1",
               caps=True, spacing=3)
        self.head(slide, 0.8, 3.0, 6.8, 1.6, title, size=44, color="lt1", line_spacing=1.0)
        k.text(slide, 0.8, 4.7, 6.2, 1.0, subtitle, size=16, color="accent6")

    def closing(self, slide, d):
        k.oval(slide, -1.8, -2.2, 6.0, 6.0, "accent3", name="Dekorasi")
        k.oval(slide, 10.6, 4.4, 4.6, 4.6, "accent1", name="Dekorasi")
        k.oval(slide, 9.8, 1.0, 0.8, 0.8, "accent2", name="Dekorasi")
        self.head(slide, 1.5, 2.3, 10.3, 1.4, d["judul"], size=66, color="lt1", align="c")
        k.text(slide, 2.0, 3.75, 9.3, 0.6, d["sub"], size=18, color="accent6", align="c")
        x0 = 6.67 - 4.6
        for i, (ic, label) in enumerate(d["kontak"]):
            x = x0 + i * 3.1
            k.icon(slide, self, ic, x, 5.0, 0.38, "accent1")
            k.text(slide, x + 0.5, 4.98, 2.6, 0.45, label, size=13, color="lt1", anchor="m")


# ===================================================================== MINIMALIS
class Minimalis(Theme):
    key = "minimalis"
    name = "Minimalis Mono"
    label = "Minimalis"
    head_font = "Arial"
    body_font = "Arial"
    colors = dict(dk1="161616", lt1="FFFFFF", dk2="161616", lt2="F4F4F2",
                  accent1="0E9F76", accent2="161616", accent3="9AA09C", accent4="7A7A78",
                  accent5="CFD3D0", accent6="E4E6E4", hlink="0E9F76", folHlink="7A7A78")
    surface = "lt2"
    primary = "dk1"
    title_size = 32
    card_radius = 0.0
    grid = "accent6"
    series = ("accent1", "dk1", "accent3", "accent5")

    def card(self, slide, x, y, w, h, i=0, fill=None, name="Kartu"):
        return k.rect(slide, x, y, w, h, fill or "lt1", line="accent5", line_w=0.75, name=name)

    def badge(self, slide, x, y, d, label, i=0, fill=None, color=None, size=None):
        c = k.rect(slide, x, y, d, d, fill or "dk1", name=f"Penanda {label}")
        k.text(slide, x, y, d, d, label, size=size or d * 24, color=color or "lt1", bold=True,
               align="c", anchor="m", shape_obj=c)
        return c

    def icon_disc(self, slide, name, x, y, d, i=0, fill=None, color=None):
        k.icon(slide, self, name, x, y, d * 0.8, color or "dk1")

    def frame(self, slide, title, kicker, page, meta):
        if kicker:
            k.text(slide, 0.7, 0.5, 9, 0.35, kicker, size=12, color=self.accent, bold=True,
                   name="Kicker")
        self.head(slide, 0.7, 0.8, 10.0, 0.85, title, name="Judul slide")
        k.text(slide, 10.9, 0.35, 1.75, 1.0, f"{page:02d}", size=48, bold=True, color="accent6",
               align="r", font="+mj-lt", name="Nomor slide besar")
        k.text(slide, 0.7, 6.92, 8, 0.3, meta, size=10, color=self.muted, name="Footer")
        k.oval(slide, 12.53, 7.02, 0.1, 0.1, "accent1", name="Titik aksen")
        return 1.95

    def footer(self, slide, page, meta):
        pass

    def cover(self, slide, d):
        k.rect(slide, 8.9, 0, 4.433, 7.5, "lt2", name="Panel kanan")
        k.text(slide, 9.4, 0.7, 3.4, 4, "20\n26", size=110, bold=True, color="accent6",
               font="+mj-lt", line_spacing=0.85, name="Tahun dekoratif")
        self.logo_slot(slide, 9.4, 5.6, 0.9)
        k.text(slide, 10.45, 5.7, 2.5, 0.8, [[dict(text=d["kampus"], bold=True)], d["fakultas"]],
               size=10, color="accent4")
        k.text(slide, 0.8, 0.75, 6, 0.35, d["jenis"], size=12, bold=True, color="accent1",
               spacing=1)
        self.head(slide, 0.8, 1.7, 7.6, 2.9, d["judul"], size=38, line_spacing=1.02, anchor="t")
        k.line(slide, 0.8, 4.95, 1.6, 4.95, "dk1", 2.0, name="Pemisah")
        k.text(slide, 0.8, 5.2, 7.5, 1.4,
               [[dict(text=d["nama"], bold=True, size=18)], d["nim"], d["pembimbing"]],
               size=13, color="accent4", line_spacing=1.2)

    def divider(self, slide, num, title, subtitle):
        k.text(slide, 0.62, 0.45, 8, 3.3, num, size=190, bold=True, color="accent6",
               font="+mj-lt", line_spacing=0.9, name="Nomor bagian")
        k.text(slide, 0.8, 4.0, 6, 0.4, "Bagian " + num, size=13, bold=True, color="accent1")
        self.head(slide, 0.8, 4.4, 9, 1.3, title, size=44)
        k.text(slide, 0.8, 5.55, 7.5, 1.0, subtitle, size=16, color="accent4")
        k.oval(slide, 12.33, 6.83, 0.3, 0.3, "accent1", name="Titik aksen")

    def closing(self, slide, d):
        self.head(slide, 0.8, 1.7, 11, 1.5, d["judul"], size=72)
        k.text(slide, 0.8, 3.25, 8, 0.6, d["sub"], size=18, color="accent4")
        k.line(slide, 0.8, 4.45, 12.53, 4.45, "accent5", 0.75, name="Garis")
        for i, (ic, label) in enumerate(d["kontak"]):
            x = 0.8 + i * 3.9
            k.icon(slide, self, ic, x, 4.9, 0.34, "accent1")
            k.text(slide, x + 0.5, 4.86, 3.2, 0.45, label, size=13, color="dk1", anchor="m")
        k.oval(slide, 12.33, 6.83, 0.3, 0.3, "accent1", name="Titik aksen")


# ===================================================================== AKADEMIK BIRU
class AkademikBiru(Theme):
    key = "akademik-biru"
    name = "Akademik Biru"
    label = "Akademik Biru"
    head_font = "Cambria"
    body_font = "Calibri"
    colors = dict(dk1="1B2A41", lt1="FFFFFF", dk2="0B2A5B", lt2="EEF3FA",
                  accent1="1F5FBF", accent2="F2B134", accent3="5FA8E8", accent4="5E6B7E",
                  accent5="0B2A5B", accent6="C9D8EE", hlink="1F5FBF", folHlink="5E6B7E")
    primary = "dk2"
    surface = "lt2"
    card_radius = 0.1
    grid = "accent6"
    series = ("dk2", "accent1", "accent3", "accent2")
    divider_bg = closing_bg = "dk2"

    def card(self, slide, x, y, w, h, i=0, fill=None, name="Kartu"):
        shp = k.rrect(slide, x, y, w, h, fill or "lt1", radius=self.card_radius, name=name,
                      line="accent6", line_w=0.75)
        k.shadow(shp, blur=14, dist=3, alpha=10, color="0B2A5B")
        return shp

    def badge(self, slide, x, y, d, label, i=0, fill=None, color=None, size=None):
        return super().badge(slide, x, y, d, label, i, fill or "dk2", color, size)

    def _dots(self, slide, x, y, cols, rows, gap=0.22, color="accent6", d=0.06):
        for r in range(rows):
            for c in range(cols):
                k.oval(slide, x + c * gap, y + r * gap, d, d, color, name="Pola titik")

    def frame(self, slide, title, kicker, page, meta):
        self._dots(slide, 11.55, 0.45, 5, 4)
        if kicker:
            k.text(slide, 0.7, 0.45, 9, 0.35, kicker, size=12, bold=True, color=self.accent,
                   spacing=1.5, caps=True, name="Kicker")
        self.head(slide, 0.7, 0.75, 10.5, 0.85, title, name="Judul slide")
        k.line(slide, 0.7, 6.8, 12.63, 6.8, "accent6", 0.75, name="Garis footer")
        k.text(slide, 0.7, 6.92, 8, 0.3, meta, size=10, color=self.muted, name="Footer")
        k.text(slide, 11.63, 6.92, 1.0, 0.3, f"{page:02d}", size=10, bold=True, color="dk2",
               align="r", name="Nomor slide")
        return 1.95

    def cover(self, slide, d):
        k.rect(slide, 0, 0, 7.4, 7.5, "dk2", name="Panel biru")
        self._dots(slide, 5.6, 0.55, 6, 5, color="accent1")
        self.logo_slot(slide, 0.8, 0.7, 0.95, fill="accent6", color="accent6")
        k.text(slide, 1.95, 0.8, 4.2, 0.8, [[dict(text=d["kampus"], bold=True)], d["fakultas"]],
               size=12, color="lt1")
        k.text(slide, 0.8, 2.25, 6, 0.4, d["jenis"], size=13, bold=True, color="accent2",
               caps=True, spacing=2)
        self.head(slide, 0.8, 2.7, 6.2, 3.0, d["judul"], size=32, color="lt1", line_spacing=1.05)
        k.text(slide, 8.1, 2.3, 4.6, 0.35, "Disusun oleh", size=12, color="accent4", caps=True,
               spacing=1.5, bold=True)
        k.text(slide, 8.1, 2.7, 4.6, 1.1, [[dict(text=d["nama"], bold=True, size=20,
                                                  font="+mj-lt")], d["nim"]],
               size=14, color="dk2", line_spacing=1.2)
        k.text(slide, 8.1, 4.1, 4.6, 0.35, "Dosen Pembimbing", size=12, color="accent4",
               caps=True, spacing=1.5, bold=True)
        k.text(slide, 8.1, 4.5, 4.6, 1.0, d["pembimbing_list"], size=15, color="dk1",
               line_spacing=1.2)
        k.text(slide, 8.1, 6.3, 4.6, 0.4, d["tahun"], size=12, color="accent4")
        self._dots(slide, 11.6, 6.2, 5, 3)

    def divider(self, slide, num, title, subtitle):
        k.rect(slide, 0, 0, 13.333, 7.5, "dk2", name="Latar")
        self._dots(slide, 10.4, 0.6, 10, 6, color="accent1")
        k.text(slide, 0.8, 1.6, 4, 1.8, num, size=110, bold=True, color="accent2", font="+mj-lt",
               name="Nomor bagian")
        self.head(slide, 0.8, 3.65, 9, 1.3, title, size=44, color="lt1")
        k.text(slide, 0.8, 4.85, 7.5, 1.0, subtitle, size=16, color="accent6")

    def closing(self, slide, d):
        k.rect(slide, 0, 0, 13.333, 7.5, "dk2", name="Latar")
        self._dots(slide, 0.8, 0.7, 8, 3, color="accent1")
        self._dots(slide, 10.9, 5.6, 8, 4, color="accent1")
        self.head(slide, 0.8, 2.3, 11, 1.4, d["judul"], size=64, color="lt1")
        k.text(slide, 0.8, 3.7, 9, 0.6, d["sub"], size=18, color="accent6")
        for i, (ic, label) in enumerate(d["kontak"]):
            x = 0.8 + i * 3.6
            self.icon_disc(slide, ic, x, 4.9, 0.55, fill="accent1", color="lt1")
            k.text(slide, x + 0.7, 4.95, 2.8, 0.45, label, size=13, color="lt1", anchor="m")


# ===================================================================== GELAP ELEGAN
class GelapElegan(Theme):
    key = "gelap-elegan"
    name = "Gelap Elegan"
    label = "Gelap Elegan"
    head_font = "Cambria"
    body_font = "Calibri"
    colors = dict(dk1="111318", lt1="F2EEE6", dk2="1C1F26", lt2="2A2E37",
                  accent1="C9A45C", accent2="8FB3A8", accent3="E3CFA1", accent4="A29F97",
                  accent5="6E7480", accent6="3A3F4A", hlink="C9A45C", folHlink="A29F97")
    dark = True
    bg = "dk1"
    surface = "dk2"
    text = "lt1"
    primary = "lt1"
    accent = "accent1"
    on_accent = "dk1"
    grid = "accent6"
    card_radius = 0.06
    series = ("accent1", "accent2", "accent3", "accent5")

    def card(self, slide, x, y, w, h, i=0, fill=None, name="Kartu"):
        return k.rrect(slide, x, y, w, h, fill or "dk2", radius=self.card_radius, name=name,
                       line="accent6", line_w=0.75)

    def badge(self, slide, x, y, d, label, i=0, fill=None, color=None, size=None):
        c = k.oval(slide, x, y, d, d, fill or "dk1", line="accent1", line_w=1.25,
                   name=f"Penanda {label}")
        k.text(slide, x, y, d, d, label, size=size or d * 24, color=color or "accent1",
               bold=True, align="c", anchor="m", font="+mj-lt", shape_obj=c)
        return c

    def icon_disc(self, slide, name, x, y, d, i=0, fill=None, color=None):
        k.oval(slide, x, y, d, d, fill, line="accent1", line_w=1.0, name="Latar ikon")
        pad = d * 0.26
        k.icon(slide, self, name, x + pad, y + pad, d - 2 * pad, color or "accent1")

    def _frame_lines(self, slide, inset=0.3):
        k.rect(slide, inset, inset, 13.333 - 2 * inset, 7.5 - 2 * inset, None, line="accent1",
               line_w=0.75, name="Bingkai emas")

    def frame(self, slide, title, kicker, page, meta):
        if kicker:
            k.text(slide, 0.8, 0.55, 9, 0.35, kicker, size=11, bold=True, color="accent1",
                   spacing=3, caps=True, name="Kicker")
        self.head(slide, 0.8, 0.85, 10.5, 0.85, title, bold=False, name="Judul slide")
        k.text(slide, 0.8, 6.85, 8, 0.3, meta, size=10, color=self.muted, name="Footer")
        k.text(slide, 10.9, 6.85, 1.63, 0.3, f"— {page:02d}", size=10, color="accent1",
               align="r", name="Nomor slide")
        return 2.0

    def cover(self, slide, d):
        self._frame_lines(slide)
        k.rect(slide, 8.65, 0.3, 4.383, 6.9, "dk2", name="Panel")
        k.oval(slide, 9.35, 1.25, 3.0, 3.0, None, line="accent1", line_w=0.75, name="Lingkaran emas")
        k.oval(slide, 9.75, 1.65, 2.2, 2.2, None, line="accent6", line_w=0.75, name="Lingkaran")
        self.logo_slot(slide, 10.3, 2.2, 1.1, fill="accent1", color="accent1")
        k.text(slide, 8.95, 4.75, 3.8, 0.9, [[dict(text=d["kampus"], bold=True, color="lt1")],
                                              d["fakultas"]],
               size=12, color="accent4", align="c")
        k.text(slide, 8.95, 6.2, 3.8, 0.4, d["tahun"], size=12, color="accent1", align="c",
               spacing=3)
        k.text(slide, 1.0, 1.15, 6, 0.4, d["jenis"], size=12, bold=True, color="accent1",
               spacing=4, caps=True)
        self.head(slide, 1.0, 1.75, 7.2, 3.0, d["judul"], size=36, bold=False, line_spacing=1.05)
        k.line(slide, 1.0, 4.95, 2.2, 4.95, "accent1", 1.25, name="Ornamen")
        k.text(slide, 1.0, 5.2, 7, 1.3, [[dict(text=d["nama"], size=18, color="lt1", bold=True)],
                                          d["nim"], d["pembimbing"]],
               size=12, color="accent4", line_spacing=1.2)

    def divider(self, slide, num, title, subtitle):
        self._frame_lines(slide)
        k.text(slide, 1.5, 1.2, 10.333, 2.2, num, size=120, color="accent1", font="+mj-lt",
               align="c", name="Nomor bagian")
        k.line(slide, 6.17, 3.55, 7.17, 3.55, "accent1", 1.25, name="Ornamen")
        self.head(slide, 1.5, 3.8, 10.333, 1.2, title, size=44, bold=False, align="c")
        k.text(slide, 2.5, 5.0, 8.333, 1.0, subtitle, size=16, color="accent4", align="c")

    def closing(self, slide, d):
        self._frame_lines(slide)
        k.oval(slide, 5.67, 0.9, 2.0, 2.0, None, line="accent1", line_w=0.75, name="Ornamen")
        k.icon(slide, self, "sparkles", 6.27, 1.5, 0.8, "accent1")
        self.head(slide, 1.5, 3.05, 10.333, 1.3, d["judul"], size=60, bold=False, align="c")
        k.text(slide, 2.0, 4.35, 9.333, 0.6, d["sub"], size=16, color="accent4", align="c")
        x0 = 6.67 - 4.6
        for i, (ic, label) in enumerate(d["kontak"]):
            x = x0 + i * 3.1
            k.icon(slide, self, ic, x, 5.45, 0.34, "accent1")
            k.text(slide, x + 0.48, 5.4, 2.6, 0.45, label, size=12, color="lt1", anchor="m")


# ===================================================================== PASTEL
class Pastel(Theme):
    key = "pastel"
    name = "Pastel Lembut"
    label = "Pastel"
    head_font = "Calibri"
    body_font = "Calibri"
    colors = dict(dk1="3D3553", lt1="FFFFFF", dk2="4B3F72", lt2="F6F1FD",
                  accent1="8E6CE0", accent2="F59AB5", accent3="68C4A4", accent4="7D7590",
                  accent5="FFC48C", accent6="E7DEFA", hlink="8E6CE0", folHlink="7D7590")
    primary = "dk2"
    surface = "lt2"
    card_radius = 0.32
    grid = "accent6"
    series = ("accent1", "accent2", "accent3", "accent5")
    FILLS = ("accent1+80", "accent2+75", "accent3+75", "accent5+70")
    INK = ("accent1", "accent2-25", "accent3-30", "accent5-35")

    def card_fill(self, i):
        return self.FILLS[i % 4]

    def card(self, slide, x, y, w, h, i=0, fill=None, name="Kartu"):
        return k.rrect(slide, x, y, w, h, fill or self.FILLS[i % 4], radius=self.card_radius,
                       name=name)

    def badge(self, slide, x, y, d, label, i=0, fill=None, color=None, size=None):
        return super().badge(slide, x, y, d, label, i, fill or self.INK[i % 4], color or "lt1", size)

    def icon_disc(self, slide, name, x, y, d, i=0, fill=None, color=None):
        k.oval(slide, x, y, d, d, fill or "lt1", name="Latar ikon")
        pad = d * 0.25
        k.icon(slide, self, name, x + pad, y + pad, d - 2 * pad, color or self.INK[i % 4])

    def _blobs(self, slide, layout="frame"):
        if layout == "frame":
            k.oval(slide, 11.9, -1.0, 2.3, 2.3, "accent2+75", name="Gelembung")
            k.oval(slide, 12.6, 0.9, 1.1, 1.1, "accent3+70", name="Gelembung")
        elif layout == "cover":
            k.oval(slide, 7.9, -1.3, 6.2, 6.2, "accent1+75", name="Gelembung")
            k.oval(slide, 10.6, 3.6, 4.4, 4.4, "accent2+70", name="Gelembung")
            k.oval(slide, 8.0, 4.6, 2.2, 2.2, "accent3+65", name="Gelembung")
            k.oval(slide, 12.2, 2.75, 0.8, 0.8, "accent5+40", name="Gelembung")
            k.oval(slide, -0.9, 6.3, 2.2, 2.2, "accent5+70", name="Gelembung")

    def frame(self, slide, title, kicker, page, meta):
        self._blobs(slide)
        if kicker:
            pill_w = 0.3 + len(kicker) * 0.105
            pill = k.rrect(slide, 0.7, 0.42, pill_w, 0.36, "accent1+80", radius=0.18, name="Kicker")
            k.text(slide, 0, 0, 0, 0, kicker, size=11, bold=True, color="accent1", align="c",
                   anchor="m", shape_obj=pill, caps=True, spacing=1)
        self.head(slide, 0.7, 0.88, 10.5, 0.85, title, name="Judul slide")
        k.text(slide, 0.7, 6.92, 8, 0.3, meta, size=10, color=self.muted, name="Footer")
        pill = k.rrect(slide, 11.93, 6.86, 0.7, 0.36, "accent6", radius=0.18, name="Nomor slide")
        k.text(slide, 0, 0, 0, 0, f"{page:02d}", size=10, bold=True, color="dk2", align="c",
               anchor="m", shape_obj=pill)
        return 2.05

    def cover(self, slide, d):
        self._blobs(slide, "cover")
        k.icon(slide, self, "graduation-cap", 9.75, 1.15, 2.4, "accent1")
        self.logo_slot(slide, 0.8, 0.7, 0.85)
        k.text(slide, 1.85, 0.8, 5, 0.7, [[dict(text=d["kampus"], bold=True)], d["fakultas"]],
               size=12, color="accent4")
        pill = k.rrect(slide, 0.8, 2.05, 3.0, 0.42, "accent2+75", radius=0.21, name="Label")
        k.text(slide, 0, 0, 0, 0, d["jenis"], size=12, bold=True, color="accent2-30", align="c",
               anchor="m", shape_obj=pill, caps=True, spacing=1)
        self.head(slide, 0.8, 2.7, 6.9, 2.4, d["judul"], size=36, line_spacing=1.02)
        card = k.rrect(slide, 0.8, 5.25, 5.6, 1.35, "lt1", radius=0.3, name="Kartu identitas")
        k.shadow(card, blur=20, dist=4, alpha=10, color="4B3F72")
        k.text(slide, 1.15, 5.42, 5.0, 1.1,
               [[dict(text=d["nama"], bold=True, size=18, color="dk2")], d["nim"], d["pembimbing"]],
               size=12, color="accent4", line_spacing=1.15)

    def divider(self, slide, num, title, subtitle):
        k.oval(slide, 7.7, 0.6, 6.3, 6.3, "accent1+75", name="Gelembung")
        k.oval(slide, 7.3, 4.9, 1.8, 1.8, "accent2+70", name="Gelembung")
        k.oval(slide, 12.5, 0.2, 1.0, 1.0, "accent3+65", name="Gelembung")
        k.text(slide, 7.7, 0.6, 6.3, 6.3, num, size=150, bold=True, color="accent1", align="c",
               anchor="m", font="+mj-lt", name="Nomor bagian")
        pill = k.rrect(slide, 0.8, 2.55, 1.7, 0.4, "accent2+75", radius=0.2, name="Label")
        k.text(slide, 0, 0, 0, 0, "Bagian " + num, size=12, bold=True, color="accent2-30",
               align="c", anchor="m", shape_obj=pill, caps=True)
        self.head(slide, 0.8, 3.1, 6.6, 1.6, title, size=44, line_spacing=1.0)
        k.text(slide, 0.8, 4.75, 6.2, 1.0, subtitle, size=16, color="accent4")

    def closing(self, slide, d):
        k.oval(slide, -1.5, -1.8, 5.0, 5.0, "accent1+75", name="Gelembung")
        k.oval(slide, 10.8, 4.2, 4.5, 4.5, "accent2+70", name="Gelembung")
        k.oval(slide, 10.2, 0.6, 1.4, 1.4, "accent3+65", name="Gelembung")
        k.oval(slide, 1.4, 5.6, 1.0, 1.0, "accent5+50", name="Gelembung")
        k.icon(slide, self, "heart", 6.27, 1.2, 0.8, "accent2")
        self.head(slide, 1.5, 2.2, 10.333, 1.4, d["judul"], size=64, align="c")
        k.text(slide, 2.0, 3.6, 9.333, 0.6, d["sub"], size=18, color="accent4", align="c")
        x0 = 6.67 - 4.65
        for i, (ic, label) in enumerate(d["kontak"]):
            x = x0 + i * 3.1
            pill = k.rrect(slide, x, 4.75, 2.9, 0.6, "lt1", radius=0.3, name="Kontak")
            k.shadow(pill, blur=14, dist=3, alpha=10, color="4B3F72")
            k.icon(slide, self, ic, x + 0.22, 4.89, 0.32, self.INK[i % 4])
            k.text(slide, x + 0.65, 4.75, 2.2, 0.6, label, size=12, color="dk1", anchor="m")


THEMES = [Modern(), Minimalis(), AkademikBiru(), GelapElegan(), Pastel()]
