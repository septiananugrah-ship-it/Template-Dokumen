"""Lima desain CV + surat lamaran yang serasi (Word .docx)."""
from __future__ import annotations

from docx.shared import Cm, Pt

from templategen import docx_kit as dk

from . import content as C


class Design:
    key = "base"
    label = "Base"
    font = "Calibri"
    head_font = "Calibri"
    size = 10.5
    margins = (1.6, 1.8, 1.4, 1.8)
    ink = "222222"
    muted = "666666"
    accent = "1F3A5F"
    data = None
    position = ""
    company = "PT Nama Perusahaan"
    source = "situs JobStreet"

    def new(self):
        return dk.new_document(self.font, self.size, self.margins, self.head_font, self.ink)

    # ---------------------------------------------------------- blok umum
    def section(self, cont, title):
        p = dk.heading(cont, title.upper(), level=1, size=11, bold=True, color=self.accent,
                       before=9, after=4, spacing=1)
        dk.border(p, "bottom", self.accent, 6, 2)
        return p

    def job(self, cont, role, org, place, period, bullets, width):
        p = dk.para(cont, [(role, dict(bold=True, size=self.size + 0.5)),
                           (f"\t{period}", dict(color=self.muted, size=self.size - 0.5))],
                    before=4, keep=True)
        dk.right_tab(p, width)
        dk.para(cont, f"{org} · {place}" if place else org, color=self.accent, italic=True,
                after=2, keep=True)
        for b in bullets:
            dk.bullet(cont, b, color=self.ink)

    def edu(self, cont, degree, school, period, note, width):
        p = dk.para(cont, [(degree, dict(bold=True, size=self.size + 0.5)),
                           (f"\t{period}", dict(color=self.muted, size=self.size - 0.5))],
                    before=3, keep=True)
        dk.right_tab(p, width)
        dk.para(cont, school, color=self.accent, italic=True)
        if note:
            dk.para(cont, note, color=self.muted, size=self.size - 0.5, after=2)

    def inline_list(self, cont, items, sep="  •  "):
        dk.para(cont, sep.join(items), after=2, line=1.25)

    def certs(self, cont, certs):
        for name, org, year in certs:
            dk.para(cont, [(name, dict(bold=True)), (f" — {org}, {year}", dict(color=self.muted))],
                    after=2)

    def projects(self, cont, projects):
        for name, desc in projects:
            dk.para(cont, [(name, dict(bold=True)), (f" — {desc}", dict(color=self.muted))],
                    after=2)

    # ---------------------------------------------------------- surat
    def letter_header(self, doc):
        d = self.data
        p = dk.para(doc, d["name"], size=20, bold=True, color=self.accent, font=self.head_font)
        dk.para(doc, " | ".join(d["contact"][:3]), color=self.muted, size=10, after=4)
        dk.border(doc.paragraphs[-1], "bottom", self.accent, 8, 6)

    def letter(self, path):
        doc = self.new()
        self.letter_header(doc)
        L = C.LETTER
        city = self.data["contact"][0].split(",")[0]
        dk.para(doc, L["date"].format(city=city), before=18, after=12, align="r")
        dk.para(doc, "Perihal: " + L["subject"].format(position=self.position), bold=True,
                after=12)
        for line in L["to"]:
            dk.para(doc, line)
        dk.para(doc, "di Tempat", after=14)
        fmt = dict(position=self.position, company=self.company, source=self.source,
                   highlight=C.HIGHLIGHTS[self.key])
        for i, b in enumerate(L["body"]):
            dk.para(doc, b.format(**fmt), after=12, line=1.45, align="j" if i else "l",
                    size=self.size + 0.5)
        dk.para(doc, L["closing"], before=8, after=44)
        dk.para(doc, self.data["name"], bold=True)
        dk.set_core(doc, f"Surat Lamaran - {self.label}")
        doc.save(path)


# ====================================================================== 1
class Klasik(Design):
    key = "klasik"
    label = "ATS Klasik"
    accent = "1F3A5F"
    data = C.KLASIK
    position = "Staf Akuntansi"
    size = 11
    margins = (1.5, 1.9, 1.3, 1.9)

    def cv(self, path):
        d = self.data
        doc = self.new()
        W = dk.content_width(doc)
        dk.para(doc, d["name"], size=24, bold=True, color=self.accent, align="c",
                font=self.head_font)
        dk.para(doc, d["title"], size=12, color=self.ink, align="c", after=3)
        dk.para(doc, "  |  ".join(d["contact"]), size=9.5, color=self.muted, align="c", after=2)
        self.section(doc, "Ringkasan Profil")
        dk.para(doc, d["summary"], line=1.3, align="j")
        self.section(doc, "Pengalaman Kerja")
        for e in d["experience"]:
            self.job(doc, *e, W)
        self.section(doc, "Pendidikan")
        for e in d["education"]:
            self.edu(doc, *e, W)
        self.section(doc, "Keahlian")
        for s in d["skills"]:
            dk.bullet(doc, s)
        self.section(doc, "Sertifikasi")
        self.certs(doc, d["certifications"])
        self.section(doc, "Organisasi")
        for role, org, period in d["organizations"]:
            p = dk.para(doc, [(role, dict(bold=True)), (f" — {org}", {}),
                              (f"\t{period}", dict(color=self.muted, size=self.size - 0.5))])
            dk.right_tab(p, W)
        self.section(doc, "Bahasa")
        self.inline_list(doc, d["languages"])
        dk.set_core(doc, f"CV - {self.label}")
        doc.save(path)

    def letter_header(self, doc):
        d = self.data
        dk.para(doc, d["name"], size=20, bold=True, color=self.accent, align="c")
        p = dk.para(doc, "  |  ".join(d["contact"][:3]), color=self.muted, size=10, align="c")
        dk.border(p, "bottom", self.accent, 8, 6)


# ====================================================================== 2
class Modern(Design):
    key = "modern"
    label = "Modern Dua Kolom"
    accent = "0E7C86"
    side_fill = "EAF4F4"
    data = C.MODERN
    margins = (1.3, 1.3, 1.2, 1.3)
    position = "Digital Marketing Specialist"
    source = "LinkedIn"
    size = 11

    def side_head(self, cell, title):
        dk.heading(cell, title.upper(), 1, size=10.5, bold=True, color=self.accent, before=12,
                   after=4, spacing=1)

    def cv(self, path):
        d = self.data
        doc = self.new()
        W = dk.content_width(doc)
        wl, wr = 6.0, W - 6.0
        t = dk.layout_table(doc, [wl, wr])
        left, right = t.rows[0].cells
        dk.row_height(t.rows[0], 29.7 - 1.3 - 1.2 - 0.3)
        dk.shade(left, self.side_fill)
        dk.cell_margins(left, 0.6, 0.5, 0.6, 0.5)
        dk.cell_margins(right, 0.3, 0.1, 0.3, 0.7)
        # kiri
        dk.fill_cell_para(left, d["name"], size=21, bold=True, color=self.accent, line=1.0,
                          font=self.head_font)
        dk.para(left, d["title"], size=11, color=self.ink, before=4, after=4)
        self.side_head(left, "Kontak")
        for c in d["contact"]:
            dk.para(left, c, size=10, after=4)
        self.side_head(left, "Keahlian")
        for s in d["skills"]:
            dk.bullet(left, s, size=10, after=3)
        self.side_head(left, "Bahasa")
        for s in d["languages"]:
            dk.para(left, s, size=10, after=4)
        self.side_head(left, "Sertifikasi")
        for name, org, year in d["certifications"]:
            dk.para(left, name, size=10, bold=True)
            dk.para(left, f"{org} · {year}", size=9.5, color=self.muted, after=6)
        # kanan
        rw = wr - 0.8
        p = dk.fill_cell_para(right, "PROFIL", style="Heading 1", size=11, bold=True,
                              color=self.accent, after=4, spacing=1, keep=True)
        dk.para(right, d["summary"], line=1.3, align="j")
        self.section_r(right, "Pengalaman Kerja")
        for e in d["experience"]:
            self.job(right, *e, rw)
        self.section_r(right, "Pendidikan")
        for e in d["education"]:
            self.edu(right, *e, rw)
        dk.set_core(doc, f"CV - {self.label}")
        doc.save(path)

    def section_r(self, cell, title):
        p = dk.heading(cell, title.upper(), 1, size=11, bold=True, color=self.accent,
                       before=14, after=4, spacing=1)
        dk.border(p, "bottom", "B7D9DB", 6, 2)

    def letter_header(self, doc):
        d = self.data
        W = dk.content_width(doc)
        t = dk.layout_table(doc, [W])
        c = t.rows[0].cells[0]
        dk.shade(c, self.side_fill)
        dk.cell_margins(c, 0.5, 0.6, 0.5, 0.6)
        dk.fill_cell_para(c, d["name"], size=20, bold=True, color=self.accent)
        dk.para(c, d["title"] + "   ·   " + "  ·  ".join(d["contact"][1:3]), size=10,
                color=self.ink, before=2)


# ====================================================================== 3
class Minimalis(Design):
    key = "minimalis"
    label = "Minimalis"
    font = "Arial"
    head_font = "Arial"
    size = 10.5
    accent = "111111"
    muted = "777777"
    data = C.MINIMALIS
    margins = (1.8, 2.0, 1.6, 2.0)
    position = "UI/UX Designer"
    source = "Glints"

    def cv(self, path):
        d = self.data
        doc = self.new()
        W = dk.content_width(doc)
        dk.para(doc, d["name"], size=26, color=self.ink, font=self.head_font, line=1.0)
        dk.para(doc, d["title"], size=12, color="0E9F76", before=2, after=6, bold=True)
        p = dk.para(doc, "     ".join(d["contact"]), size=9, color=self.muted, after=6)
        dk.border(p, "bottom", "DDDDDD", 4, 10)
        wl, wr = 3.6, W - 3.6
        rows = [("Profil", lambda c: dk.para(c, d["summary"], line=1.35)),
                ("Pengalaman", lambda c: [self.job(c, *e, wr) for e in d["experience"]]),
                ("Pendidikan", lambda c: [self.edu(c, *e, wr) for e in d["education"]]),
                ("Proyek", lambda c: self.projects(c, d["projects"])),
                ("Keahlian", lambda c: self.inline_list(c, d["skills"], "   ·   ")),
                ("Sertifikasi", lambda c: self.certs(c, d["certifications"])),
                ("Bahasa", lambda c: self.inline_list(c, d["languages"], "   ·   "))]
        t = dk.layout_table(doc, [wl, wr])
        for i, (label, fill) in enumerate(rows):
            row = t.rows[0] if i == 0 else dk.add_row(t, [wl, wr])
            lc, rc = row.cells
            dk.cell_margins(lc, 0.4, 0.2, 0.4, 0)
            dk.cell_margins(rc, 0.4, 0, 0.4, 0)
            dk.fill_cell_para(lc, label.upper(), style="Heading 1", size=9, bold=True,
                              color=self.muted, spacing=1.5, before=4)
            fill(rc)
            dk.remove_leading_empty(rc)
            if i < len(rows) - 1:
                for c in (lc, rc):
                    dk.cell_borders(c, "E5E5E5", 4, sides=("bottom",))
        dk.set_core(doc, f"CV - {self.label}")
        doc.save(path)

    def job(self, cont, role, org, place, period, bullets, width):
        p = dk.para(cont, [(role, dict(bold=True, size=11.5)),
                           (f"\t{period}", dict(color=self.muted, size=9.5))], before=5, keep=True)
        dk.right_tab(p, width)
        dk.para(cont, f"{org}, {place}", color=self.muted, after=2, keep=True)
        for b in bullets:
            dk.bullet(cont, b)

    def edu(self, cont, degree, school, period, note, width):
        p = dk.para(cont, [(degree, dict(bold=True, size=11.5)),
                           (f"\t{period}", dict(color=self.muted, size=9.5))], before=4)
        dk.right_tab(p, width)
        dk.para(cont, school + (f" · {note}" if note else ""), color=self.muted)

    def letter_header(self, doc):
        d = self.data
        dk.para(doc, d["name"], size=22)
        dk.para(doc, d["title"], size=11, color="0E9F76", bold=True, before=2)
        p = dk.para(doc, "     ".join(d["contact"][1:3]), size=9, color=self.muted, before=4)
        dk.border(p, "bottom", "DDDDDD", 4, 10)


# ====================================================================== 4
class Elegan(Design):
    key = "elegan"
    label = "Profesional Elegan"
    font = "Calibri"
    head_font = "Cambria"
    accent = "1C2A39"
    gold = "B08D57"
    data = C.ELEGAN
    margins = (0, 0, 1.3, 0)
    size = 11
    position = "Senior Project Manager"
    source = "situs karier perusahaan"
    PAD = 1.8

    def section(self, cont, title):
        p = dk.heading(cont, title, 1, size=13, bold=True, color=self.accent, before=10,
                       after=4, font=self.head_font)
        dk.border(p, "bottom", self.gold, 6, 3)

    def header_band(self, doc, small=False):
        d = self.data
        t = dk.layout_table(doc, [21.0])
        c = t.rows[0].cells[0]
        dk.shade(c, self.accent)
        dk.cell_margins(c, 1.0 if not small else 0.8, self.PAD, 0.8 if not small else 0.7,
                        self.PAD)
        dk.fill_cell_para(c, d["name"], size=26 if not small else 22, color="FFFFFF",
                          font=self.head_font, line=1.0)
        dk.para(c, d["title"], size=12, color=self.gold, before=3, bold=True, spacing=0.5)
        dk.para(c, "   |   ".join(d["contact"]), size=9.5, color="D9DEE5", before=6)

    def body(self, doc):
        """Badan dokumen memakai tabel 1 kolom berpadding supaya margin kiri-kanan
        tetap ada walau halaman tanpa margin (agar pita header penuh)."""
        t = dk.layout_table(doc, [21.0])
        c = t.rows[0].cells[0]
        dk.cell_margins(c, 0.2, self.PAD, 0, self.PAD)
        return c

    def cv(self, path):
        d = self.data
        doc = self.new()
        self.header_band(doc)
        c = self.body(doc)
        W = 21.0 - 2 * self.PAD
        p = dk.fill_cell_para(c, "Ringkasan Profesional", style="Heading 1", size=13, bold=True,
                              color=self.accent, before=6, after=4, font=self.head_font)
        dk.border(p, "bottom", self.gold, 6, 3)
        dk.para(c, d["summary"], line=1.3, align="j")
        self.section(c, "Pengalaman Profesional")
        for e in d["experience"]:
            self.job(c, *e, W)
        self.section(c, "Pendidikan")
        for e in d["education"]:
            self.edu(c, *e, W)
        # dua kolom: keahlian | sertifikasi & bahasa
        self.section(c, "Kompetensi & Sertifikasi")
        half = W / 2
        t = dk.layout_table(c, [half, half])
        l, r = t.rows[0].cells
        dk.cell_margins(r, 0, 0, 0, 0.4)
        for s in d["skills"]:
            dk.bullet(l, s)
        dk.remove_leading_empty(l)
        for name, org, year in d["certifications"]:
            dk.para(r, name, bold=True)
            dk.para(r, f"{org} · {year}", color=self.muted, after=4)
        dk.para(r, "Bahasa: " + ", ".join(d["languages"]), color=self.ink, before=2)
        dk.remove_leading_empty(r)
        dk.set_core(doc, f"CV - {self.label}")
        doc.save(path)

    def letter(self, path):
        doc = self.new()
        self.header_band(doc, small=True)
        c = self.body(doc)
        L = C.LETTER
        dk.fill_cell_para(c, L["date"].format(city="Surabaya"), before=14, after=12,
                          align="r")
        dk.para(c, "Perihal: " + L["subject"].format(position=self.position), bold=True,
                after=12)
        for line in L["to"]:
            dk.para(c, line)
        dk.para(c, "di Tempat", after=14)
        fmt = dict(position=self.position, company=self.company, source=self.source,
                   highlight=C.HIGHLIGHTS[self.key])
        for i, b in enumerate(L["body"]):
            dk.para(c, b.format(**fmt), after=12, line=1.45, align="j" if i else "l",
                    size=self.size + 0.5)
        dk.para(c, L["closing"], before=8, after=44)
        dk.para(c, self.data["name"], bold=True, font=self.head_font, size=12)
        dk.set_core(doc, f"Surat Lamaran - {self.label}")
        doc.save(path)


# ====================================================================== 5
class Fresh(Design):
    key = "fresh"
    label = "Fresh Graduate"
    accent = "5B4FCF"
    soft = "EFEDFC"
    data = C.FRESH
    margins = (1.4, 1.6, 1.2, 1.6)
    size = 11
    position = "Junior Backend Developer"
    source = "Instagram @lokerkampus"

    def section(self, cont, title):
        p = dk.heading(cont, title.upper(), 1, size=11, bold=True, color=self.accent,
                       before=9, after=4, spacing=1)
        return p

    def header(self, doc, photo=True):
        d = self.data
        W = dk.content_width(doc)
        widths = [3.2, W - 3.2] if photo else [W]
        t = dk.layout_table(doc, widths)
        cells = t.rows[0].cells
        if photo:
            ph = cells[0]
            dk.shade(ph, self.soft)
            dk.cell_borders(ph, self.accent, 6, val="dashed")
            dk.valign(ph, "center")
            dk.row_height(t.rows[0], 4.0, exact=True)
            dk.fill_cell_para(ph, "FOTO", size=11, bold=True, color=self.accent, align="c")
            dk.para(ph, "3 × 4 cm", size=8.5, color=self.muted, align="c")
            dk.para(ph, "(hapus teks,\nInsert > Picture)", size=7.5, color=self.muted,
                    align="c", before=2)
        info = cells[-1]
        dk.valign(info, "center")
        dk.cell_margins(info, 0, 0, 0, 0.6 if photo else 0)
        dk.fill_cell_para(info, d["name"], size=22, bold=True, color=self.ink, line=1.0)
        dk.para(info, d["title"], size=12, color=self.accent, bold=True, before=3, after=6)
        for i in range(0, len(d["contact"]), 2):
            dk.para(info, "     ".join(d["contact"][i:i + 2]), size=9.5, color=self.muted,
                    after=1)

    def cv(self, path):
        d = self.data
        doc = self.new()
        W = dk.content_width(doc)
        self.header(doc)
        self.section(doc, "Tentang Saya")
        dk.para(doc, d["summary"], line=1.3, align="j")
        self.section(doc, "Pendidikan")
        for e in d["education"]:
            self.edu(doc, *e, W)
        self.section(doc, "Pengalaman Magang & Organisasi")
        for e in d["experience"]:
            self.job(doc, *e, W)
        self.section(doc, "Proyek")
        self.projects(doc, d["projects"])
        # keahlian sebagai "chip" berwarna lembut
        self.section(doc, "Keahlian")
        t = dk.layout_table(doc, [W / 3] * 3)
        for i, s in enumerate(d["skills"]):
            r, cidx = divmod(i, 3)
            row = t.rows[0] if r == 0 else (t.rows[r] if r < len(t.rows) else
                                            dk.add_row(t, [W / 3] * 3))
            cell = row.cells[cidx]
            dk.shade(cell, self.soft)
            dk.cell_borders(cell, "FFFFFF", 24)
            dk.cell_margins(cell, 0.12, 0.2, 0.12, 0.2)
            dk.fill_cell_para(cell, s, size=10, bold=True, color=self.accent, align="c")
        self.section(doc, "Prestasi & Sertifikat")
        self.certs(doc, d["certifications"])
        self.section(doc, "Bahasa")
        self.inline_list(doc, d["languages"])
        dk.set_core(doc, f"CV - {self.label}")
        doc.save(path)

    def letter_header(self, doc):
        self.header(doc, photo=False)
        p = dk.para(doc, "", after=2)
        dk.border(p, "bottom", self.accent, 8, 2)


DESIGNS = [Klasik(), Modern(), Minimalis(), Elegan(), Fresh()]
