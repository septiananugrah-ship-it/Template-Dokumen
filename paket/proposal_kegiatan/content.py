"""Isi contoh Template PPT Proposal Kegiatan & LPJ (acara kampus fiktif)."""
from templategen.themes_elegan import ORGANISASI as THEMES  # noqa: F401

META = "Festival Literasi Digital 2026  ·  BEM Fakultas"
META_LPJ = "LPJ Festival Literasi Digital 2026  ·  BEM Fakultas"

COVER = dict(
    kampus="BEM Fakultas Nama Kampus",
    fakultas="",
    jenis="Proposal Kegiatan",
    judul="Festival Literasi Digital 2026",
    nama="Badan Eksekutif Mahasiswa Fakultas",
    nim="Seminar, lomba, dan pameran · 14–15 Maret 2026",
    pembimbing="Narahubung: Nama Ketua Panitia · 0812-3456-7890",
    tahun="Universitas Nama Kampus",
)

CLOSING = dict(
    judul="Terima Kasih",
    sub="Mari wujudkan kegiatan ini bersama.",
    kontak=[("phone", "0812-3456-7890"), ("mail", "fld@kampus.ac.id"),
            ("at-sign", "@festivalliterasi")],
)


def div(num, title, sub):
    return dict(type="divider", num=num, title=title, subtitle=sub)


PROPOSAL = [
    dict(type="cover", **COVER),
    dict(type="text_stats", kicker="Pendahuluan", title="Latar Belakang",
         paragraphs=["Mahasiswa menghabiskan banyak waktu di dunia digital, namun belum semua "
                     "mampu memilah informasi yang benar.",
                     "Festival Literasi Digital hadir sebagai ruang belajar yang menyenangkan "
                     "tentang keamanan data, cek fakta, dan kreativitas konten."],
         stats=[("1.500", "target peserta dari 20 kampus"),
                ("2 hari", "seminar, lomba, dan pameran"),
                ("12", "pembicara dan juri praktisi")]),
    dict(type="numbered", kicker="Tujuan", title="Tujuan Kegiatan",
         items=[("Edukasi", "Meningkatkan kemampuan mahasiswa memverifikasi informasi"),
                ("Kreativitas", "Mendorong konten digital yang positif dan bermanfaat"),
                ("Jejaring", "Mempertemukan mahasiswa dengan komunitas dan industri")]),
    dict(type="icon_grid", kicker="Informasi", title="Waktu dan Tempat",
         items=[("calendar", "Tanggal", "Sabtu–Minggu, 14–15 Maret 2026"),
                ("clock", "Waktu", "08.00–17.00 WIB"),
                ("map-pin", "Tempat", "Auditorium Utama Universitas Nama Kampus"),
                ("users", "Peserta", "Mahasiswa, pelajar SMA, dan masyarakat umum")]),
    dict(type="table_slide", kicker="Rundown", title="Rangkaian Acara Hari Pertama",
         rows=[["Waktu", "Kegiatan", "Tempat", "PJ"],
               ["08.00–09.00", "Registrasi peserta", "Lobi", "Sekretariat"],
               ["09.00–09.30", "Pembukaan & sambutan", "Auditorium", "Acara"],
               ["09.30–12.00", "Seminar: Cek Fakta di Era AI", "Auditorium", "Acara"],
               ["13.00–15.00", "Lomba video pendek (babak final)", "Aula B", "Lomba"],
               ["15.00–17.00", "Pameran komunitas & penutupan", "Plaza", "Acara"]],
         col_widths=[2.2, 5.0, 2.4, 2.3], align=["c", "l", "l", "l"]),
    dict(type="org_chart", kicker="Kepanitiaan", title="Susunan Panitia",
         top=("Nama Ketua", "Ketua Panitia"),
         middle=[("Nama", "Sekretaris"), ("Nama", "Bendahara"), ("Nama", "Koord. Acara"),
                 ("Nama", "Koord. Humas")]),
    dict(type="table_slide", kicker="Anggaran", title="Rencana Anggaran",
         rows=[["Pos", "Rincian", "Jumlah (Rp)"],
               ["Pembicara & juri", "12 orang", "18.000.000"],
               ["Sewa tempat & alat", "Auditorium, sound, LED", "15.500.000"],
               ["Publikasi", "Iklan digital, banner, merchandise", "8.000.000"],
               ["Konsumsi", "Panitia & tamu, 2 hari", "9.500.000"],
               ["Hadiah lomba", "3 kategori", "6.000.000"],
               ["Total", "", "57.000.000"]],
         col_widths=[3.5, 5.4, 3.0], align=["l", "l", "r"]),
    dict(type="funds", kicker="Pendanaan", title="Sumber Dana", amount="Rp57 juta",
         caption="Kebutuhan dana kegiatan dipenuhi dari empat sumber berikut.",
         uses=[("Sponsor", 50, "Perusahaan & media partner"),
               ("Fakultas", 25, "Dana kemahasiswaan"),
               ("Tiket", 15, "Seminar berbayar"),
               ("Kas BEM", 10, "Dana organisasi")]),
    dict(type="tiers", kicker="Kerja Sama", title="Paket Sponsor",
         featured=2,
         tiers=[("Silver", "Rp3 jt", ["Logo di banner & media sosial",
                                      "Disebut oleh MC", "1 stan pameran (bersama)"]),
                ("Gold", "Rp7 jt", ["Logo di banner & media sosial", "Video iklan 30 detik",
                                    "1 stan pameran"]),
                ("Platinum", "Rp15 jt", ["Logo utama di semua publikasi",
                                         "Sesi presentasi 15 menit",
                                         "Stan pameran khusus", "Data peserta (opt-in)"])]),
    dict(type="closing", **CLOSING),
]

LPJ = [
    dict(type="cover", **{**COVER, "jenis": "Laporan Pertanggungjawaban",
                          "nim": "Dilaksanakan 14–15 Maret 2026"}),
    dict(type="stats4", kicker="Ringkasan", title="Hasil Kegiatan",
         stats=[("1.620", "Peserta", "108% dari target 1.500"),
                ("9", "Sponsor", "3 platinum, 2 gold, 4 silver"),
                ("Rp61 jt", "Dana terkumpul", "107% dari kebutuhan"),
                ("4,7/5", "Kepuasan", "Survei 520 peserta")]),
    dict(type="kpi_bars", kicker="Capaian", title="Target dan Realisasi",
         rows=[("Peserta", "1.620", "1.500", 108), ("Karya lomba", "184", "200", 92),
               ("Kampus asal", "23", "20", 115), ("Liputan media", "7", "10", 70)]),
    dict(type="photos", kicker="Dokumentasi", title="Dokumentasi Kegiatan",
         captions=["Seminar utama", "Final lomba video", "Pameran komunitas"]),
    dict(type="table_slide", kicker="Keuangan", title="Realisasi Anggaran",
         rows=[["Pos", "Anggaran (Rp)", "Realisasi (Rp)", "Selisih (Rp)"],
               ["Pembicara & juri", "18.000.000", "17.500.000", "500.000"],
               ["Sewa tempat & alat", "15.500.000", "15.500.000", "0"],
               ["Publikasi", "8.000.000", "8.750.000", "-750.000"],
               ["Konsumsi", "9.500.000", "9.100.000", "400.000"],
               ["Hadiah lomba", "6.000.000", "6.000.000", "0"],
               ["Total", "57.000.000", "56.850.000", "150.000"]],
         col_widths=[3.5, 2.8, 2.8, 2.8], align=["l", "r", "r", "r"],
         note="Sisa dana Rp4.150.000 (termasuk kelebihan sponsor) dikembalikan ke kas BEM."),
    dict(type="compare", kicker="Evaluasi", title="Evaluasi Kegiatan",
         left=("thumbs-up", "Berjalan Baik",
               ["Peserta melebihi target", "Pembicara tepat waktu dan interaktif",
                "Sponsor puas dengan eksposur"]),
         right=("triangle-alert", "Perlu Perbaikan",
                ["Antrean registrasi panjang di pagi hari", "Sinyal internet aula lemah",
                 "Publikasi media terlambat dimulai"])),
    dict(type="numbered", kicker="Rekomendasi", title="Rekomendasi Kegiatan Berikutnya",
         items=[("Registrasi", "Gunakan check-in kode QR dan buka meja tambahan"),
                ("Teknis", "Survei jaringan internet H-14 dan sewa router cadangan"),
                ("Publikasi", "Mulai kerja sama media paling lambat H-45")]),
    dict(type="logos", kicker="Terima Kasih", title="Sponsor dan Mitra",
         names=["Sponsor 1", "Sponsor 2", "Sponsor 3", "Sponsor 4", "Mitra 1", "Mitra 2",
                "Mitra 3", "Mitra 4"]),
    dict(type="closing", **{**CLOSING, "sub": "Terima kasih atas dukungan semua pihak."}),
]

DECKS = [("Proposal-Kegiatan", "Proposal", PROPOSAL, META),
         ("LPJ-Kegiatan", "LPJ", LPJ, META_LPJ)]
