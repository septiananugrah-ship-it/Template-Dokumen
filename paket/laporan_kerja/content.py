"""Isi contoh Template PPT Laporan Kerja Bulanan (divisi pemasaran fiktif)."""
from templategen.themes_elegan import LAPORAN as THEMES  # noqa: F401

META = "Laporan Bulanan Divisi Pemasaran  ·  Oktober 2026"

COVER = dict(
    brand="PT Nama Perusahaan",
    jenis="Laporan Kinerja Bulanan",
    judul="Laporan Divisi Pemasaran Oktober 2026",
    tagline="Disampaikan dalam rapat evaluasi bulanan manajemen.",
    meta="Disusun oleh: Nama Lengkap, Manajer Pemasaran  ·  3 November 2026",
    photo="Foto tim / kegiatan",
)

CLOSING = dict(
    judul="Terima Kasih",
    sub="Terbuka untuk pertanyaan dan masukan.",
    kontak=[("mail", "nama@perusahaan.co.id"), ("phone", "Ext. 214"),
            ("calendar", "Rapat berikutnya: 1 Des")],
)


def div(num, title, sub):
    return dict(type="divider", num=num, title=title, subtitle=sub)


SLIDES = [
    dict(type="cover", **COVER),
    dict(type="stats4", kicker="Ringkasan Eksekutif", title="Sorotan Bulan Ini",
         stats=[("Rp4,8 M", "Penjualan", "104% dari target bulanan"),
                ("1.240", "Pelanggan baru", "Naik 18% dari September"),
                ("3,6×", "ROAS iklan", "Target minimal 3,0×"),
                ("92%", "Kepuasan", "Survei 410 pelanggan")]),
    dict(type="agenda", kicker="Agenda", title="Isi Laporan",
         items=[("Kinerja", "KPI dan pencapaian"),
                ("Penjualan", "Grafik dan tren"),
                ("Anggaran", "Realisasi biaya"),
                ("Proyek", "Status pekerjaan"),
                ("Evaluasi", "Kendala dan solusi"),
                ("Rencana", "Target bulan depan")]),
    div("01", "Kinerja", "Capaian indikator utama bulan Oktober"),
    dict(type="kpi_bars", kicker="KPI", title="Realisasi terhadap Target",
         rows=[("Penjualan", "Rp4,8 M", "Rp4,6 M", 104),
               ("Pelanggan baru", "1.240", "1.200", 103),
               ("Leads dari iklan", "3.150", "3.500", 90),
               ("Konversi website", "2,4%", "3,0%", 80),
               ("Konten terbit", "46", "50", 92)]),
    dict(type="chart_bar", kicker="Penjualan", title="Penjualan per Bulan",
         chart_title="Penjualan (Rp miliar), Juli–Oktober",
         categories=["Jul", "Agu", "Sep", "Okt"],
         series=[("Target", (4.0, 4.2, 4.4, 4.6)), ("Realisasi", (3.8, 4.3, 4.1, 4.8))],
         insights=[("+17%", "kenaikan penjualan Oktober dibanding September"),
                   ("3 dari 4", "bulan terakhir mencapai target")]),
    dict(type="chart_mix", kicker="Penjualan", title="Kanal dan Tren Mingguan",
         pie=dict(title="Penjualan per kanal", categories=["Marketplace", "Website", "Toko",
                                                           "Reseller"],
                  values=(42, 26, 20, 12)),
         line=dict(title="Pesanan per minggu", min=200,
                   categories=["M1", "M2", "M3", "M4"],
                   series=[("Pesanan", (280, 310, 365, 402))])),
    dict(type="numbered", kicker="Pencapaian", title="Pencapaian Utama",
         items=[("Kampanye 10.10", "Menghasilkan Rp1,2 M dalam 3 hari, 26% dari penjualan "
                                   "bulanan"),
                ("Website baru", "Waktu muat turun dari 4,1 detik menjadi 1,8 detik"),
                ("Kemitraan", "Menandatangani kerja sama dengan 12 reseller baru")]),
    div("02", "Anggaran & Proyek", "Penggunaan biaya dan status pekerjaan"),
    dict(type="table_slide", kicker="Anggaran", title="Anggaran vs Realisasi",
         rows=[["Pos biaya (Rp juta)", "Anggaran", "Realisasi", "Selisih", "Serapan"],
               ["Iklan digital", "450", "438", "12", "97%"],
               ["Konten & kreatif", "120", "131", "-11", "109%"],
               ["Event & promosi", "200", "176", "24", "88%"],
               ["Alat & langganan", "35", "35", "0", "100%"],
               ["Total", "805", "780", "25", "97%"]],
         col_widths=[4.0, 2.0, 2.0, 2.0, 1.9], align=["l", "c", "c", "c", "c"],
         note="Kelebihan biaya konten karena tambahan produksi video kampanye 10.10."),
    dict(type="gantt", kicker="Proyek", title="Status Proyek Berjalan",
         months=["Okt M1", "M2", "M3", "M4", "Nov M1", "M2"],
         rows=[("Kampanye 10.10", 0, 1), ("Peluncuran website", 0, 2),
               ("Program reseller", 1, 4), ("Riset produk baru", 2, 5),
               ("Persiapan Harbolnas", 3, 5)]),
    div("03", "Evaluasi & Rencana", "Pelajaran bulan ini dan langkah berikutnya"),
    dict(type="compare", kicker="Evaluasi", title="Kendala dan Solusi",
         left=("triangle-alert", "Kendala",
               ["Konversi website di bawah target (2,4%)",
                "Biaya konten melebihi anggaran 9%",
                "Stok produk terlaris habis 4 hari"]),
         right=("wrench", "Solusi",
                ["Uji A/B halaman produk dan proses checkout",
                 "Jadwal produksi konten dikunci di awal bulan",
                 "Koordinasi mingguan stok dengan gudang"])),
    dict(type="steps", kicker="Rencana", title="Rencana Bulan November",
         items=[("target", "Target", "Penjualan Rp5,2 M"),
                ("shopping-bag", "Harbolnas 11.11", "Kampanye 5 hari"),
                ("mouse-pointer-click", "Konversi 3%", "Perbaikan checkout"),
                ("users", "Reseller", "Tambah 15 mitra"),
                ("chart-line", "Laporan", "Dasbor mingguan")]),
    dict(type="icon_grid", kicker="Dukungan", title="Dukungan yang Dibutuhkan",
         items=[("wallet", "Tambahan anggaran", "Rp60 juta untuk iklan Harbolnas"),
                ("package", "Stok aman", "Persediaan 2× rata-rata untuk 3 produk terlaris"),
                ("code", "Tim IT", "Dua minggu pengembangan untuk perbaikan checkout"),
                ("user-plus", "Tenaga tambahan", "Satu admin media sosial (kontrak)")]),
    dict(type="closing", **CLOSING),
]

DECKS = [("Laporan-Kerja", "Laporan Kerja", SLIDES, META)]
