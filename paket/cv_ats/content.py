"""Contoh isi CV & surat lamaran. Tokoh fiktif, isi ditulis seperti CV
sungguhan supaya pembeli tahu cara menulis tiap bagian."""

KLASIK = dict(
    name="Dewi Anggraini, S.Ak.",
    title="Staf Akuntansi & Administrasi Keuangan",
    contact=["Bandung, Jawa Barat", "0812-3456-7890", "dewi.anggraini@email.com",
             "linkedin.com/in/dewianggraini"],
    summary="Lulusan S1 Akuntansi dengan 3 tahun pengalaman di bidang pembukuan, rekonsiliasi "
            "bank, dan pelaporan pajak. Terbiasa memakai Accurate, SAP B1, dan Excel tingkat "
            "lanjut. Teliti, tepat waktu, dan terbiasa bekerja dengan target tutup buku bulanan.",
    experience=[
        ("Staf Akuntansi", "PT Sinar Niaga Sejahtera", "Bandung", "Jan 2023 – Sekarang", [
            "Mengelola jurnal harian dan tutup buku bulanan untuk 3 cabang",
            "Mempercepat rekonsiliasi bank dari 5 hari menjadi 2 hari dengan template Excel",
            "Menyiapkan SPT Masa PPN dan PPh 21 tanpa koreksi selama 2 tahun berturut-turut",
            "Menjadi penghubung utama dengan auditor eksternal saat audit tahunan",
        ]),
        ("Admin Keuangan", "CV Karya Mandiri", "Cimahi", "Mar 2021 – Des 2022", [
            "Memproses 300+ faktur dan pembayaran pemasok setiap bulan",
            "Menyusun laporan arus kas mingguan untuk direktur",
            "Merapikan arsip dokumen keuangan 2018–2021 ke sistem digital",
        ]),
        ("Magang Auditor", "KAP Rahman & Rekan", "Bandung", "Jul – Sep 2020", [
            "Membantu pengujian substantif akun piutang dan persediaan untuk 4 klien",
        ]),
    ],
    education=[("S1 Akuntansi", "Universitas Padjadjaran", "2016 – 2020", "IPK 3,62 / 4,00")],
    skills=["Akuntansi keuangan & perpajakan", "Accurate, SAP Business One", "Microsoft Excel "
            "(Pivot, VLOOKUP, Power Query)", "Rekonsiliasi bank", "Brevet Pajak A & B"],
    languages=["Indonesia (penutur asli)", "Inggris (aktif, TOEFL ITP 540)"],
    organizations=[("Bendahara", "Himpunan Mahasiswa Akuntansi Unpad", "2018 – 2019")],
    certifications=[("Brevet Pajak A & B", "IAI Jawa Barat", "2021"),
                    ("Microsoft Office Specialist: Excel", "Certiport", "2022")],
)

MODERN = dict(
    name="Rizky Pratama",
    title="Digital Marketing Specialist",
    contact=["Jakarta Selatan", "0813-2222-4545", "rizky.pratama@email.com",
             "linkedin.com/in/rizkypratama", "rizkypratama.com"],
    summary="Digital marketer dengan 4 tahun pengalaman mengelola iklan berbayar dan media "
            "sosial untuk brand FMCG dan e-commerce. Fokus pada data: setiap kampanye diukur "
            "dari biaya per akuisisi dan ROAS, bukan sekadar jangkauan.",
    experience=[
        ("Digital Marketing Specialist", "Tokoloka.id", "Jakarta", "Feb 2023 – Sekarang", [
            "Mengelola anggaran iklan Meta & Google Rp350 juta/bulan dengan ROAS rata-rata 4,2x",
            "Menurunkan biaya per akuisisi 31% lewat uji A/B materi iklan dan landing page",
            "Memimpin 3 orang tim konten untuk TikTok dan Instagram",
        ]),
        ("Social Media Executive", "PT Segar Alami (FMCG)", "Jakarta", "Jun 2021 – Jan 2023", [
            "Menumbuhkan pengikut Instagram dari 40 ribu menjadi 185 ribu dalam 18 bulan",
            "Menjalankan 12 kampanye kolaborasi dengan 60+ kreator",
            "Menyusun laporan performa bulanan di Looker Studio untuk manajemen",
        ]),
        ("Marketing Intern", "Startup EduKita", "Depok", "Jan – Jun 2021", [
            "Menulis 40 artikel SEO; 6 di antaranya masuk halaman pertama Google",
            "Membantu riset kata kunci dan kalender konten bulanan",
        ]),
    ],
    education=[("S1 Ilmu Komunikasi", "Universitas Indonesia", "2017 – 2021", "IPK 3,51")],
    skills=["Meta Ads & Google Ads", "Google Analytics 4", "SEO & copywriting", "TikTok Ads",
            "Canva & CapCut", "Looker Studio"],
    languages=["Indonesia", "Inggris (profesional)"],
    certifications=[("Google Ads Search Certification", "Google", "2024"),
                    ("Meta Certified Digital Marketing Associate", "Meta", "2023")],
)

MINIMALIS = dict(
    name="Salsabila Rahma",
    title="UI/UX Designer",
    contact=["Yogyakarta", "0857-1111-2020", "salsabila.rahma@email.com",
             "behance.net/salsabilarahma"],
    summary="Desainer produk yang senang mengubah masalah rumit menjadi alur yang sederhana. "
            "Berpengalaman 3 tahun merancang aplikasi fintech dan edukasi, dari riset pengguna "
            "hingga prototipe siap dikembangkan.",
    experience=[
        ("UI/UX Designer", "PayRupa (fintech)", "Remote", "Agu 2023 – Sekarang", [
            "Mendesain ulang alur pendaftaran; tingkat penyelesaian naik dari 58% ke 81%",
            "Membangun design system 120+ komponen di Figma untuk 4 tim produk",
            "Bekerja harian dengan PM dan engineer dalam sprint 2 mingguan",
        ]),
        ("Junior Product Designer", "Belajarin", "Yogyakarta", "Jan 2022 – Jul 2023", [
            "Melakukan 30+ wawancara pengguna dan uji usability untuk fitur kelas daring",
            "Merancang aplikasi Android dengan rating 4,7 di Play Store",
        ]),
        ("Freelance UI Designer", "Berbagai klien UMKM", "Yogyakarta", "2020 – 2021", [
            "Mendesain 12 situs dan aplikasi untuk usaha kuliner, butik, dan sekolah",
        ]),
    ],
    projects=[("Redesain Aplikasi KRL", "studi kasus, 2.300+ apresiasi di Behance"),
              ("Kit Ikon Batik", "120 ikon gratis, diunduh 5.000+ kali")],
    education=[("S1 Desain Komunikasi Visual", "Institut Seni Indonesia Yogyakarta",
                "2017 – 2021", "Lulus dengan pujian")],
    skills=["Figma, FigJam", "User research", "Wireframe & prototyping", "Design system",
            "Usability testing", "HTML/CSS dasar"],
    languages=["Indonesia", "Inggris"],
    certifications=[("Google UX Design Certificate", "Coursera", "2022")],
)

ELEGAN = dict(
    name="Andreas Wijaya, M.M.",
    title="Project Manager | PMP",
    contact=["Surabaya", "0811-3030-7070", "andreas.wijaya@email.com",
             "linkedin.com/in/andreaswijaya"],
    summary="Project manager bersertifikat PMP dengan 9 tahun pengalaman memimpin proyek "
            "implementasi sistem dan konstruksi bernilai hingga Rp45 miliar. Kuat dalam "
            "pengendalian biaya, manajemen risiko, dan komunikasi dengan pemangku kepentingan.",
    experience=[
        ("Senior Project Manager", "PT Nusantara Infrastruktur", "Surabaya", "2021 – Sekarang", [
            "Memimpin 6 proyek sekaligus dengan total nilai Rp120 miliar, 100% selesai tepat waktu",
            "Menekan pembengkakan biaya dari 12% menjadi 3% lewat pelaporan earned value",
            "Membina 14 anggota tim lintas fungsi dan 5 subkontraktor",
        ]),
        ("Project Manager", "PT Solusi Data Prima", "Jakarta", "2017 – 2021", [
            "Mengimplementasikan ERP di 22 cabang klien ritel dalam 14 bulan",
            "Menyusun standar dokumen proyek yang kemudian dipakai seluruh divisi",
        ]),
        ("Project Coordinator", "PT Solusi Data Prima", "Jakarta", "2015 – 2017", [
            "Mengatur jadwal, notulen, dan laporan mingguan untuk 8 proyek TI",
        ]),
    ],
    education=[("Magister Manajemen", "Universitas Airlangga", "2019 – 2021", ""),
               ("S1 Teknik Industri", "Institut Teknologi Sepuluh Nopember", "2010 – 2014", "")],
    skills=["Manajemen proyek (PMBOK, Agile)", "Pengendalian biaya & jadwal",
            "Manajemen risiko", "MS Project, Jira", "Negosiasi kontrak", "Kepemimpinan tim"],
    languages=["Indonesia", "Inggris (fasih)", "Mandarin (dasar)"],
    certifications=[("Project Management Professional (PMP)", "PMI", "2019"),
                    ("Certified ScrumMaster", "Scrum Alliance", "2020")],
)

FRESH = dict(
    name="Muhammad Fajar Hidayat",
    title="Fresh Graduate Teknik Informatika",
    contact=["Semarang", "0896-5555-1234", "fajar.hidayat@email.com", "github.com/fajarhidayat"],
    summary="Lulusan baru Teknik Informatika yang suka membangun aplikasi web. Berpengalaman "
            "magang sebagai backend developer dan aktif di organisasi kampus. Cepat belajar, "
            "terbiasa bekerja dalam tim, dan siap ditempatkan di seluruh Indonesia.",
    education=[("S1 Teknik Informatika", "Universitas Diponegoro", "2020 – 2024",
                "IPK 3,71 / 4,00 · Skripsi: Sistem Rekomendasi Buku dengan Collaborative Filtering")],
    experience=[
        ("Backend Developer Intern", "PT Teknologi Kreatif", "Semarang", "Feb – Jul 2023", [
            "Membuat 15 endpoint REST API dengan Laravel untuk aplikasi kasir",
            "Menulis unit test sehingga cakupan kode naik dari 40% ke 72%",
        ]),
        ("Ketua Divisi Riset & Teknologi", "Himpunan Mahasiswa Informatika", "Semarang",
         "2022 – 2023", [
             "Mengadakan 6 pelatihan coding dengan total 400+ peserta",
         ]),
        ("Asisten Praktikum Basis Data", "Laboratorium Informatika", "Semarang", "2022", [
            "Membimbing 60 mahasiswa dalam praktikum SQL setiap minggu",
        ]),
    ],
    projects=[("Aplikasi Antrean Puskesmas", "Laravel, MySQL · dipakai 2 puskesmas"),
              ("Bot Pengingat Tugas Kuliah", "Python, Telegram API · 300+ pengguna")],
    skills=["PHP & Laravel", "Python", "JavaScript", "MySQL", "Git & GitHub", "REST API"],
    languages=["Indonesia", "Inggris (TOEFL ITP 550)"],
    certifications=[("Juara 2 Hackathon Jateng", "Diskominfo Jateng", "2023"),
                    ("Dicoding: Belajar Back-End Pemula", "Dicoding", "2022")],
)

# Isi surat lamaran (dipakai semua desain, nama & posisi disesuaikan)
LETTER = dict(
    date="{city}, 22 Oktober 2026",
    to=["Yth. Manajer HRD", "PT Nama Perusahaan", "Jl. Alamat Perusahaan No. 1", "Kota"],
    subject="Lamaran Pekerjaan sebagai {position}",
    body=[
        "Dengan hormat,",
        "Berdasarkan informasi lowongan yang saya temukan di {source}, saya bermaksud melamar "
        "posisi {position} di {company}. Saya yakin pengalaman dan keahlian saya sesuai dengan "
        "kebutuhan tim Bapak/Ibu.",
        "{highlight}",
        "Saya terbiasa bekerja dengan target, mudah beradaptasi, dan senang mempelajari hal "
        "baru. Bersama surat ini saya lampirkan CV, ijazah, transkrip nilai, dan dokumen "
        "pendukung lainnya.",
        "Besar harapan saya untuk dapat mengikuti tahap seleksi berikutnya dan menjelaskan "
        "lebih lanjut bagaimana saya dapat berkontribusi. Atas perhatian Bapak/Ibu, saya "
        "ucapkan terima kasih.",
    ],
    closing="Hormat saya,",
)

HIGHLIGHTS = {
    "klasik": "Selama tiga tahun terakhir saya menangani pembukuan dan pelaporan pajak untuk "
              "tiga cabang perusahaan, termasuk mempercepat rekonsiliasi bank dari lima hari "
              "menjadi dua hari.",
    "modern": "Dalam peran saya saat ini, saya mengelola anggaran iklan Rp350 juta per bulan "
              "dengan ROAS rata-rata 4,2x dan berhasil menurunkan biaya per akuisisi sebesar 31%.",
    "minimalis": "Di PayRupa, desain ulang alur pendaftaran yang saya pimpin menaikkan tingkat "
                 "penyelesaian pendaftaran dari 58% menjadi 81%.",
    "elegan": "Selama sembilan tahun saya memimpin proyek bernilai hingga Rp45 miliar dan "
              "menyelesaikan seluruh proyek terakhir tepat waktu dengan deviasi biaya di "
              "bawah 3%.",
    "fresh": "Selama magang sebagai backend developer, saya membangun 15 endpoint REST API dan "
             "menaikkan cakupan pengujian kode dari 40% menjadi 72%.",
}
