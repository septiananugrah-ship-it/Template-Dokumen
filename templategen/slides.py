"""Tata letak slide isi, dipakai bersama oleh semua tema dan semua paket.

Builder menerima daftar spesifikasi slide (dict dengan kunci 'type') lalu
memanggil metode bernama sama. Tiap metode hanya memakai peran warna tema
(theme.accent, theme.surface, ...), sehingga satu konten tampil berbeda di
tiap tema.
"""
from __future__ import annotations

from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION, XL_LEGEND_POSITION
from pptx.enum.dml import MSO_LINE_DASH_STYLE

from . import core as k

X0, X1 = 0.7, 12.63          # batas kiri/kanan area konten
W = X1 - X0
Y_END = 6.6                  # batas bawah area konten


class Builder:
    def __init__(self, theme, meta):
        self.t = theme
        self.meta = meta
        self.prs = k.new_presentation(theme)
        self.page = 0

    # ------------------------------------------------------------ dasar
    def build(self, specs, path):
        for spec in specs:
            spec = dict(spec)
            kind = spec.pop("type")
            self.page += 1
            slide = getattr(self, kind)(**spec)
            if spec.get("notes"):
                k.notes(slide, spec["notes"])
        self.prs.core_properties.title = self.meta
        self.prs.core_properties.author = "Template-Dokumen"
        self.prs.save(path)
        return path

    def _content(self, title, kicker=None, notes=None):
        slide = k.blank_slide(self.prs, self.t)
        y = self.t.frame(slide, title, kicker, self.page, self.meta)
        return slide, y

    def _panel(self):
        """Tema dengan kartu warna-warni memakai panel netral di belakang grafik
        agar batang grafik tidak menyatu dengan warna kartu."""
        return "lt1" if getattr(self.t, "neutral_panel", False) else None

    # ------------------------------------------------------------ halaman khusus
    def cover(self, notes=None, **d):
        s = k.blank_slide(self.prs, self.t, self.t.cover_bg)
        self.t.cover(s, d)
        return s

    def divider(self, num, title, subtitle="", notes=None):
        s = k.blank_slide(self.prs, self.t, self.t.divider_bg)
        self.t.divider(s, num, title, subtitle)
        return s

    def closing(self, notes=None, **d):
        s = k.blank_slide(self.prs, self.t, self.t.closing_bg)
        self.t.closing(s, d)
        return s

    # ------------------------------------------------------------ isi
    def agenda(self, title, items, kicker=None, notes=None):
        s, y = self._content(title, kicker)
        t = self.t
        rows = (len(items) + 1) // 2
        col_w = (W - 0.5) / 2
        row_h = (Y_END - y + 0.3) / rows
        for i, (head, desc) in enumerate(items):
            col, row = divmod(i, rows)
            x = X0 + col * (col_w + 0.5)
            yy = y + row * row_h
            t.card(s, x, yy, col_w, row_h - 0.3, i=i, name=f"Agenda {i + 1}")
            d = 0.62
            t.badge(s, x + 0.3, yy + (row_h - 0.3 - d) / 2, d, f"{i + 1:02d}", i=i, size=15)
            ch = row_h - 0.3
            k.text(s, x + 1.2, yy + ch / 2 - 0.42, col_w - 1.45, 0.42, head, size=19, bold=True,
                   color=t.primary, font="+mj-lt", anchor="b")
            k.text(s, x + 1.2, yy + ch / 2 + 0.04, col_w - 1.45, 0.45, desc, size=14,
                   color=t.muted)
        return s

    def text_stats(self, title, paragraphs, stats, kicker=None, notes=None):
        s, y = self._content(title, kicker)
        t = self.t
        t.body(s, X0, y + 0.05, 6.6, Y_END - y, paragraphs, size=17, line_spacing=1.3,
               para_after=12, name="Paragraf")
        n = len(stats)
        gap = 0.3
        h = (Y_END - y - gap * (n - 1)) / n
        x = 7.85
        for i, (val, label) in enumerate(stats):
            yy = y + i * (h + gap)
            t.card(s, x, yy, X1 - x, h, i=i, name=f"Statistik {i + 1}")
            k.text(s, x + 0.35, yy, 2.1, h, val, size=36, bold=True, color=t.accent,
                   anchor="m", font="+mj-lt")
            k.text(s, x + 2.45, yy, X1 - x - 2.7, h, label, size=15, color=t.text, anchor="m")
        return s

    def numbered(self, title, items, kicker=None, notes=None, lead=None):
        s, y = self._content(title, kicker)
        t = self.t
        if lead:
            t.body(s, X0, y - 0.15, W, 0.5, lead, size=15, color=t.muted)
            y += 0.5
        n = len(items)
        gap = 0.25
        h = (Y_END - y - gap * (n - 1)) / n
        for i, (head, desc) in enumerate(items):
            yy = y + i * (h + gap)
            t.card(s, X0, yy, W, h, i=i, name=f"Butir {i + 1}")
            d = min(0.8, h - 0.35)
            t.badge(s, X0 + 0.35, yy + (h - d) / 2, d, str(i + 1), i=i, size=22)
            k.text(s, X0 + 1.5, yy + 0.05, 2.9, h - 0.1, head, size=18, bold=True,
                   color=t.primary, anchor="m", font="+mj-lt")
            k.text(s, X0 + 4.5, yy + 0.05, W - 4.85, h - 0.1, desc, size=16, color=t.text,
                   anchor="m", line_spacing=1.2)
        return s

    def two_col(self, title, cols, kicker=None, notes=None):
        s, y = self._content(title, kicker)
        t = self.t
        cw = (W - 0.4) / 2
        for i, (ic, head, items) in enumerate(cols):
            x = X0 + i * (cw + 0.4)
            t.card(s, x, y, cw, Y_END - y, i=i, name=f"Kolom {i + 1}")
            t.icon_disc(s, ic, x + 0.4, y + 0.4, 0.75, i=i)
            k.text(s, x + 1.35, y + 0.4, cw - 1.7, 0.75, head, size=22, bold=True,
                   color=t.primary, anchor="m", font="+mj-lt")
            k.bullets(s, x + 0.45, y + 1.5, cw - 0.9, Y_END - y - 1.7, items, size=16,
                      color=t.text, bullet_color=t.accent, para_after=14, line_spacing=1.2)
        return s

    def icon_grid(self, title, items, kicker=None, notes=None, lead=None):
        s, y = self._content(title, kicker)
        t = self.t
        if lead:
            t.body(s, X0, y - 0.15, W, 0.5, lead, size=15, color=t.muted)
            y += 0.55
        cols = 2 if len(items) == 4 else 3
        rows = (len(items) + cols - 1) // cols
        gap = 0.3
        cw = (W - gap * (cols - 1)) / cols
        ch = (Y_END - y - gap * (rows - 1)) / rows
        for i, (ic, head, desc) in enumerate(items):
            r, c = divmod(i, cols)
            x, yy = X0 + c * (cw + gap), y + r * (ch + gap)
            t.card(s, x, yy, cw, ch, i=i, name=f"Kartu {i + 1}")
            d = 0.8
            t.icon_disc(s, ic, x + 0.4, yy + 0.4, d, i=i)
            k.text(s, x + 1.5, yy + 0.4, cw - 1.8, 0.45, head, size=20, bold=True,
                   color=t.primary, font="+mj-lt")
            k.text(s, x + 1.5, yy + 0.9, cw - 1.8, ch - 1.0, desc, size=16, color=t.text,
                   line_spacing=1.2)
        return s

    def table_slide(self, title, rows, col_widths=None, kicker=None, notes=None, note=None,
                    align=None, row_h=None):
        s, y = self._content(title, kicker)
        t = self.t
        row_h = row_h or min(0.72, (Y_END - y - (0.6 if note else 0)) / len(rows))
        widths = col_widths or [W / len(rows[0])] * len(rows[0])
        scale = W / sum(widths)
        widths = [w * scale for w in widths]
        head_fill = t.accent if not t.dark else "dk2"
        head_color = t.on_accent if not t.dark else "accent1"
        band = None if t.dark else t.surface
        k.table(s, t, X0, y, W, rows, col_widths=widths, row_h=row_h, header_fill=head_fill,
                header_color=head_color, band_fill=band, size=14, header_size=14,
                line_color=t.grid, align=align, bold_first_col=True,
                body_fill=("dk1" if t.dark else None))
        if note:
            k.text(s, X0, Y_END - 0.35, W, 0.35, note, size=11, italic=True, color=t.muted)
        return s

    def flow(self, title, inputs, output, labels, caption, kicker=None, notes=None):
        s, y = self._content(title, kicker)
        t = self.t
        n = len(inputs)
        bw, bh, gap = 3.9, 1.25, 0.45
        total = n * bh + (n - 1) * gap
        top = y + (Y_END - 0.9 - y - total) / 2
        ox, ow, oh = 8.1, 4.1, 1.8
        oy = top + total / 2 - oh / 2
        for i, (head, sub) in enumerate(inputs):
            yy = top + i * (bh + gap)
            t.card(s, X0 + 0.4, yy, bw, bh, i=i, name=f"Variabel {i + 1}")
            k.text(s, X0 + 0.7, yy + 0.2, bw - 0.6, 0.45, head, size=18, bold=True,
                   color=t.primary, font="+mj-lt")
            k.text(s, X0 + 0.7, yy + 0.67, bw - 0.6, 0.4, sub, size=14, color=t.muted)
            sx, sy = X0 + 0.4 + bw, yy + bh / 2
            k.line(s, sx + 0.1, sy, ox - 0.12, oy + oh / 2, t.accent, 2.0, arrow=True,
                   name=f"Panah {labels[i]}")
            mx = (sx + ox) / 2
            my = (sy + oy + oh / 2) / 2
            t.badge(s, mx - 0.3, my - 0.3, 0.6, labels[i], i=i, size=13)
        k.rrect(s, ox, oy, ow, oh, t.accent if not t.dark else "dk2", radius=t.card_radius,
                name="Variabel terikat", line=("accent1" if t.dark else None))
        k.text(s, ox + 0.3, oy + 0.25, ow - 0.6, 0.6, output[0], size=20, bold=True,
               color=t.on_accent if not t.dark else "accent1", font="+mj-lt", align="c")
        k.text(s, ox + 0.3, oy + 0.85, ow - 0.6, 0.5, output[1], size=14,
               color=t.on_accent if not t.dark else "lt1", align="c")
        k.text(s, X0, Y_END - 0.7, W, 0.6, caption, size=15, italic=True, color=t.muted,
               align="c")
        return s

    def steps(self, title, items, kicker=None, notes=None):
        s, y = self._content(title, kicker)
        t = self.t
        n = len(items)
        cw = W / n
        d = 1.0
        cy = y + 0.2
        k.line(s, X0 + cw / 2, cy + d / 2, X1 - cw / 2, cy + d / 2, t.grid, 2.0,
               dash=MSO_LINE_DASH_STYLE.DASH, name="Garis alur")
        for i, (ic, head, desc) in enumerate(items):
            cx = X0 + i * cw + cw / 2
            fill = t.accent if not t.dark else "dk2"
            k.oval(s, cx - d / 2, cy, d, d, fill, name=f"Tahap {i + 1}",
                   line=("accent1" if t.dark else t.bg), line_w=(1.25 if t.dark else 4))
            k.icon(s, t, ic, cx - 0.26, cy + 0.24, 0.52, t.on_accent if not t.dark else "accent1")
            k.text(s, cx - cw / 2 + 0.1, cy + d + 0.25, cw - 0.2, 0.3, f"TAHAP {i + 1}",
                   size=11, bold=True, color=t.accent, align="c", spacing=1.5)
            k.text(s, cx - cw / 2 + 0.1, cy + d + 0.6, cw - 0.2, 0.75, head, size=17, bold=True,
                   color=t.primary, align="c", font="+mj-lt", line_spacing=1.0)
            t.card(s, cx - cw / 2 + 0.12, cy + d + 1.45, cw - 0.24, Y_END - (cy + d + 1.45), i=i,
                   name=f"Keterangan {i + 1}")
            k.text(s, cx - cw / 2 + 0.3, cy + d + 1.6, cw - 0.6, Y_END - (cy + d + 1.75), desc,
                   size=14, color=t.text, align="c", line_spacing=1.15)
        return s

    def cards3(self, title, items, kicker=None, notes=None):
        s, y = self._content(title, kicker)
        t = self.t
        n = len(items)
        gap = 0.35
        cw = (W - gap * (n - 1)) / n
        h = Y_END - y
        for i, (ic, head, value, desc) in enumerate(items):
            x = X0 + i * (cw + gap)
            t.card(s, x, y, cw, h, i=i, name=f"Kartu {i + 1}")
            t.icon_disc(s, ic, x + 0.4, y + 0.4, 0.75, i=i)
            k.text(s, x + 0.4, y + 1.35, cw - 0.8, 0.4, head, size=13, bold=True, color=t.muted,
                   caps=True, spacing=1.5)
            # ukuran judul seragam per slide, mengikuti judul terpanjang
            longest = max(len(it[2]) for it in items)
            size = 28 if longest * 0.19 <= cw - 0.8 else 24
            two = longest * 0.145 > cw - 0.8
            k.text(s, x + 0.4, y + 1.75, cw - 0.8, 1.2 if two else 0.8, value,
                   size=size, bold=True, color=t.primary, font="+mj-lt", line_spacing=1.0)
            dy = 3.0 if two else 2.6
            k.text(s, x + 0.4, y + dy, cw - 0.8, h - dy - 0.2, desc, size=16, color=t.text,
                   line_spacing=1.2)
        return s

    def chart_bar(self, title, categories, series, insights, kicker=None, notes=None,
                  number_format="0.0", chart_title=None):
        s, y = self._content(title, kicker)
        t = self.t
        cw = 7.7
        t.card(s, X0, y, cw, Y_END - y, i=0, name="Panel grafik", fill=self._panel())
        if chart_title:
            k.text(s, X0 + 0.35, y + 0.2, cw - 0.7, 0.4, chart_title, size=14, bold=True,
                   color=t.primary)
        legend = XL_LEGEND_POSITION.TOP if len(series) > 1 else None
        k.chart(s, t, XL_CHART_TYPE.COLUMN_CLUSTERED, X0 + 0.2, y + 0.6, cw - 0.4,
                Y_END - y - 0.75, categories, series, colors=list(t.series), legend=legend,
                number_format=number_format, label_pos=XL_LABEL_POSITION.OUTSIDE_END,
                gap=70, overlap=-10, axis_format="0")
        x = X0 + cw + 0.35
        n = len(insights)
        gap = 0.3
        h = (Y_END - y - gap * (n - 1)) / n
        for i, (val, label) in enumerate(insights):
            yy = y + i * (h + gap)
            t.card(s, x, yy, X1 - x, h, i=i + 1, name=f"Temuan {i + 1}")
            k.text(s, x + 0.35, yy + 0.2, X1 - x - 0.7, 0.75, val, size=34, bold=True,
                   color=t.accent, font="+mj-lt")
            k.text(s, x + 0.35, yy + 0.95, X1 - x - 0.7, h - 1.05, label, size=15, color=t.text,
                   line_spacing=1.15)
        return s

    def chart_mix(self, title, pie, line, kicker=None, notes=None):
        s, y = self._content(title, kicker)
        t = self.t
        lw = 5.0
        h = Y_END - y
        t.card(s, X0, y, lw, h, i=0, name="Panel diagram lingkar", fill=self._panel())
        k.text(s, X0 + 0.35, y + 0.2, lw - 0.7, 0.4, pie["title"], size=14, bold=True,
               color=t.primary)
        k.chart(s, t, XL_CHART_TYPE.DOUGHNUT, X0 + 0.2, y + 0.65, lw - 0.4, h - 0.85,
                pie["categories"], [("Data", pie["values"])], colors=list(t.series),
                legend=XL_LEGEND_POSITION.BOTTOM, number_format='0"%"',
                label_color=("dk1" if t.dark else "lt1"))
        x = X0 + lw + 0.35
        rw = X1 - x
        t.card(s, x, y, rw, h, i=1, name="Panel grafik garis", fill=self._panel())
        k.text(s, x + 0.35, y + 0.2, rw - 0.7, 0.4, line["title"], size=14, bold=True,
               color=t.primary)
        k.chart(s, t, XL_CHART_TYPE.LINE_MARKERS, x + 0.2, y + 0.65, rw - 0.4, h - 0.85,
                line["categories"], line["series"], colors=list(t.series),
                legend=XL_LEGEND_POSITION.TOP, number_format="0", labels=False,
                axis_min=line.get("min"))
        return s

    def photos(self, title, captions, kicker=None, notes=None):
        s, y = self._content(title, kicker)
        t = self.t
        n = len(captions)
        gap = 0.35
        cw = (W - gap * (n - 1)) / n
        ph = Y_END - y - 0.6
        for i, cap in enumerate(captions):
            x = X0 + i * (cw + gap)
            box = k.rrect(s, x, y, cw, ph, t.surface if not t.dark else "dk2",
                          radius=t.card_radius, line=t.grid, line_w=1.0,
                          dash=MSO_LINE_DASH_STYLE.DASH,
                          name=f"Foto {i + 1} (Format Shape > Fill > Picture)")
            k.icon(s, t, "image-plus", x + cw / 2 - 0.4, y + ph / 2 - 0.65, 0.8, t.muted)
            k.text(s, x + 0.2, y + ph / 2 + 0.3, cw - 0.4, 0.6,
                   "Klik kanan kotak > Format Shape > Fill > Picture", size=11, color=t.muted,
                   align="c")
            k.text(s, x, y + ph + 0.15, cw, 0.4, cap, size=13, bold=True, color=t.text, align="c")
        return s

    def discussion(self, title, quote, source, points, kicker=None, notes=None):
        s, y = self._content(title, kicker)
        t = self.t
        qw = 5.3
        h = Y_END - y
        k.rrect(s, X0, y, qw, h, t.accent if not t.dark else "dk2", radius=t.card_radius,
                name="Kutipan", line=("accent1" if t.dark else None))
        qc = t.on_accent if not t.dark else "accent1"
        k.icon(s, t, "quote", X0 + 0.45, y + 0.45, 0.7, qc)
        k.text(s, X0 + 0.45, y + 1.35, qw - 0.9, h - 2.3, quote, size=21, bold=True, color=qc,
               font="+mj-lt", line_spacing=1.2)
        k.text(s, X0 + 0.45, Y_END - 0.85, qw - 0.9, 0.5, source, size=13,
               color=(t.on_accent if not t.dark else "lt1"))
        x = X0 + qw + 0.5
        k.bullets(s, x, y + 0.1, X1 - x, h - 0.1, points, size=18, color=t.text,
                  bullet_color=t.accent, para_after=22, line_spacing=1.25)
        return s

    def conclusion(self, title, left, right, kicker=None, notes=None):
        s, y = self._content(title, kicker)
        t = self.t
        cw = (W - 0.4) / 2
        for ci, (ic, head, items) in enumerate((left, right)):
            x = X0 + ci * (cw + 0.4)
            t.card(s, x, y, cw, Y_END - y, i=ci, name=head)
            t.icon_disc(s, ic, x + 0.4, y + 0.35, 0.7, i=ci)
            k.text(s, x + 1.3, y + 0.35, cw - 1.6, 0.7, head, size=22, bold=True,
                   color=t.primary, anchor="m", font="+mj-lt")
            yy = y + 1.35
            step = (Y_END - yy - 0.2) / len(items)
            for j, item in enumerate(items):
                t.badge(s, x + 0.45, yy + j * step + 0.02, 0.42, str(j + 1), i=ci, size=12)
                k.text(s, x + 1.1, yy + j * step, cw - 1.45, step - 0.1, item, size=16,
                       color=t.text, line_spacing=1.15)
        return s

    def references(self, title, refs, kicker=None, notes=None):
        s, y = self._content(title, kicker)
        t = self.t
        box = s.shapes.add_textbox(*(k.Inches(v) for v in (X0, y, W, Y_END - y)))
        tf = box.text_frame
        tf.word_wrap = True
        for side in ("left", "right", "top", "bottom"):
            setattr(tf, f"margin_{side}", 0)
        for i, ref in enumerate(refs):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.space_after = k.Pt(14)
            p.line_spacing = 1.2
            pPr = p._p.get_or_add_pPr()
            pPr.set("marL", str(k.Inches(0.5)))
            pPr.set("indent", str(-k.Inches(0.5)))
            author, _, rest = ref.partition(". ")
            for txt, b in ((author + ". ", True), (rest, False)):
                r = p.add_run()
                r.text = txt
                r.font.size = k.Pt(16)
                r.font.bold = b
                k.set_color(r.font.color, t.text)
        box.name = "Daftar pustaka (format APA)"
        return s

    def hypotheses(self, title, items, kicker=None, notes=None):
        s, y = self._content(title, kicker)
        t = self.t
        n = len(items)
        gap = 0.3
        h = (Y_END - y - gap * (n - 1)) / n
        for i, (code, desc) in enumerate(items):
            yy = y + i * (h + gap)
            t.card(s, X0, yy, W, h, i=i, name=f"Hipotesis {code}")
            d = min(0.9, h - 0.3)
            t.badge(s, X0 + 0.35, yy + (h - d) / 2, d, code, i=i, size=18)
            k.text(s, X0 + 1.6, yy, W - 1.95, h, desc, size=16, color=t.text, anchor="m",
                   line_spacing=1.2)
        return s

    def gantt(self, title, months, rows, kicker=None, notes=None):
        s, y = self._content(title, kicker)
        t = self.t
        label_w = 3.4
        cols = len(months)
        cw = (W - label_w) / cols
        n = len(rows)
        rh = (Y_END - y - 0.5) / n
        for j, m in enumerate(months):
            k.text(s, X0 + label_w + j * cw, y, cw, 0.4, m, size=12, bold=True, color=t.muted,
                   align="c", anchor="m")
        for i, (name, start, end) in enumerate(rows):
            yy = y + 0.5 + i * rh
            if i % 2 == 0:
                k.rect(s, X0, yy, W, rh, t.surface if not t.dark else "dk2", name="Baris")
            k.text(s, X0 + 0.15, yy, label_w - 0.2, rh, name, size=15, color=t.text, anchor="m")
            bar = k.rrect(s, X0 + label_w + start * cw + 0.06, yy + rh * 0.22,
                          (end - start + 1) * cw - 0.12, rh * 0.56,
                          t.series[i % len(t.series)], radius=rh * 0.28, name=f"Durasi {name}")
        return s

    # ------------------------------------------------------------ tambahan paket kuliah
    def team(self, title, members, kicker=None, notes=None):
        s, y = self._content(title, kicker)
        t = self.t
        n = len(members)
        gap = 0.3
        cw = (W - gap * (n - 1)) / n
        h = Y_END - y
        for i, (name, nim, role) in enumerate(members):
            x = X0 + i * (cw + gap)
            t.card(s, x, y, cw, h, i=i, name=f"Anggota {i + 1}")
            d = min(1.5, cw - 0.8)
            t.icon_disc(s, "user", x + (cw - d) / 2, y + 0.45, d, i=i)
            k.text(s, x + 0.15, y + d + 0.7, cw - 0.3, 0.8, name, size=17, bold=True,
                   color=t.primary, align="c", font="+mj-lt", line_spacing=1.0, anchor="b")
            k.text(s, x + 0.15, y + d + 1.55, cw - 0.3, 0.35, nim, size=13, color=t.muted,
                   align="c")
            k.text(s, x + 0.15, y + d + 2.0, cw - 0.3, 0.4, role, size=13, bold=True,
                   color=t.accent, align="c", caps=True, spacing=1)
        return s

    def quotes(self, title, items, kicker=None, notes=None):
        s, y = self._content(title, kicker)
        t = self.t
        n = len(items)
        gap = 0.35
        cw = (W - gap * (n - 1)) / n
        h = Y_END - y
        for i, (quote, author) in enumerate(items):
            x = X0 + i * (cw + gap)
            t.card(s, x, y, cw, h, i=i, name=f"Definisi {i + 1}")
            k.icon(s, t, "quote", x + 0.4, y + 0.4, 0.6, t.accent)
            k.text(s, x + 0.4, y + 1.2, cw - 0.8, h - 2.2, quote, size=16, italic=True,
                   color=t.text, line_spacing=1.3)
            k.text(s, x + 0.4, Y_END - 0.85, cw - 0.8, 0.5, author, size=15, bold=True,
                   color=t.primary, font="+mj-lt")
        return s

    def timeline(self, title, items, kicker=None, notes=None):
        s, y = self._content(title, kicker)
        t = self.t
        n = len(items)
        cw = W / n
        mid = y + (Y_END - y) / 2
        k.line(s, X0, mid, X1, mid, t.grid, 3.0, name="Garis waktu")
        for i, (year, head, desc) in enumerate(items):
            cx = X0 + i * cw + cw / 2
            d = 0.36
            k.oval(s, cx - d / 2, mid - d / 2, d, d, t.series[i % len(t.series)],
                   line=t.bg, line_w=3, name=f"Titik {year}")
            up = i % 2 == 0
            ty = mid - 2.15 if up else mid + 0.45
            ty = mid - 2.3 if up else mid + 0.45
            k.text(s, cx - cw / 2 + 0.05, ty, cw - 0.1, 0.6, year, size=30, bold=True,
                   color=t.primary, align="c", font="+mj-lt")
            k.text(s, cx - cw / 2 + 0.05, ty + 0.65, cw - 0.1, 0.4, head, size=17, bold=True,
                   color=t.accent if not getattr(t, "FILLS", None) else t.primary, align="c")
            k.text(s, cx - cw / 2 + 0.05, ty + 1.08, cw - 0.1, 0.75, desc, size=14,
                   color=t.muted, align="c", line_spacing=1.1)
        return s

    def compare(self, title, left, right, kicker=None, notes=None):
        s, y = self._content(title, kicker)
        t = self.t
        gap = 0.9
        cw = (W - gap) / 2
        h = Y_END - y
        for ci, (ic, head, items) in enumerate((left, right)):
            x = X0 + ci * (cw + gap)
            t.card(s, x, y, cw, h, i=ci, name=head)
            t.icon_disc(s, ic, x + 0.4, y + 0.35, 0.7, i=ci)
            k.text(s, x + 1.3, y + 0.35, cw - 1.6, 0.7, head, size=22, bold=True,
                   color=t.primary, anchor="m", font="+mj-lt")
            k.bullets(s, x + 0.45, y + 1.4, cw - 0.9, h - 1.6, items, size=16, color=t.text,
                      bullet_color=t.series[ci], para_after=12, line_spacing=1.2)
        d = 0.8
        t.badge(s, X0 + cw + (gap - d) / 2, y + h / 2 - d / 2, d, "VS", size=18)
        return s

    # ------------------------------------------------------------ tambahan pitch deck
    def _photo(self, s, x, y, w, h, label):
        if hasattr(self.t, "photo"):
            return self.t.photo(s, x, y, w, h, label=label)
        return k.rrect(s, x, y, w, h, self.t.surface, radius=self.t.card_radius,
                       name=f"{label} (Format Shape > Fill > Picture)")

    def image_text(self, title, heading, points, photo="Foto produk", kicker=None,
                   notes=None, lead=None):
        s, y = self._content(title, kicker)
        t = self.t
        pw = 5.4
        self._photo(s, X0, y, pw, Y_END - y, photo)
        x = X0 + pw + 0.6
        k.text(s, x, y + 0.05, X1 - x, 0.9, heading, size=24, bold=True, color=t.primary,
               font="+mj-lt", line_spacing=1.05)
        yy = y + 1.1
        if lead:
            k.text(s, x, yy, X1 - x, 0.9, lead, size=15, color=t.muted, line_spacing=1.25)
            yy += 1.0
        n = len(points)
        step = (Y_END - yy) / n
        for i, (ic, head, desc) in enumerate(points):
            py = yy + i * step
            t.icon_disc(s, ic, x, py, 0.6, i=i)
            k.text(s, x + 0.85, py - 0.02, X1 - x - 0.85, 0.4, head, size=17, bold=True,
                   color=t.primary)
            k.text(s, x + 0.85, py + 0.38, X1 - x - 0.85, step - 0.45, desc, size=14,
                   color=t.text, line_spacing=1.15)
        return s

    def market(self, title, levels, note=None, kicker=None, notes=None):
        """TAM / SAM / SOM: lingkaran konsentris + keterangan."""
        s, y = self._content(title, kicker)
        t = self.t
        h = Y_END - y
        cx, cy = X0 + 2.6, y + h / 2
        tones = list(t.series[:3])[::-1]
        for i, (lvl, val, desc) in enumerate(levels):
            r = h / 2 * (1 - i * 0.3)
            k.oval(s, cx - r, cy - r, 2 * r, 2 * r, tones[i] if i else t.surface,
                   line=t.grid if i == 0 else None, name=f"Lingkaran {lvl}")
        k.text(s, cx - 1.0, cy - 0.35, 2.0, 0.7, levels[-1][0], size=18, bold=True,
               color="lt1" if not t.dark else "dk1", align="c", anchor="m")
        x = X0 + 6.0
        rowh = h / len(levels)
        for i, (lvl, val, desc) in enumerate(levels):
            yy = y + i * rowh
            k.text(s, x, yy + 0.1, 1.4, 0.5, lvl, size=16, bold=True, color=t.accent,
                   spacing=1.5)
            k.text(s, x + 1.4, yy, X1 - x - 1.4, 0.7, val, size=30, bold=True,
                   color=t.primary, font="+mj-lt")
            k.text(s, x + 1.4, yy + 0.7, X1 - x - 1.4, rowh - 0.8, desc, size=14,
                   color=t.muted, line_spacing=1.15)
            if i < len(levels) - 1:
                k.line(s, x, yy + rowh - 0.08, X1, yy + rowh - 0.08, t.grid, 0.75,
                       name="Pemisah")
        if note:
            k.text(s, X0, Y_END + 0.02, W, 0.3, note, size=10, italic=True, color=t.muted)
        return s

    def check_table(self, title, headers, rows, kicker=None, notes=None, highlight=1):
        """Tabel perbandingan kompetitor: ✓ / – per fitur, kolom kita disorot."""
        s, y = self._content(title, kicker)
        t = self.t
        n = len(headers)
        first = 4.2
        cw = (W - first) / (n - 1)
        rh = min(0.62, (Y_END - y) / (len(rows) + 1))
        hx = X0 + first + (highlight - 1) * cw
        t.card(s, hx, y - 0.1, cw, rh * (len(rows) + 1) + 0.2, name="Sorotan kolom kita")
        for j, hd in enumerate(headers):
            x = X0 if j == 0 else X0 + first + (j - 1) * cw
            k.text(s, x + (0 if j == 0 else 0.05), y, (first if j == 0 else cw - 0.1), rh,
                   hd, size=14, bold=True, color=t.primary, align="l" if j == 0 else "c",
                   anchor="m")
        for i, row in enumerate(rows):
            yy = y + (i + 1) * rh
            k.line(s, X0, yy, X1, yy, t.grid, 0.75, name="Garis")
            for j, val in enumerate(row):
                x = X0 if j == 0 else X0 + first + (j - 1) * cw
                if j and val in ("v", "x"):
                    ic = "check" if val == "v" else "minus"
                    col = t.accent if val == "v" else t.grid
                    k.icon(s, t, ic, x + cw / 2 - 0.17, yy + rh / 2 - 0.17, 0.34, col)
                else:
                    k.text(s, x + (0 if j == 0 else 0.05), yy, (first if j == 0 else cw - 0.1),
                           rh, val, size=14, color=t.text, align="l" if j == 0 else "c",
                           anchor="m", bold=(j == highlight))
        return s

    def funds(self, title, amount, caption, uses, kicker=None, notes=None):
        """Kebutuhan dana: angka besar + diagram penggunaan dana."""
        s, y = self._content(title, kicker)
        t = self.t
        lw = 5.2
        t.card(s, X0, y, lw, Y_END - y, name="Total dana")
        k.text(s, X0 + 0.45, y + 0.45, lw - 0.9, 0.4, "Kebutuhan dana", size=13, bold=True,
               color=t.muted, caps=True, spacing=1.5)
        k.text(s, X0 + 0.45, y + 0.9, lw - 0.9, 1.2, amount, size=46, bold=True,
               color=t.primary, font="+mj-lt")
        k.text(s, X0 + 0.45, y + 2.2, lw - 0.9, Y_END - y - 2.5, caption, size=15,
               color=t.text, line_spacing=1.3)
        x = X0 + lw + 0.5
        cats = [u[0] for u in uses]
        vals = tuple(u[1] for u in uses)
        k.chart(s, t, XL_CHART_TYPE.DOUGHNUT, x, y, 3.6, Y_END - y, cats, [("Dana", vals)],
                colors=list(t.series), legend=None, number_format='0"%"', labels=False)
        lx = x + 3.9
        step = (Y_END - y) / len(uses)
        for i, (cat, val, desc) in enumerate(uses):
            yy = y + i * step + 0.1
            k.oval(s, lx, yy + 0.12, 0.22, 0.22, t.series[i % len(t.series)],
                   name="Penanda warna")
            k.text(s, lx + 0.35, yy, X1 - lx - 0.35, 0.45,
                   [[dict(text=f"{val}%  ", bold=True, color=t.primary),
                     dict(text=cat, bold=True)]], size=15, color=t.text)
            k.text(s, lx + 0.35, yy + 0.42, X1 - lx - 0.35, step - 0.5, desc, size=12,
                   color=t.muted)
        return s

    def team_photo(self, title, members, kicker=None, notes=None):
        s, y = self._content(title, kicker)
        t = self.t
        n = len(members)
        gap = 0.4
        cw = (W - gap * (n - 1)) / n
        ph = min(cw, Y_END - y - 1.4)
        for i, (name, role, bio) in enumerate(members):
            x = X0 + i * (cw + gap)
            self._photo(s, x + (cw - ph) / 2, y, ph, ph, "Foto")
            k.text(s, x, y + ph + 0.15, cw, 0.45, name, size=17, bold=True, color=t.primary,
                   align="c", font="+mj-lt")
            k.text(s, x, y + ph + 0.55, cw, 0.35, role, size=12, bold=True, color=t.accent,
                   align="c", caps=True, spacing=1.5)
            k.text(s, x + 0.1, y + ph + 0.9, cw - 0.2, Y_END - (y + ph + 0.9), bio, size=12,
                   color=t.muted, align="c", line_spacing=1.1)
        return s

    # ------------------------------------------------------------ tambahan company profile
    def stats4(self, title, stats, lead=None, kicker=None, notes=None):
        """Empat angka pencapaian besar."""
        s, y = self._content(title, kicker)
        t = self.t
        if lead:
            k.text(s, X0, y - 0.1, W * 0.7, 0.9, lead, size=16, color=t.muted,
                   line_spacing=1.3)
            y += 1.0
        n = len(stats)
        gap = 0.3
        cw = (W - gap * (n - 1)) / n
        h = Y_END - y
        longest = max(len(v[0]) for v in stats)
        vsize = 44
        while vsize > 26 and longest * vsize * 0.0075 > cw - 0.7:  # perkiraan lebar teks
            vsize -= 2
        for i, (val, label, desc) in enumerate(stats):
            x = X0 + i * (cw + gap)
            t.card(s, x, y, cw, h, name=f"Angka {i + 1}")
            k.text(s, x + 0.35, y + 0.35, cw - 0.7, 1.1, val, size=vsize, bold=True,
                   color=t.primary, font="+mj-lt", anchor="b")
            k.text(s, x + 0.35, y + 1.5, cw - 0.7, 0.4, label, size=13, bold=True,
                   color=t.accent, caps=True, spacing=1.5)
            k.text(s, x + 0.35, y + 1.95, cw - 0.7, h - 2.1, desc, size=14, color=t.text,
                   line_spacing=1.2)
        return s

    def logos(self, title, names, lead=None, kicker=None, notes=None):
        """Kisi logo klien/mitra (kotak tempat logo)."""
        s, y = self._content(title, kicker)
        t = self.t
        if lead:
            k.text(s, X0, y - 0.1, W, 0.6, lead, size=16, color=t.muted)
            y += 0.7
        cols = 4
        rows = (len(names) + cols - 1) // cols
        gap = 0.3
        cw = (W - gap * (cols - 1)) / cols
        ch = (Y_END - y - gap * (rows - 1)) / rows
        for i, nm in enumerate(names):
            r, c = divmod(i, cols)
            x, yy = X0 + c * (cw + gap), y + r * (ch + gap)
            t.card(s, x, yy, cw, ch, name=f"Logo {nm} (ganti dengan logo)")
            k.icon(s, t, "building-2", x + cw / 2 - 0.25, yy + ch / 2 - 0.45, 0.5, t.muted)
            k.text(s, x, yy + ch / 2 + 0.12, cw, 0.4, nm, size=14, bold=True, color=t.muted,
                   align="c", caps=True, spacing=1.5)
        return s

    def org_chart(self, title, top, middle, bottom=None, kicker=None, notes=None):
        """Struktur organisasi 2–3 tingkat dengan garis penghubung."""
        s, y = self._content(title, kicker)
        t = self.t
        bw, bh = 2.7, 0.95
        levels = [[top], middle] + ([bottom] if bottom else [])
        gaps = (Y_END - y - bh * len(levels)) / max(1, len(levels) - 1)
        centers = []
        for li, row in enumerate(levels):
            yy = y + li * (bh + gaps)
            n = len(row)
            span = W / n
            cs = []
            for i, (name, role) in enumerate(row):
                cx = X0 + span * i + span / 2
                fill = t.badge_fill if li == 0 and hasattr(t, "badge_fill") else None
                if li == 0:
                    box = k.rrect(s, cx - bw / 2, yy, bw, bh, t.primary if not t.dark else
                                  "accent1", radius=t.card_radius, name=f"Jabatan {role}")
                    ink, sub = ("lt1", "lt1") if not t.dark else ("dk1", "dk1")
                else:
                    t.card(s, cx - bw / 2, yy, bw, bh, name=f"Jabatan {role}")
                    ink, sub = t.primary, t.muted
                k.text(s, cx - bw / 2, yy + 0.1, bw, 0.4, role, size=12, bold=True,
                       color=sub if li else ink, align="c", caps=True, spacing=1)
                k.text(s, cx - bw / 2, yy + 0.45, bw, 0.4, name, size=15, bold=True,
                       color=ink, align="c")
                cs.append((cx, yy))
            centers.append(cs)
        for li in range(1, len(centers)):
            py = centers[li - 1][0][1] + bh
            cy = centers[li][0][1]
            mid = py + (cy - py) / 2
            parents = centers[li - 1]
            children = centers[li]
            # garis dari induk (atau bagian tengah tingkat sebelumnya) ke anak
            for px, _ in parents:
                k.line(s, px, py, px, mid, t.grid, 1.5, name="Garis struktur")
            xs = [c[0] for c in children] + [p[0] for p in parents]
            k.line(s, min(xs), mid, max(xs), mid, t.grid, 1.5, name="Garis struktur")
            for cx, cyy in children:
                k.line(s, cx, mid, cx, cyy, t.grid, 1.5, name="Garis struktur")
        return s

    def contact_map(self, title, address, items, kicker=None, notes=None):
        s, y = self._content(title, kicker)
        t = self.t
        mw = 6.6
        self._photo(s, X0, y, mw, Y_END - y, "Peta lokasi (tempel tangkapan layar Google Maps)")
        x = X0 + mw + 0.6
        k.text(s, x, y + 0.05, X1 - x, 0.4, "Alamat", size=13, bold=True, color=t.accent,
               caps=True, spacing=1.5)
        k.text(s, x, y + 0.5, X1 - x, 1.2, address, size=17, color=t.primary,
               line_spacing=1.3, font="+mj-lt")
        yy = y + 1.95
        for ic, label in items:
            t.icon_disc(s, ic, x, yy, 0.55)
            k.text(s, x + 0.75, yy, X1 - x - 0.75, 0.55, label, size=15, color=t.text,
                   anchor="m")
            yy += 0.78
        return s

    # ------------------------------------------------------------ tambahan materi ajar
    def big_question(self, title, question, hint=None, kicker=None, notes=None):
        """Pertanyaan pemantik: satu pertanyaan besar di tengah."""
        s, y = self._content(title, kicker)
        t = self.t
        t.card(s, X0, y, W, Y_END - y, name="Pertanyaan")
        k.icon(s, t, "circle-help", X0 + W / 2 - 0.45, y + 0.4, 0.9, t.accent)
        k.text(s, X0 + 0.8, y + 1.45, W - 1.6, 2.0, question, size=32, color=t.primary,
               font="+mj-lt", align="c", anchor="m", line_spacing=1.15)
        if hint:
            k.text(s, X0 + 0.8, Y_END - 1.0, W - 1.6, 0.6, hint, size=15, italic=True,
                   color=t.muted, align="c")
        return s

    def quiz(self, title, question, options, answer=None, kicker=None, notes=None):
        """Soal pilihan ganda A–D; bila `answer` diisi, pilihan itu disorot."""
        s, y = self._content(title, kicker)
        t = self.t
        k.text(s, X0, y, W, 1.0, question, size=24, color=t.primary, font="+mj-lt",
               line_spacing=1.15)
        oy = y + 1.25
        gap = 0.3
        cw = (W - gap) / 2
        ch = (Y_END - oy - gap) / 2
        for i, opt in enumerate(options):
            r, c = divmod(i, 2)
            x, yy = X0 + c * (cw + gap), oy + r * (ch + gap)
            letter = "ABCD"[i]
            right = answer == letter
            if right:
                k.rrect(s, x, yy, cw, ch, t.primary if not t.dark else "accent1",
                        radius=t.card_radius, name=f"Pilihan {letter} (benar)")
                ink = "lt1" if not t.dark else "dk1"
            else:
                t.card(s, x, yy, cw, ch, name=f"Pilihan {letter}")
                ink = t.text
            t.badge(s, x + 0.35, yy + ch / 2 - 0.35, 0.7, letter, size=18,
                    fill=(("dk1" if t.dark else "lt1") if right else None),
                    color=(("accent1" if t.dark else t.primary) if right else None))
            k.text(s, x + 1.3, yy, cw - 1.6, ch, opt, size=18, color=ink, anchor="m")
            if right:
                k.icon(s, t, "circle-check", x + cw - 0.75, yy + ch / 2 - 0.25, 0.5, ink)
        return s

    def example(self, title, problem, steps, result, kicker=None, notes=None):
        """Contoh soal + langkah pembahasan."""
        s, y = self._content(title, kicker)
        t = self.t
        lw = 5.0
        t.card(s, X0, y, lw, Y_END - y, name="Soal")
        k.text(s, X0 + 0.4, y + 0.35, lw - 0.8, 0.4, "Soal", size=13, bold=True,
               color=t.accent, caps=True, spacing=1.5)
        k.text(s, X0 + 0.4, y + 0.8, lw - 0.8, Y_END - y - 1.1, problem, size=17,
               color=t.text, line_spacing=1.3)
        x = X0 + lw + 0.5
        k.text(s, x, y, X1 - x, 0.4, "Pembahasan", size=13, bold=True, color=t.accent,
               caps=True, spacing=1.5)
        yy = y + 0.55
        step = (Y_END - yy - 0.95) / len(steps)
        for i, st in enumerate(steps, 1):
            t.badge(s, x, yy + 0.02, 0.45, str(i), size=12)
            k.text(s, x + 0.65, yy, X1 - x - 0.65, step - 0.05, st, size=16, color=t.text,
                   line_spacing=1.2)
            yy += step
        box = k.rrect(s, x, Y_END - 0.8, X1 - x, 0.8, t.primary if not t.dark else "accent1",
                      radius=t.card_radius, name="Jawaban akhir")
        k.text(s, x + 0.3, Y_END - 0.8, X1 - x - 0.6, 0.8, result, size=18, bold=True,
               color="lt1" if not t.dark else "dk1", anchor="m")
        return s

    def reflection(self, title, prompts, kicker=None, notes=None):
        """Refleksi akhir pelajaran: tiga pertanyaan dengan ruang jawaban."""
        s, y = self._content(title, kicker)
        t = self.t
        n = len(prompts)
        gap = 0.35
        cw = (W - gap * (n - 1)) / n
        h = Y_END - y
        for i, (ic, prompt) in enumerate(prompts):
            x = X0 + i * (cw + gap)
            t.card(s, x, y, cw, h, name=f"Refleksi {i + 1}")
            t.icon_disc(s, ic, x + 0.4, y + 0.4, 0.75)
            k.text(s, x + 0.4, y + 1.4, cw - 0.8, 1.2, prompt, size=18, bold=True,
                   color=t.primary, line_spacing=1.2)
            for j in range(4):
                ly = y + 2.9 + j * 0.6
                if ly < Y_END - 0.3:
                    k.line(s, x + 0.4, ly, x + cw - 0.4, ly, t.grid, 0.75,
                           dash=MSO_LINE_DASH_STYLE.DASH, name="Garis jawaban")
        return s

    # ------------------------------------------------------------ tambahan laporan kerja
    def kpi_bars(self, title, rows, kicker=None, notes=None):
        """KPI: realisasi vs target dengan bilah progres. rows = (nama, realisasi, target, %)."""
        s, y = self._content(title, kicker)
        t = self.t
        name_w, val_w = 3.6, 2.6
        bar_x = X0 + name_w + val_w
        bar_w = W - name_w - val_w - 1.1
        k.text(s, X0, y, name_w, 0.35, "Indikator", size=12, bold=True, color=t.muted,
               caps=True, spacing=1.5)
        k.text(s, X0 + name_w, y, val_w, 0.35, "Realisasi / Target", size=12, bold=True,
               color=t.muted, caps=True, spacing=1.5)
        k.text(s, bar_x, y, bar_w, 0.35, "Capaian", size=12, bold=True, color=t.muted,
               caps=True, spacing=1.5)
        rh = (Y_END - y - 0.5) / len(rows)
        for i, (name, real, target, pct) in enumerate(rows):
            yy = y + 0.5 + i * rh
            k.text(s, X0, yy, name_w, rh, name, size=16, bold=True, color=t.primary,
                   anchor="m")
            k.text(s, X0 + name_w, yy, val_w, rh,
                   [[dict(text=real, bold=True, color=t.primary),
                     dict(text=f" / {target}", color=t.muted)]], size=15, anchor="m")
            bh = 0.28
            by = yy + rh / 2 - bh / 2
            k.rrect(s, bar_x, by, bar_w, bh, t.surface if not t.dark else "lt2",
                    radius=bh / 2, name="Bilah latar")
            fill_w = max(bh, bar_w * min(pct, 100) / 100)
            k.rrect(s, bar_x, by, fill_w, bh, t.series[0] if pct >= 100 else t.series[1],
                    radius=bh / 2, name=f"Bilah {pct}%")
            k.text(s, bar_x + bar_w + 0.1, yy, 1.0, rh, f"{pct}%", size=16, bold=True,
                   color=t.primary, anchor="m", align="r")
            if i < len(rows) - 1:
                k.line(s, X0, yy + rh, X1, yy + rh, t.grid, 0.75, name="Garis")
        return s

    # ------------------------------------------------------------ tambahan proposal kegiatan
    def tiers(self, title, tiers, kicker=None, notes=None, featured=1):
        """Paket sponsor / harga: 3 kolom, kolom tengah disorot."""
        s, y = self._content(title, kicker)
        t = self.t
        n = len(tiers)
        gap = 0.35
        cw = (W - gap * (n - 1)) / n
        h = Y_END - y
        for i, (name, price, items) in enumerate(tiers):
            x = X0 + i * (cw + gap)
            hot = i == featured
            if hot:
                k.rrect(s, x, y, cw, h, t.primary if not t.dark else "accent1",
                        radius=t.card_radius, name=f"Paket {name} (unggulan)")
                ink, sub = ("lt1", "lt1") if not t.dark else ("dk1", "dk1")
            else:
                t.card(s, x, y, cw, h, name=f"Paket {name}")
                ink, sub = t.primary, t.muted
            k.text(s, x + 0.4, y + 0.4, cw - 0.8, 0.4, name, size=14, bold=True,
                   color=sub if not hot else ink, caps=True, spacing=2)
            k.text(s, x + 0.4, y + 0.85, cw - 0.8, 0.8, price, size=30, bold=True, color=ink,
                   font="+mj-lt")
            k.bullets(s, x + 0.4, y + 1.9, cw - 0.8, h - 2.1, items, size=14,
                      color=ink if hot else t.text,
                      bullet_color=("lt1" if not t.dark else "dk1") if hot else t.accent,
                      para_after=8)
        return s
