"""Tema elegan berwarna selaras: satu warna utama + netral, semua kartu
seragam, grafik memakai gradasi satu warna. Dipakai paket pitch deck dan
paket-paket PPT berikutnya."""
from __future__ import annotations

from pptx.enum.shapes import MSO_SHAPE

from . import core as k
from .themes import Theme


def _photo(slide, t, x, y, w, h, kind=MSO_SHAPE.RECTANGLE, label="Foto", radius=None,
           dark=False):
    fill = t.photo_fill
    shp = k.shape(slide, kind, x, y, w, h, fill, radius=radius,
                  name=f"{label} (klik kanan > Format Shape > Fill > Picture)")
    s = min(w, h) * 0.18
    ink = t.photo_ink
    k.icon(slide, t, "image", x + w / 2 - s / 2, y + h / 2 - s * 0.8, s, ink)
    k.text(slide, x + 0.1, y + h / 2 + s * 0.35, w - 0.2, 0.4, label, size=11, bold=True,
           color=ink, align="c", spacing=1, caps=True)
    return shp


class Elegan(Theme):
    """Dasar tema elegan. Variasi antar tema hanya lewat palet, font, motif kecil."""
    motif = "square"          # square | ring | rule | corner
    photo_fill = "lt2"
    photo_ink = "accent4"
    card_line = None          # garis tepi kartu (None = tanpa garis)
    title_bold = True
    cover_style = "split"     # split | framed | circle
    dark_divider = True

    # ------------------------------------------------------------ elemen seragam
    def card(self, slide, x, y, w, h, i=0, fill=None, name="Kartu"):
        if self.card_radius:
            return k.rrect(slide, x, y, w, h, fill or self.surface, radius=self.card_radius,
                           name=name, line=self.card_line, line_w=0.75)
        return k.rect(slide, x, y, w, h, fill or self.surface, name=name, line=self.card_line,
                      line_w=0.75)

    def badge(self, slide, x, y, d, label, i=0, fill=None, color=None, size=None):
        return super().badge(slide, x, y, d, label, 0, fill or self.badge_fill,
                             color or self.badge_ink, size)

    badge_fill = "dk2"
    badge_ink = "lt1"

    def icon_disc(self, slide, name, x, y, d, i=0, fill=None, color=None):
        k.oval(slide, x, y, d, d, fill or self.disc_fill, name="Latar ikon")
        pad = d * 0.26
        k.icon(slide, self, name, x + pad, y + pad, d - 2 * pad, color or self.disc_ink)

    disc_fill = "lt2"
    disc_ink = "dk2"

    def photo(self, slide, x, y, w, h, label="Foto"):
        return _photo(slide, self, x, y, w, h, label=label)

    def head(self, slide, x, y, w, h, content, size=None, color=None, **kw):
        kw.setdefault("bold", self.title_bold)
        return super().head(slide, x, y, w, h, content, size, color, **kw)

    # ------------------------------------------------------------ motif
    def _motif(self, slide, where):
        m = self.motif
        if m == "square":
            k.rect(slide, 12.33, 0.55, 0.3, 0.3, "accent1", name="Aksen")
        elif m == "ring":
            k.oval(slide, 12.13, 0.45, 0.5, 0.5, None, line="accent1", line_w=1.25,
                   name="Aksen")
        elif m == "rule":
            k.line(slide, 11.63, 0.7, 12.63, 0.7, "accent1", 1.5, name="Aksen")
        elif m == "corner":
            k.line(slide, 12.23, 0.45, 12.63, 0.45, "accent1", 1.5, name="Aksen")
            k.line(slide, 12.63, 0.45, 12.63, 0.85, "accent1", 1.5, name="Aksen")

    def frame(self, slide, title, kicker, page, meta):
        self._motif(slide, "frame")
        if kicker:
            k.text(slide, 0.7, 0.45, 9, 0.35, kicker, size=11, bold=True, color=self.accent,
                   caps=True, spacing=2.5, name="Kicker")
        self.head(slide, 0.7, 0.78, 10.8, 0.85, title, name="Judul slide")
        k.text(slide, 0.7, 6.92, 8, 0.3, meta, size=10, color=self.muted, name="Footer")
        k.text(slide, 11.63, 6.92, 1.0, 0.3, f"{page:02d}", size=10, bold=True,
               color=self.primary, align="r", name="Nomor slide")
        return 1.95

    # ------------------------------------------------------------ halaman khusus
    def cover(self, slide, d):
        if "kampus" in d:  # sampul akademik: logo kampus + identitas penyaji
            d = dict(d, brand=d["kampus"], tagline=None,
                     meta=d.get("tahun", ""), _people=[d["nama"], d["nim"], d["pembimbing"]])
        top = d.get("brand", "")
        if self.cover_style == "split":
            _photo(slide, self, 7.9, 0, 5.433, 7.5, label=d.get("photo", "Foto utama"))
            x, w = 0.8, 6.4
        elif self.cover_style == "framed":
            k.rect(slide, 0.35, 0.35, 12.633, 6.8, None, line="accent1", line_w=0.75,
                   name="Bingkai")
            _photo(slide, self, 8.3, 0.9, 4.1, 5.7, label=d.get("photo", "Foto utama"))
            x, w = 1.0, 6.6
        else:  # circle
            k.oval(slide, 7.95, 0.95, 5.1, 5.1, None, line="accent1", line_w=1.0,
                   name="Lingkaran")
            _photo(slide, self, 8.3, 1.3, 4.4, 4.4, MSO_SHAPE.OVAL,
                   label=d.get("photo", "Foto utama"))
            x, w = 0.8, 6.6
        if d.get("_people"):
            self.logo_slot(slide, x, 0.55, 0.8, fill=self.muted, color=self.muted)
            k.text(slide, x + 0.95, 0.75, w - 0.95, 0.45, top, size=12, bold=True,
                   color=self.primary, caps=True, spacing=2)
        else:
            k.text(slide, x, 0.8, w, 0.4, top, size=13, bold=True, color=self.primary,
                   caps=True, spacing=2.5)
        k.text(slide, x, 2.05, w, 0.4, d["jenis"], size=12, bold=True, color=self.accent,
               caps=True, spacing=2.5)
        self.head(slide, x, 2.5, w, 2.4, d["judul"], size=42, line_spacing=1.02)
        if d.get("_people"):
            nm, nim, pb = d["_people"]
            k.text(slide, x, 4.95, w - 0.4, 1.3, [[dict(text=nm, bold=True, size=17,
                                                         color=self.primary)], nim, pb],
                   size=13, color=self.muted, line_spacing=1.25)
        else:
            k.text(slide, x, 5.0, w - 0.6, 0.9, d.get("tagline", ""), size=16,
                   color=self.muted, line_spacing=1.25)
        k.text(slide, x, 6.45, w, 0.4, d.get("meta", ""), size=11, color=self.muted)

    def divider(self, slide, num, title, subtitle):
        on = "lt1" if self.dark_divider else self.primary
        sub = self.divider_sub
        k.text(slide, 0.8, 1.5, 5, 1.9, num, size=110, bold=False, color="accent1",
               font="+mj-lt", name="Nomor bagian")
        self.head(slide, 0.8, 3.6, 9, 1.3, title, size=46, color=on)
        k.text(slide, 0.8, 4.85, 7.5, 1.0, subtitle, size=17, color=sub)
        if self.motif == "ring":
            k.oval(slide, 9.3, 1.4, 4.6, 4.6, None, line="accent1", line_w=1.0,
                   name="Lingkaran")
        else:
            k.rect(slide, 12.03, 6.6, 0.6, 0.06, "accent1", name="Aksen")

    divider_sub = "accent6"

    def closing(self, slide, d):
        on = "lt1" if self.dark_divider else self.primary
        self.head(slide, 0.8, 2.0, 11, 1.4, d["judul"], size=60, color=on)
        k.text(slide, 0.8, 3.4, 9, 0.6, d["sub"], size=18, color=self.divider_sub)
        for i, (ic, label) in enumerate(d["kontak"]):
            x = 0.8 + i * 3.7
            k.icon(slide, self, ic, x, 4.6, 0.34, "accent1")
            k.text(slide, x + 0.5, 4.55, 3.1, 0.45, label, size=13, color=on, anchor="m")


# ===================================================================== MONOKROM
class Monokrom(Elegan):
    key = "monokrom"
    name = "Monokrom"
    label = "Monokrom"
    head_font = "Cambria"
    body_font = "Calibri"
    colors = dict(dk1="161616", lt1="FFFFFF", dk2="161616", lt2="F2F2F0",
                  accent1="161616", accent2="555555", accent3="8C8C8C", accent4="6E6E6E",
                  accent5="BDBDBD", accent6="CFCFCF", hlink="161616", folHlink="6E6E6E")
    primary = "dk1"
    accent = "accent4"
    surface = "lt2"
    grid = "accent6"
    card_radius = 0.0
    series = ("dk1", "accent3", "accent5", "accent2")
    motif = "square"
    cover_style = "split"
    title_bold = False
    divider_bg = closing_bg = "dk1"
    divider_sub = "accent5"
    disc_fill = "lt1"
    hi = "lt1"

    def divider(self, slide, num, title, subtitle):
        k.text(slide, 0.8, 1.5, 5, 1.9, num, size=110, color="lt1", font="+mj-lt",
               name="Nomor bagian")
        self.head(slide, 0.8, 3.6, 9, 1.3, title, size=46, color="lt1")
        k.text(slide, 0.8, 4.85, 7.5, 1.0, subtitle, size=17, color="accent5")


# ===================================================================== HITAM EMAS
class HitamEmas(Elegan):
    key = "hitam-emas"
    name = "Hitam Emas"
    label = "Hitam Emas"
    head_font = "Cambria"
    body_font = "Calibri"
    colors = dict(dk1="0E0E10", lt1="F4F1EA", dk2="1A1A1D", lt2="242428",
                  accent1="C8A96A", accent2="8E7A52", accent3="E2D3B0", accent4="A19D94",
                  accent5="5E5A52", accent6="34343A", hlink="C8A96A", folHlink="A19D94")
    dark = True
    bg = "dk1"
    surface = "dk2"
    text = "lt1"
    primary = "lt1"
    accent = "accent1"
    on_accent = "dk1"
    grid = "accent6"
    card_radius = 0.04
    card_line = "accent6"
    series = ("accent1", "accent2", "accent3", "accent5")
    motif = "ring"
    cover_style = "framed"
    title_bold = False
    photo_fill = "dk2"
    photo_ink = "accent4"
    badge_fill = "dk1"
    badge_ink = "accent1"
    disc_fill = "dk1"
    disc_ink = "accent1"
    divider_sub = "accent4"

    def badge(self, slide, x, y, d, label, i=0, fill=None, color=None, size=None):
        c = k.oval(slide, x, y, d, d, fill or "dk1", line="accent1", line_w=1.0,
                   name=f"Penanda {label}")
        k.text(slide, x, y, d, d, label, size=size or d * 24, color=color or "accent1",
               bold=True, align="c", anchor="m", font="+mj-lt", shape_obj=c)
        return c

    def icon_disc(self, slide, name, x, y, d, i=0, fill=None, color=None):
        k.oval(slide, x, y, d, d, None, line="accent1", line_w=1.0, name="Latar ikon")
        pad = d * 0.26
        k.icon(slide, self, name, x + pad, y + pad, d - 2 * pad, "accent1")


# ===================================================================== NAVY
class Navy(Elegan):
    key = "navy"
    name = "Navy Profesional"
    label = "Navy"
    head_font = "Calibri"
    body_font = "Calibri"
    colors = dict(dk1="1A2233", lt1="FFFFFF", dk2="14213D", lt2="EFF2F6",
                  accent1="4A6FA5", accent2="14213D", accent3="8FA8CC", accent4="657084",
                  accent5="C9D5E6", accent6="DCE2EA", hlink="4A6FA5", folHlink="657084")
    primary = "dk2"
    accent = "accent1"
    grid = "accent6"
    card_radius = 0.08
    series = ("dk2", "accent1", "accent3", "accent5")
    motif = "corner"
    cover_style = "split"
    divider_bg = closing_bg = "dk2"
    photo_fill = "lt2"
    disc_fill = "lt1"


# ===================================================================== BATU (warm gray)
class Batu(Elegan):
    key = "batu"
    name = "Batu Hangat"
    label = "Batu"
    head_font = "Cambria"
    body_font = "Calibri"
    colors = dict(dk1="2E2A27", lt1="FFFFFF", dk2="3F3A36", lt2="F1EEEA",
                  accent1="8C7B6B", accent2="3F3A36", accent3="B5A898", accent4="7A716A",
                  accent5="D6CEC4", accent6="E2DCD5", hlink="8C7B6B", folHlink="7A716A")
    primary = "dk2"
    accent = "accent1"
    grid = "accent6"
    card_radius = 0.18
    series = ("dk2", "accent1", "accent3", "accent5")
    motif = "rule"
    cover_style = "circle"
    title_bold = False
    divider_bg = closing_bg = "dk2"
    divider_sub = "accent5"
    disc_fill = "lt1"


# ===================================================================== ZAITUN
class Zaitun(Elegan):
    key = "zaitun"
    name = "Zaitun"
    label = "Zaitun"
    head_font = "Calibri"
    body_font = "Calibri"
    colors = dict(dk1="232A22", lt1="FFFFFF", dk2="2F3A2F", lt2="EFF1EC",
                  accent1="6B7B4B", accent2="2F3A2F", accent3="A3AE88", accent4="6A7066",
                  accent5="CDD3BF", accent6="DFE3D8", hlink="6B7B4B", folHlink="6A7066")
    primary = "dk2"
    accent = "accent1"
    grid = "accent6"
    card_radius = 0.28
    series = ("dk2", "accent1", "accent3", "accent5")
    motif = "ring"
    cover_style = "framed"
    divider_bg = closing_bg = "dk2"
    divider_sub = "accent5"
    disc_fill = "lt1"


# ===================================================================== MARUN
class Marun(Elegan):
    key = "marun"
    name = "Marun"
    label = "Marun"
    head_font = "Cambria"
    body_font = "Calibri"
    colors = dict(dk1="2A1A20", lt1="FFFFFF", dk2="5E2235", lt2="F5EFF1",
                  accent1="8E3B55", accent2="5E2235", accent3="C08A9B", accent4="776A6F",
                  accent5="E3CCD4", accent6="EADFE3", hlink="8E3B55", folHlink="776A6F")
    primary = "dk2"
    accent = "accent1"
    grid = "accent6"
    card_radius = 0.12
    series = ("dk2", "accent1", "accent3", "accent5")
    motif = "ring"
    cover_style = "split"
    title_bold = False
    divider_bg = closing_bg = "dk2"
    divider_sub = "accent5"
    disc_fill = "lt1"


# ===================================================================== SLATE
class Slate(Elegan):
    key = "slate"
    name = "Slate"
    label = "Slate"
    head_font = "Calibri"
    body_font = "Calibri"
    colors = dict(dk1="1E2430", lt1="FFFFFF", dk2="334155", lt2="F1F4F7",
                  accent1="5B7083", accent2="334155", accent3="94A3B8", accent4="64748B",
                  accent5="CBD5E1", accent6="E2E8F0", hlink="5B7083", folHlink="64748B")
    primary = "dk2"
    accent = "accent1"
    grid = "accent6"
    card_radius = 0.06
    series = ("dk2", "accent1", "accent3", "accent5")
    motif = "square"
    cover_style = "framed"
    divider_bg = closing_bg = "dk2"
    divider_sub = "accent5"
    disc_fill = "lt1"


# ===================================================================== HUTAN
class Hutan(Elegan):
    key = "hutan"
    name = "Hutan"
    label = "Hutan"
    head_font = "Cambria"
    body_font = "Calibri"
    colors = dict(dk1="17261E", lt1="FFFFFF", dk2="1F3B2D", lt2="EEF3F0",
                  accent1="3F6B53", accent2="1F3B2D", accent3="8CAE9A", accent4="5F6E66",
                  accent5="C9D9CF", accent6="DCE6E0", hlink="3F6B53", folHlink="5F6E66")
    primary = "dk2"
    accent = "accent1"
    grid = "accent6"
    card_radius = 0.22
    series = ("dk2", "accent1", "accent3", "accent5")
    motif = "rule"
    cover_style = "circle"
    title_bold = False
    divider_bg = closing_bg = "dk2"
    divider_sub = "accent5"
    disc_fill = "lt1"


# ===================================================================== MALAM (gelap)
class Malam(Elegan):
    key = "malam"
    name = "Biru Malam"
    label = "Biru Malam"
    head_font = "Calibri"
    body_font = "Calibri"
    colors = dict(dk1="0D1321", lt1="EEF2F8", dk2="16203A", lt2="1E2A47",
                  accent1="8FB3E8", accent2="5C7FB8", accent3="C7D8F2", accent4="93A0B8",
                  accent5="3E5687", accent6="2A3757", hlink="8FB3E8", folHlink="93A0B8")
    dark = True
    bg = "dk1"
    surface = "dk2"
    text = "lt1"
    primary = "lt1"
    accent = "accent1"
    on_accent = "dk1"
    grid = "accent6"
    card_radius = 0.1
    card_line = "accent6"
    series = ("accent1", "accent2", "accent3", "accent5")
    motif = "corner"
    cover_style = "framed"
    photo_fill = "dk2"
    photo_ink = "accent4"
    badge_fill = "accent1"
    badge_ink = "dk1"
    disc_fill = "dk1"
    disc_ink = "accent1"
    divider_sub = "accent4"


# ===================================================================== PASIR (terang hangat)
class Pasir(Elegan):
    key = "pasir"
    name = "Pasir"
    label = "Pasir"
    head_font = "Cambria"
    body_font = "Calibri"
    colors = dict(dk1="2B2622", lt1="FFFFFF", dk2="2B2622", lt2="F4F1EC",
                  accent1="A0866B", accent2="2B2622", accent3="C9B8A3", accent4="7B7068",
                  accent5="E3D9CD", accent6="E8E2DA", hlink="A0866B", folHlink="7B7068")
    primary = "dk1"
    accent = "accent1"
    grid = "accent6"
    card_radius = 0.0
    card_line = "accent6"
    surface = "lt1"
    series = ("dk1", "accent1", "accent3", "accent5")
    motif = "corner"
    cover_style = "split"
    title_bold = False
    dark_divider = False
    divider_bg = closing_bg = "lt2"
    divider_sub = "accent4"
    badge_fill = "dk1"


def variant(key, label, colors, base=Elegan, **attrs):
    """Buat tema elegan baru hanya dari palet + beberapa atribut."""
    defaults = dict(key=key, name=label, label=label, colors=colors, primary="dk2",
                    accent="accent1", grid="accent6", series=("dk2", "accent1", "accent3",
                                                              "accent5"),
                    divider_bg="dk2", closing_bg="dk2", divider_sub="accent5", disc_fill="lt1")
    defaults.update(attrs)
    return type(label.replace(" ", ""), (base,), defaults)()


def _pal(dk1, dk2, lt2, a1, a3, a4, a5, a6):
    return dict(dk1=dk1, lt1="FFFFFF", dk2=dk2, lt2=lt2, accent1=a1, accent2=dk2, accent3=a3,
                accent4=a4, accent5=a5, accent6=a6, hlink=a1, folHlink=a4)


GRAFIT = variant("grafit", "Grafit", _pal("1F2124", "2B2E33", "F1F2F3", "6B7280", "A3A8B0",
                                          "6B6F76", "D1D4D8", "E3E5E8"),
                 head_font="Calibri", body_font="Calibri", card_radius=0.06, motif="square",
                 cover_style="split")
TEAL = variant("teal", "Teal", _pal("10302E", "134E4A", "EDF5F4", "2F7F78", "8FC1BB",
                                    "5D706E", "C7E0DD", "DCEBEA"),
               head_font="Cambria", body_font="Calibri", card_radius=0.16, motif="ring",
               cover_style="circle", title_bold=False)
CHAMPAGNE = variant("champagne", "Champagne", _pal("2C2720", "2C2720", "F7F3EC", "B08D57",
                                                    "D8C3A0", "7C7166", "EADCC6", "EFE6D8"),
                    head_font="Cambria", body_font="Calibri", card_radius=0.0,
                    card_line="accent6", surface="lt1", motif="corner", cover_style="framed",
                    title_bold=False, primary="dk1", series=("dk1", "accent1", "accent3",
                                                             "accent5"))
INDIGO = variant("indigo", "Indigo", _pal("1C1A3A", "2E2A5A", "F0EFF7", "5B54A0", "A7A2D6",
                                          "686580", "D2CFEA", "E2E0F1"),
                 head_font="Calibri", body_font="Calibri", card_radius=0.12, motif="corner",
                 cover_style="split")
BATA = variant("bata", "Bata", _pal("2A1C18", "6B2F22", "F6F0EE", "9A4A38", "C89A8D", "7A6A65",
                                    "E6D2CC", "EEE2DE"),
               head_font="Cambria", body_font="Calibri", card_radius=0.2, motif="rule",
               cover_style="split", title_bold=False)

THEMES = [Monokrom(), HitamEmas(), Navy(), Batu(), Zaitun()]
PROFIL = [GRAFIT, TEAL, CHAMPAGNE, INDIGO, BATA]
KULIAH = [Marun(), Slate(), Hutan(), Malam(), Pasir()]
