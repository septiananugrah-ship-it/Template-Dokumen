"""Isi contoh Template PPT Webinar & Seminar (acara fiktif)."""
from templategen.themes_elegan import WEBINAR as THEMES  # noqa: F401

META = "Webinar Karier Digital 2026  ·  Sabtu, 21 November 2026"

COVER = dict(
    brand="Komunitas Nama Penyelenggara",
    jenis="Webinar Nasional · Gratis",
    judul="Memulai Karier di Dunia Digital",
    tagline="Belajar langsung dari praktisi data, desain produk, dan pemasaran digital.",
    meta="Sabtu, 21 November 2026  ·  09.00–12.00 WIB  ·  Zoom Meeting",
    photo="Foto pembicara / poster",
)

CLOSING = dict(
    judul="Sampai Jumpa!",
    sub="Isi presensi dan formulir umpan balik untuk mendapatkan e-sertifikat.",
    kontak=[("link", "bit.ly/presensi-webinar"), ("at-sign", "@komunitasdigital"),
            ("mail", "halo@komunitas.id")],
)


def div(num, title, sub):
    return dict(type="divider", num=num, title=title, subtitle=sub)


SLIDES = [
    dict(type="cover", **COVER),
    dict(type="image_text", kicker="Tentang Acara", title="Selamat Datang",
         heading="Tiga jam belajar karier digital bersama praktisi industri",
         lead="Webinar ini dirancang untuk mahasiswa tingkat akhir, fresh graduate, dan siapa "
              "pun yang ingin beralih karier.",
         points=[("users", "1.200 peserta", "Terdaftar dari 34 provinsi"),
                 ("mic", "3 pembicara", "Data, desain produk, pemasaran"),
                 ("award", "E-sertifikat", "Untuk peserta yang hadir sampai akhir")],
         photo="Poster acara"),
    dict(type="numbered", kicker="Tata Tertib", title="Selama Webinar Berlangsung",
         items=[("Nama tampilan", "Gunakan format Nama_Asal Instansi agar mudah dipresensi"),
                ("Mikrofon", "Matikan mikrofon kecuali saat dipersilakan bertanya"),
                ("Pertanyaan", "Tulis pertanyaan di kolom Q&A, bukan di chat umum")]),
    dict(type="table_slide", kicker="Rundown", title="Susunan Acara",
         rows=[["Waktu (WIB)", "Sesi", "Pengisi"],
               ["09.00–09.10", "Pembukaan", "MC"],
               ["09.10–09.50", "Karier sebagai Data Analyst", "Pembicara 1"],
               ["09.50–10.30", "Masuk ke Dunia UI/UX", "Pembicara 2"],
               ["10.30–11.10", "Digital Marketing untuk Pemula", "Pembicara 3"],
               ["11.10–11.50", "Tanya jawab", "Moderator"],
               ["11.50–12.00", "Penutupan & foto bersama", "MC"]],
         col_widths=[2.6, 6.0, 3.3], align=["c", "l", "l"]),
    dict(type="team_photo", kicker="Pembicara", title="Pembicara & Moderator",
         members=[("Nama Pembicara", "Data Analyst", "Senior Analyst di perusahaan e-commerce"),
                  ("Nama Pembicara", "Product Designer", "8 tahun merancang aplikasi fintech"),
                  ("Nama Pembicara", "Digital Marketer", "Membangun 20+ kampanye nasional"),
                  ("Nama Moderator", "Moderator", "Ketua Komunitas Nama Penyelenggara")]),
    div("01", "Sesi Pertama", "Karier sebagai Data Analyst"),
    dict(type="image_text", kicker="Sesi 1", title="Profil Pembicara",
         heading="Nama Pembicara",
         lead="Senior Data Analyst dengan pengalaman 6 tahun di bidang e-commerce dan logistik.",
         points=[("graduation-cap", "Pendidikan", "S1 Statistika, Universitas Nama Kampus"),
                 ("briefcase", "Pengalaman", "Data Analyst di 3 perusahaan teknologi"),
                 ("at-sign", "Kontak", "linkedin.com/in/namapembicara")],
         photo="Foto pembicara"),
    dict(type="icon_grid", kicker="Sesi 1", title="Keahlian yang Dibutuhkan",
         items=[("database", "SQL", "Mengambil dan mengolah data dari basis data"),
                ("table", "Spreadsheet", "Excel atau Google Sheets tingkat lanjut"),
                ("chart-column", "Visualisasi", "Dasbor dengan Looker Studio atau Power BI"),
                ("message-square", "Komunikasi", "Menjelaskan temuan ke tim non-teknis")]),
    dict(type="stats4", kicker="Fakta", title="Peluang Karier Digital",
         stats=[("9 jt", "Talenta digital", "Kebutuhan Indonesia hingga 2030 (contoh data)"),
                ("38%", "Lowongan", "Meminta kemampuan analisis data"),
                ("2×", "Pertumbuhan", "Lowongan UI/UX dalam 3 tahun"),
                ("70%", "Remote", "Posisi digital yang bisa dikerjakan jarak jauh")]),
    div("02", "Tanya Jawab", "Saatnya bertanya kepada pembicara"),
    dict(type="big_question", kicker="Sesi Tanya Jawab", title="Ada Pertanyaan?",
         question="Tulis pertanyaanmu di kolom Q&A beserta nama dan asal instansi.",
         hint="Tiga penanya terbaik mendapat hadiah dari sponsor."),
    dict(type="logos", kicker="Didukung Oleh", title="Sponsor & Media Partner",
         names=["Sponsor 1", "Sponsor 2", "Sponsor 3", "Sponsor 4", "Media 1", "Media 2",
                "Media 3", "Media 4"]),
    dict(type="icon_grid", kicker="Setelah Acara", title="Presensi dan E-Sertifikat",
         items=[("clipboard-check", "Isi presensi", "Tautan dibagikan di chat pukul 11.50"),
                ("star", "Umpan balik", "Formulir singkat 2 menit"),
                ("award", "E-sertifikat", "Dikirim ke email maksimal 3 hari kerja"),
                ("file-text", "Materi", "Slide pembicara dibagikan lewat email")]),
    dict(type="closing", **CLOSING),
]

DECKS = [("Webinar", "Webinar", SLIDES, META)]
