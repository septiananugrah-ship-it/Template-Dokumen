"""Isi contoh Template PPT Company Profile (perusahaan fiktif)."""
from templategen.themes_elegan import PROFIL as THEMES  # noqa: F401

META = "PT Nusa Karya Mandiri  ·  Company Profile 2026"

COVER = dict(
    brand="PT Nusa Karya Mandiri",
    jenis="Company Profile 2026",
    judul="Membangun Ruang yang Bertahan Lama",
    tagline="Kontraktor dan konsultan desain interior untuk kantor, ritel, dan hunian sejak 2012.",
    meta="www.nusakarya.co.id",
    photo="Foto kantor / proyek",
)

CLOSING = dict(
    judul="Mari Bekerja Sama",
    sub="Hubungi kami untuk konsultasi dan survei lokasi tanpa biaya.",
    kontak=[("phone", "(021) 555-0123"), ("mail", "halo@nusakarya.co.id"),
            ("globe", "nusakarya.co.id")],
)


def div(num, title, sub):
    return dict(type="divider", num=num, title=title, subtitle=sub)


SLIDES = [
    dict(type="cover", **COVER),
    dict(type="agenda", kicker="Daftar Isi", title="Isi Profil Perusahaan",
         items=[("Tentang Kami", "Sejarah, visi, misi, dan nilai"),
                ("Layanan", "Apa yang kami kerjakan"),
                ("Pencapaian", "Angka dan klien kami"),
                ("Portofolio", "Proyek pilihan"),
                ("Tim", "Struktur dan manajemen"),
                ("Kontak", "Lokasi dan cara menghubungi")]),
    div("01", "Tentang Kami", "Siapa kami dan apa yang kami percayai"),
    dict(type="image_text", kicker="Tentang Kami", title="Profil Singkat",
         heading="Lebih dari satu dekade mewujudkan ruang kerja dan hunian",
         lead="Berawal dari studio desain kecil di Jakarta Selatan, kini kami melayani klien "
              "di 12 kota dengan 85 tenaga ahli.",
         points=[("calendar", "Berdiri 2012", "Badan hukum PT sejak 2015"),
                 ("map-pin", "12 kota", "Jabodetabek, Bandung, Surabaya, Medan, dan lainnya"),
                 ("users", "85 karyawan", "Arsitek, desainer, dan tenaga lapangan")],
         photo="Foto kantor"),
    dict(type="two_col", kicker="Tentang Kami", title="Visi dan Misi",
         cols=[("eye", "Visi", ["Menjadi mitra desain dan pembangunan interior paling "
                                "tepercaya di Indonesia pada 2030"]),
               ("target", "Misi", ["Mengerjakan proyek tepat waktu dan sesuai anggaran",
                                   "Memakai material lokal berkualitas dan ramah lingkungan",
                                   "Mengembangkan tenaga ahli lewat pelatihan rutin"])]),
    dict(type="icon_grid", kicker="Nilai Perusahaan", title="Nilai yang Kami Pegang",
         items=[("shield-check", "Integritas", "Transparan dalam anggaran dan progres proyek"),
                ("ruler", "Presisi", "Detail dikerjakan sesuai gambar kerja"),
                ("leaf", "Berkelanjutan", "Memilih material yang aman dan tahan lama"),
                ("handshake", "Kemitraan", "Klien dilibatkan di setiap tahap keputusan")]),
    dict(type="timeline", kicker="Perjalanan", title="Sejarah Singkat",
         items=[("2012", "Studio berdiri", "Tiga pendiri, satu ruang kerja"),
                ("2015", "Menjadi PT", "Proyek kantor pertama 2.000 m²"),
                ("2018", "Cabang Surabaya", "Ekspansi ke Jawa Timur"),
                ("2022", "ISO 9001", "Sistem mutu tersertifikasi"),
                ("2026", "300+ proyek", "Hadir di 12 kota")]),
    div("02", "Layanan & Pencapaian", "Apa yang kami kerjakan dan hasilnya"),
    dict(type="cards3", kicker="Layanan", title="Layanan Kami",
         items=[("pen-tool", "Desain", "Desain Interior", "Konsep, gambar kerja, dan visual 3D "
                                                        "sebelum pembangunan dimulai"),
                ("hammer", "Bangun", "Fit-out & Renovasi", "Pengerjaan sipil, MEP, dan furnitur "
                                                          "dengan tim sendiri"),
                ("clipboard-check", "Kelola", "Manajemen Proyek", "Pengawasan jadwal, mutu, "
                                                                  "dan biaya hingga serah terima")]),
    dict(type="stats4", kicker="Pencapaian", title="Dalam Angka",
         stats=[("300+", "Proyek", "Selesai sejak 2012"),
                ("98%", "Tepat waktu", "Proyek diserahkan sesuai jadwal"),
                ("120rb", "Meter persegi", "Total area yang dikerjakan"),
                ("4,9/5", "Kepuasan", "Rata-rata survei klien 2025")]),
    dict(type="logos", kicker="Klien", title="Dipercaya Oleh",
         lead="Sebagian klien yang telah bekerja sama dengan kami.",
         names=["Klien 1", "Klien 2", "Klien 3", "Klien 4", "Klien 5", "Klien 6", "Klien 7",
                "Klien 8"]),
    dict(type="photos", kicker="Portofolio", title="Proyek Pilihan",
         captions=["Kantor Fintech, Jakarta · 1.800 m²", "Butik Ritel, Bandung · 240 m²",
                   "Hunian Tapak, Surabaya · 320 m²"]),
    dict(type="quotes", kicker="Testimoni", title="Kata Klien",
         items=[("Tim Nusa Karya sangat rapi dalam laporan progres. Kantor kami selesai dua "
                 "minggu lebih cepat.", "Manajer GA, perusahaan fintech"),
                ("Desainnya sesuai karakter brand kami dan anggarannya transparan sejak awal.",
                 "Pemilik butik, Bandung"),
                ("Komunikasinya cepat, setiap perubahan dicatat dan dikonfirmasi tertulis.",
                 "Pemilik rumah, Surabaya")]),
    div("03", "Tim & Kontak", "Orang-orang di balik setiap proyek"),
    dict(type="org_chart", kicker="Organisasi", title="Struktur Organisasi",
         top=("Nama Direktur", "Direktur Utama"),
         middle=[("Nama Manajer", "Desain"), ("Nama Manajer", "Proyek"),
                 ("Nama Manajer", "Keuangan"), ("Nama Manajer", "Pemasaran")]),
    dict(type="team_photo", kicker="Manajemen", title="Tim Manajemen",
         members=[("Nama Lengkap", "Direktur Utama", "Arsitek, 18 tahun pengalaman"),
                  ("Nama Lengkap", "Kepala Desain", "Lulusan desain interior ITB"),
                  ("Nama Lengkap", "Kepala Proyek", "Mengelola 120+ proyek fit-out"),
                  ("Nama Lengkap", "Kepala Keuangan", "Akuntan bersertifikat CA")]),
    dict(type="table_slide", kicker="Legalitas", title="Legalitas dan Sertifikasi",
         rows=[["Dokumen", "Nomor", "Keterangan"],
               ["Akta Pendirian", "No. 12 / 2015", "Notaris Nama Notaris, S.H."],
               ["NIB", "1234567890123", "Perizinan berusaha OSS"],
               ["NPWP Perusahaan", "01.234.567.8-901.000", "KPP Jakarta Selatan"],
               ["SBU Konstruksi", "BG009 / Kecil", "LPJK, berlaku hingga 2028"],
               ["ISO 9001:2015", "QMS-2022-0456", "Sistem manajemen mutu"]],
         col_widths=[3.2, 3.4, 5.3]),
    dict(type="contact_map", kicker="Kontak", title="Lokasi Kantor",
         address="Jl. Contoh Raya No. 45, Kebayoran Baru, Jakarta Selatan 12120",
         items=[("phone", "(021) 555-0123"), ("message-circle", "WhatsApp 0812-3456-7890"),
                ("mail", "halo@nusakarya.co.id"), ("clock", "Senin–Jumat, 08.00–17.00")]),
    dict(type="closing", **CLOSING),
]

DECKS = [("Company-Profile", "Company Profile", SLIDES, META)]
