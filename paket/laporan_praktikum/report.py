"""Penyusun dokumen laporan praktikum (Word) dengan format akademik:
Times New Roman 12, spasi 1,5, margin 4-3-3-3, halaman romawi untuk bagian
awal dan arab untuk isi, daftar isi berupa field Word."""
from __future__ import annotations

import re
from pathlib import Path

from docx.enum.section import WD_SECTION
from docx.shared import Cm, Pt

from templategen import docx_kit as dk
from templategen import render

FONT = "Times New Roman"
ROMAN = ["I", "II", "III", "IV", "V", "VI"]
W = 21 - 4 - 3  # lebar isi (cm)
IND = 1.0       # jarak nomor subjudul ke teks subjudul; isi subbab sejajar teks ini


class Report:
    def __init__(self, data, accent="1F3A5F"):
        self.d = data
        self.accent = accent

    # ------------------------------------------------------------ blok dasar
    def body(self, cont, text, indent=True, after=6, left=None):
        """Paragraf isi. Di dalam subbab, seluruh paragraf digeser sejajar dengan
        teks subjudul (bukan dengan nomornya), baris pertama menjorok 1,25 cm."""
        p = dk.para(cont, text, align="j", line=1.5, after=after)
        pf = p.paragraph_format
        pf.left_indent = Cm(self.left if left is None else left)
        if indent:
            pf.first_line_indent = Cm(1.25)
        return p

    left = 0.0

    def bab(self, doc, n, title):
        p = dk.heading(doc, [(f"BAB {ROMAN[n - 1]}", {}), ("\n" + title, {})], 1, size=14,
                       bold=True, color="000000", align="c", after=18, line=1.5)
        p.paragraph_format.page_break_before = n > 1
        self.left = 0.0
        self.toc.append((f"BAB {ROMAN[n - 1]} {title}", 1, title))
        return p

    def sub(self, doc, num, title):
        p = dk.heading(doc, f"{num}\t{title}", 2, size=12, bold=True, color="000000",
                       before=6, after=6, line=1.5)
        pf = p.paragraph_format
        pf.left_indent = Cm(IND)
        pf.first_line_indent = Cm(-IND)
        pf.tab_stops.add_tab_stop(Cm(IND))
        self.left = IND
        self.toc.append((f"{num} {title}", 2, f"{num} {title}"))

    def numbered(self, doc, items, start=1, fmt="{}."):
        for i, it in enumerate(items, start):
            p = dk.para(doc, f"{fmt.format(i)}\t{it}", align="j", line=1.5, after=0)
            pf = p.paragraph_format
            pf.left_indent = Cm(self.left + 0.75)
            pf.first_line_indent = Cm(-0.75)
            pf.tab_stops.add_tab_stop(Cm(self.left + 0.75))

    def caption(self, doc, text, before=6, after=6):
        p = dk.para(doc, text, align="c", bold=True, size=11, before=before, after=after,
                    line=1.15, keep=True)
        p.paragraph_format.left_indent = Cm(self.left)
        return p

    def table(self, doc, rows, widths=None, align=None):
        n = len(rows[0])
        avail = W - self.left
        widths = widths or [avail / n] * n
        widths = [w * avail / sum(widths) for w in widths]
        t = dk.layout_table(doc, widths, cell_margin=(0.08, 0.15, 0.08, 0.15),
                            indent_cm=self.left)
        for r, row in enumerate(rows):
            tr = t.rows[0] if r == 0 else dk.add_row(t, widths)
            for c, val in enumerate(row):
                cell = tr.cells[c]
                dk.cell_borders(cell, "000000", 6)
                if r == 0:
                    dk.shade(cell, "E7ECF3")
                dk.valign(cell, "center")
                a = "c" if (r == 0 or (align and align[c] == "c")) else "l"
                bold = r == 0 or (row[0] == "Rata-rata")
                dk.fill_cell_para(cell, val, size=11, bold=bold, align=a, line=1.15)
        dk.para(doc, "", after=4)
        return t

    def figure_box(self, doc, label):
        t = dk.layout_table(doc, [W * 0.75])
        c = t.rows[0].cells[0]
        dk.cell_borders(c, "7F8FA6", 8, val="dashed")
        dk.shade(c, "F5F7FA")
        dk.valign(c, "center")
        dk.row_height(t.rows[0], 6.0, exact=True)
        dk.fill_cell_para(c, "[ Tempel foto / gambar di sini ]", size=11, color="5A6B82",
                          align="c", bold=True)
        dk.para(c, "Klik di kotak ini, hapus teksnya, lalu Insert > Pictures", size=9,
                color="7F8FA6", align="c")
        self.caption(doc, label, before=4, after=10)

    def code_box(self, doc, code):
        t = dk.layout_table(doc, [W - self.left], cell_margin=(0.2, 0.3, 0.2, 0.3),
                            indent_cm=self.left)
        c = t.rows[0].cells[0]
        dk.shade(c, "F3F4F6")
        dk.cell_borders(c, "D0D4DA", 6)
        first = True
        for line in code.splitlines():
            if first:
                dk.fill_cell_para(c, line or " ", size=9.5, font="Courier New", line=1.0)
                first = False
            else:
                dk.para(c, line or " ", size=9.5, font="Courier New", line=1.0)
        dk.para(doc, "", after=4)

    # ------------------------------------------------------------ halaman depan
    def cover(self, doc):
        d = self.d
        dk.para(doc, "LAPORAN PRAKTIKUM", size=16, bold=True, align="c", after=2)
        dk.para(doc, d["mk"].upper(), size=14, bold=True, align="c", after=14)
        dk.para(doc, f"PERCOBAAN {d['no']}", size=12, bold=True, align="c", after=2)
        dk.para(doc, d["judul"].upper(), size=13, bold=True, align="c", line=1.3, after=26,
                color=self.accent)
        # tempat logo
        t = dk.layout_table(doc, [4.0])
        t.alignment = 1
        c = t.rows[0].cells[0]
        dk.cell_borders(c, "8A94A6", 8, val="dashed")
        dk.valign(c, "center")
        dk.row_height(t.rows[0], 4.0, exact=True)
        dk.fill_cell_para(c, "LOGO KAMPUS", size=10, bold=True, color="8A94A6", align="c")
        dk.para(c, "(Insert > Pictures)", size=8, color="8A94A6", align="c")
        dk.para(doc, "", after=20)
        dk.para(doc, "Disusun oleh:", align="c", after=6)
        info = [("Nama", d["nama"]), ("NIM", d["nim"]), ("Kelompok", d["kelompok"]),
                ("Asisten", d["asisten"])]
        widths = [3.0, 0.5, 6.5]
        t = dk.layout_table(doc, widths)
        for i, (k_, v) in enumerate(info):
            row = t.rows[0] if i == 0 else dk.add_row(t, widths)
            for cell, txt in zip(row.cells, (k_, ":", v)):
                dk.fill_cell_para(cell, txt, line=1.5, bold=(txt == v and i == 0))
        dk.para(doc, "", after=60)
        for line in (d["lab"], d["prodi"], d["fakultas"], d["univ"], d["tahun"]):
            dk.para(doc, line, size=13, bold=True, align="c", line=1.3)

    def approval(self, doc):
        d = self.d
        dk.para(doc, "LEMBAR PENGESAHAN", size=14, bold=True, align="c", after=24)
        self.left = 0.0
        self.body(doc, f"Laporan praktikum {d['mk']} percobaan {d['no']} yang berjudul "
                       f"“{d['judul']}” telah diperiksa dan disetujui oleh asisten "
                       f"praktikum.", indent=False, after=30)
        dk.para(doc, f"{d['kota']}, {d['tanggal']}", align="r", after=20)
        widths = [W / 2, W / 2]
        t = dk.layout_table(doc, widths)
        for cell, role, name in zip(t.rows[0].cells, ("Asisten Praktikum,", "Praktikan,"),
                                    (d["asisten"], d["nama"])):
            dk.fill_cell_para(cell, role, align="c", after=60)
            p = dk.para(cell, name, align="c", bold=True)
            dk.para(cell, "NIM. ...................." if role.startswith("Asisten")
                    else f"NIM. {d['nim']}", align="c")
        dk.para(doc, "", after=30)
        dk.para(doc, "Mengetahui,", align="c")
        dk.para(doc, "Dosen Pengampu", align="c", after=60)
        dk.para(doc, d["dosen"], align="c", bold=True)
        dk.para(doc, "NIP. ....................", align="c")

    # ------------------------------------------------------------ dokumen utuh
    def build(self, path: Path, toc_pages=None):
        d = self.d
        self.toc = []
        doc = dk.new_document(FONT, 12, margins=(3, 3, 3, 4), head_font=FONT, color="000000")
        doc.styles["Normal"].paragraph_format.line_spacing = 1.5
        s1 = doc.sections[0]
        dk.blank_footer(s1)
        self.cover(doc)

        s2 = doc.add_section(WD_SECTION.NEW_PAGE)
        dk.page_number_format(s2, "lowerRoman", 1)
        dk.footer_page_number(s2)
        self.approval(doc)
        dk.page_break(doc)
        dk.para(doc, "DAFTAR ISI", size=14, bold=True, align="c", after=18)
        toc_slot = doc.add_paragraph()  # jangkar daftar isi, diisi setelah isi selesai

        s3 = doc.add_section(WD_SECTION.NEW_PAGE)
        dk.page_number_format(s3, "decimal", 1)
        dk.footer_page_number(s3)

        # BAB I
        self.bab(doc, 1, "PENDAHULUAN")
        self.sub(doc, "1.1", "Latar Belakang")
        for t in d["latar"]:
            self.body(doc, t)
        self.sub(doc, "1.2", "Tujuan Percobaan")
        self.numbered(doc, d["tujuan"])
        # BAB II
        self.bab(doc, 2, "TINJAUAN PUSTAKA")
        for i, (head, paras) in enumerate(d["teori"], 1):
            self.sub(doc, f"2.{i}", head)
            for t in paras:
                self.body(doc, t)
        # BAB III
        self.bab(doc, 3, "METODOLOGI PERCOBAAN")
        self.sub(doc, "3.1", "Alat dan Bahan" if d["bahan"] else "Alat")
        self.caption(doc, "Tabel 3.1 Alat yang digunakan")
        self.table(doc, [["No", "Nama Alat", "Jumlah"]] +
                   [[str(i), a, b] for i, (a, b) in enumerate(d["alat"], 1)],
                   [1.2, 8.3, 4.5], align=["c", "l", "c"])
        if d["bahan"]:
            self.caption(doc, "Tabel 3.2 Bahan yang digunakan")
            self.table(doc, [["No", "Nama Bahan", "Jumlah / Konsentrasi"]] +
                       [[str(i), a, b] for i, (a, b) in enumerate(d["bahan"], 1)],
                       [1.2, 8.3, 4.5], align=["c", "l", "c"])
        self.sub(doc, "3.2", "Prosedur Kerja")
        self.numbered(doc, d["prosedur"])
        if d.get("code"):
            q = dk.para(doc, "Kode program:", before=6, after=4, bold=True)
            q.paragraph_format.left_indent = Cm(self.left)
            self.code_box(doc, d["code"])
        # BAB IV
        self.bab(doc, 4, "HASIL DAN PEMBAHASAN")
        self.sub(doc, "4.1", "Data Pengamatan")
        self.caption(doc, f"Tabel 4.1 {d['data_title']}")
        n = len(d["data"][0])
        self.table(doc, d["data"], align=["c"] * n)
        self.figure_box(doc, f"Gambar 4.1 {d['figure']}")
        num = 2
        if d.get("hitung"):
            self.sub(doc, "4.2", "Perhitungan")
            for h in d["hitung"]:
                p = dk.para(doc, h, line=1.5)
                p.paragraph_format.left_indent = Cm(self.left + 0.75)
            num = 3
        self.sub(doc, f"4.{num}", "Pembahasan")
        for t in d["bahas"]:
            self.body(doc, t)
        # BAB V
        self.bab(doc, 5, "KESIMPULAN DAN SARAN")
        self.sub(doc, "5.1", "Kesimpulan")
        self.numbered(doc, d["simpulan"])
        self.sub(doc, "5.2", "Saran")
        self.numbered(doc, d["saran"])
        # Pustaka & lampiran
        p = dk.heading(doc, "DAFTAR PUSTAKA", 1, size=14, bold=True, color="000000",
                       align="c", after=18)
        p.paragraph_format.page_break_before = True
        self.toc.append(("DAFTAR PUSTAKA", 1, "DAFTAR PUSTAKA"))
        self.left = 0.0
        for ref in d["pustaka"]:
            q = dk.para(doc, ref, align="j", line=1.15, after=10)
            q.paragraph_format.left_indent = Cm(1.25)
            q.paragraph_format.first_line_indent = Cm(-1.25)
        p = dk.heading(doc, "LAMPIRAN", 1, size=14, bold=True, color="000000", align="c",
                       after=18)
        p.paragraph_format.page_break_before = True
        self.toc.append(("LAMPIRAN", 1, "LAMPIRAN"))
        self.left = 0.0
        self.numbered(doc, ["Lembar data pengamatan sementara (ditandatangani asisten)",
                            "Jawaban tugas / pertanyaan pasca praktikum",
                            "Dokumentasi tambahan"])

        # isi daftar isi
        pages = toc_pages or ["…"] * len(self.toc)
        holder = dk.layout_table(doc, [W])
        cell = holder.rows[0].cells[0]
        dk.toc(cell, [(txt, lvl, pg) for (txt, lvl, _), pg in zip(self.toc, pages)], W)
        dk.remove_leading_empty(cell)
        # pindahkan paragraf daftar isi dari sel ke jangkar, lalu buang tabelnya
        for par in list(cell.paragraphs):
            toc_slot._p.addprevious(par._p)
        holder._tbl.getparent().remove(holder._tbl)
        toc_slot._p.getparent().remove(toc_slot._p)

        dk.set_core(doc, f"Laporan Praktikum {d['label']}")
        doc.save(path)
        return path


def _norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def build_with_toc(data, path: Path, workdir: Path):
    """Dua tahap: bangun, render ke PDF untuk mencari nomor halaman tiap judul,
    lalu bangun ulang dengan daftar isi yang sudah benar."""
    from pypdf import PdfReader

    rep = Report(data)
    rep.build(path)
    pdf = render.to_pdf(path, workdir)
    texts = [_norm(p.extract_text() or "") for p in PdfReader(str(pdf)).pages]
    body_start = next(i for i, t in enumerate(texts) if "pendahuluan" in t and "bab i" in t
                      and "daftar isi" not in t)
    pages, cur = [], body_start
    for _, _, key in rep.toc:
        k = _norm(key)
        for i in range(cur, len(texts)):
            if k in texts[i]:
                cur = i
                break
        pages.append(str(cur - body_start + 1))
    Report(data).build(path, pages)
    pdf.unlink()
    return path
