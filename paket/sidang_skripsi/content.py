"""Isi contoh paket Template PPT Sidang Skripsi & Seminar Proposal.

Teks berupa contoh penelitian fiktif yang wajar, supaya pembeli langsung
melihat cara mengisi tiap slide. Semua bisa diganti di PowerPoint/Canva/
Google Slides.
"""

META = "Sidang Skripsi  ·  Nama Mahasiswa  ·  Program Studi"
META_PROPOSAL = "Seminar Proposal  ·  Nama Mahasiswa  ·  Program Studi"

JUDUL = ("Pengaruh Media Pembelajaran Interaktif terhadap Motivasi "
         "dan Hasil Belajar Siswa SMA")

COVER = dict(
    kampus="Universitas Nama Kampus",
    fakultas="Fakultas Keguruan dan Ilmu Pendidikan",
    jenis="Sidang Skripsi",
    judul=JUDUL,
    nama="Nama Lengkap Mahasiswa",
    nim="NIM 2101234567  ·  Program Studi Pendidikan",
    pembimbing="Pembimbing: Dr. Nama Dosen, M.Pd.",
    pembimbing_list="1. Dr. Nama Dosen Pertama, M.Pd.\n2. Nama Dosen Kedua, S.Pd., M.Pd.",
    tahun="Tahun Akademik 2025/2026",
)

CLOSING = dict(
    judul="Terima Kasih",
    sub="Mohon kritik dan saran dari Bapak/Ibu dewan penguji",
    kontak=[("mail", "nama@kampus.ac.id"), ("phone", "0812-3456-7890"),
            ("at-sign", "@namamahasiswa")],
)

S_LATAR = dict(
    type="text_stats", kicker="Pendahuluan", title="Latar Belakang",
    paragraphs=[
        "Pembelajaran di kelas masih didominasi metode ceramah sehingga siswa cenderung pasif "
        "dan cepat kehilangan fokus.",
        "Di sisi lain, hampir semua siswa sudah terbiasa memakai gawai. Media pembelajaran "
        "interaktif berpotensi menjembatani kebiasaan ini dengan tujuan belajar.",
        "Penelitian ini menguji apakah media interaktif benar-benar meningkatkan motivasi dan "
        "hasil belajar siswa.",
    ],
    stats=[("68%", "siswa merasa bosan saat pembelajaran ceramah (survei awal)"),
           ("92%", "siswa memiliki ponsel pintar pribadi"),
           ("71,4", "rata-rata nilai ulangan, di bawah KKM 75")],
    notes="Jelaskan fenomena di lapangan, lalu data pendukungnya. Sebutkan sumber data.",
)

S_RUMUSAN = dict(
    type="numbered", kicker="Pendahuluan", title="Rumusan Masalah",
    items=[("Motivasi belajar", "Apakah media pembelajaran interaktif berpengaruh signifikan "
                                "terhadap motivasi belajar siswa?"),
           ("Hasil belajar", "Apakah media pembelajaran interaktif berpengaruh signifikan "
                             "terhadap hasil belajar siswa?"),
           ("Pengaruh simultan", "Seberapa besar pengaruh media interaktif terhadap motivasi "
                                 "dan hasil belajar secara bersama-sama?")],
)

S_TUJUAN = dict(
    type="two_col", kicker="Pendahuluan", title="Tujuan dan Manfaat Penelitian",
    cols=[("target", "Tujuan Penelitian",
           ["Menganalisis pengaruh media interaktif terhadap motivasi belajar",
            "Menganalisis pengaruh media interaktif terhadap hasil belajar",
            "Mengukur besar pengaruh keduanya secara simultan"]),
          ("lightbulb", "Manfaat Penelitian",
           ["Teoretis: menambah kajian tentang teknologi pendidikan",
            "Bagi guru: acuan memilih media pembelajaran",
            "Bagi sekolah: dasar kebijakan pengadaan sarana digital"])],
)

S_BATASAN = dict(
    type="icon_grid", kicker="Pendahuluan", title="Batasan Masalah",
    items=[("users", "Subjek", "Siswa kelas XI SMA Negeri Contoh, semester genap"),
           ("book-open", "Materi", "Mata pelajaran Biologi bab Sistem Pernapasan"),
           ("presentation", "Media", "Kuis interaktif dan video animasi berbasis web"),
           ("calendar", "Waktu", "Penelitian berlangsung selama 6 minggu (12 pertemuan)")],
)

S_KAJIAN = dict(
    type="table_slide", kicker="Tinjauan Pustaka", title="Penelitian Terdahulu",
    rows=[["Peneliti (Tahun)", "Judul / Fokus", "Metode", "Hasil Utama"],
          ["Sari (2021)", "Media video terhadap minat belajar", "Kuasi eksperimen",
           "Minat naik 18%"],
          ["Pratama (2022)", "Gamifikasi kuis daring", "Eksperimen", "Hasil belajar naik signifikan"],
          ["Lestari (2023)", "Multimedia interaktif IPA", "R&D", "Layak dan efektif"],
          ["Nugroho (2024)", "Motivasi belajar era digital", "Survei", "Motivasi dipengaruhi media"],
          ["Penelitian ini", "Media interaktif → motivasi & hasil", "Kuasi eksperimen", "—"]],
    col_widths=[2.2, 4.2, 2.3, 3.2],
    note="Ganti dengan penelitian relevan dari jurnal 5 tahun terakhir.",
)

S_KERANGKA = dict(
    type="flow", kicker="Tinjauan Pustaka", title="Kerangka Pemikiran",
    inputs=[("Media Interaktif (X)", "Kuis, video animasi, simulasi"),
            ("Motivasi Belajar (Z)", "Variabel antara / mediasi")],
    output=("Hasil Belajar (Y)", "Nilai post-test siswa"),
    labels=["H1", "H2"],
    caption="Media interaktif diduga meningkatkan motivasi, dan motivasi yang tinggi "
            "berdampak pada hasil belajar.",
)

S_HIPOTESIS = dict(
    type="hypotheses", kicker="Tinjauan Pustaka", title="Hipotesis Penelitian",
    items=[("H1", "Terdapat pengaruh positif dan signifikan media pembelajaran interaktif "
                  "terhadap motivasi belajar siswa."),
           ("H2", "Terdapat pengaruh positif dan signifikan media pembelajaran interaktif "
                  "terhadap hasil belajar siswa."),
           ("H3", "Motivasi belajar memediasi pengaruh media interaktif terhadap hasil belajar.")],
)

S_METODE = dict(
    type="steps", kicker="Metodologi", title="Alur Penelitian",
    items=[("search", "Studi Pendahuluan", "Observasi kelas dan survei awal siswa"),
           ("clipboard-list", "Penyusunan Instrumen", "Angket motivasi dan soal tes, uji validitas"),
           ("flask-conical", "Perlakuan", "Kelas eksperimen memakai media interaktif"),
           ("database", "Pengumpulan Data", "Pre-test, post-test, dan angket"),
           ("chart-column", "Analisis Data", "Uji prasyarat, uji t, dan regresi")],
)

S_SAMPEL = dict(
    type="cards3", kicker="Metodologi", title="Populasi, Sampel, dan Teknik Analisis",
    items=[("users", "Populasi", "180 siswa", "Seluruh siswa kelas XI pada 5 rombongan belajar"),
           ("filter", "Sampel", "72 siswa", "2 kelas dipilih dengan cluster random sampling"),
           ("chart-line", "Analisis", "SPSS 26", "Uji normalitas, homogenitas, uji t, dan "
                                                  "regresi linear sederhana")],
)

S_HASIL = dict(
    type="chart_bar", kicker="Hasil Penelitian", title="Perbandingan Nilai Rata-rata",
    chart_title="Nilai rata-rata pre-test dan post-test",
    categories=["Pre-test", "Post-test", "Motivasi"],
    series=[("Kelas Eksperimen", (70.2, 86.5, 82.1)), ("Kelas Kontrol", (69.8, 76.3, 71.4))],
    insights=[("+16,3", "kenaikan nilai kelas eksperimen, dibanding +6,5 pada kelas kontrol"),
              ("82,1", "skor motivasi kelas eksperimen (kategori tinggi)")],
    notes="Klik kanan grafik > Edit Data untuk mengganti angka.",
)

S_GRAFIK = dict(
    type="chart_mix", kicker="Hasil Penelitian", title="Sebaran Kategori dan Perkembangan Nilai",
    pie=dict(title="Kategori motivasi (kelas eksperimen)",
             categories=["Sangat tinggi", "Tinggi", "Sedang", "Rendah"],
             values=(28, 47, 19, 6)),
    line=dict(title="Rata-rata nilai per pertemuan",
              min=60, categories=["P1", "P2", "P3", "P4", "P5", "P6"],
              series=[("Eksperimen", (70, 74, 78, 81, 84, 87)),
                      ("Kontrol", (70, 71, 72, 74, 75, 76))]),
)

S_UJI = dict(
    type="table_slide", kicker="Hasil Penelitian", title="Hasil Uji Hipotesis",
    rows=[["Hipotesis", "Koefisien", "t hitung", "Sig.", "Keputusan"],
          ["H1: Media → Motivasi", "0,512", "5,214", "0,000", "Diterima"],
          ["H2: Media → Hasil Belajar", "0,438", "4,327", "0,000", "Diterima"],
          ["H3: Mediasi motivasi", "0,224", "2,981", "0,004", "Diterima"],
          ["R² (koefisien determinasi)", "0,416", "—", "—", "41,6% pengaruh"]],
    col_widths=[4.0, 1.9, 1.9, 1.7, 2.4],
    align=["l", "c", "c", "c", "c"],
    note="α = 0,05. Hipotesis diterima jika Sig. < 0,05.",
)

S_FOTO = dict(
    type="photos", kicker="Hasil Penelitian", title="Dokumentasi Penelitian",
    captions=["Pelaksanaan pre-test", "Pembelajaran dengan media", "Pengisian angket"],
)

S_BAHAS = dict(
    type="discussion", kicker="Pembahasan", title="Pembahasan",
    quote="Media interaktif membuat siswa lebih aktif bertanya dan mencoba, sehingga materi "
          "lebih mudah diingat.",
    source="Temuan observasi, pertemuan ke-4",
    points=["Sejalan dengan teori: Mayer (2009) tentang pembelajaran multimedia",
            "Mendukung temuan: Pratama (2022) dan Lestari (2023)",
            "Perbedaan: pengaruh terbesar pada aspek perhatian, bukan kepuasan",
            "Keterbatasan: durasi perlakuan relatif singkat (6 minggu)"],
)

S_KESIMPULAN = dict(
    type="conclusion", kicker="Penutup", title="Kesimpulan dan Saran",
    left=("circle-check", "Kesimpulan",
          ["Media interaktif berpengaruh signifikan terhadap motivasi belajar (H1 diterima)",
           "Media interaktif berpengaruh signifikan terhadap hasil belajar (H2 diterima)",
           "Motivasi memediasi pengaruh media terhadap hasil belajar (H3 diterima)"]),
    right=("lightbulb", "Saran",
           ["Guru dapat memadukan media interaktif dengan diskusi kelompok",
            "Sekolah menyediakan akses internet yang stabil di kelas",
            "Peneliti berikutnya menambah durasi dan variasi materi"]),
)

S_PUSTAKA = dict(
    type="references", kicker="Referensi", title="Daftar Pustaka",
    refs=["Arsyad, A. (2019). Media pembelajaran (Edisi revisi). Jakarta: Rajawali Pers.",
          "Lestari, D. (2023). Pengembangan multimedia interaktif pada pembelajaran IPA. "
          "Jurnal Pendidikan Sains, 11(2), 45–57.",
          "Mayer, R. E. (2009). Multimedia learning (2nd ed.). Cambridge University Press.",
          "Pratama, R. (2022). Gamifikasi kuis daring dan hasil belajar siswa. Jurnal "
          "Teknologi Pendidikan, 24(1), 12–25.",
          "Santrock, J. W. (2018). Educational psychology (6th ed.). New York: McGraw-Hill.",
          "Sari, N. (2021). Pengaruh media video terhadap minat belajar siswa. Jurnal "
          "Inovasi Pendidikan, 9(3), 201–210.",
          "Sugiyono. (2022). Metode penelitian kuantitatif, kualitatif, dan R&D. "
          "Bandung: Alfabeta."],
)

AGENDA_SIDANG = dict(
    type="agenda", kicker="Daftar Isi", title="Alur Presentasi",
    items=[("Pendahuluan", "Latar belakang, rumusan masalah, tujuan"),
           ("Tinjauan Pustaka", "Penelitian terdahulu dan kerangka pemikiran"),
           ("Metodologi", "Alur penelitian, populasi, dan sampel"),
           ("Hasil Penelitian", "Data, grafik, dan uji hipotesis"),
           ("Pembahasan", "Temuan dikaitkan dengan teori"),
           ("Penutup", "Kesimpulan dan saran")],
)

AGENDA_PROPOSAL = dict(
    type="agenda", kicker="Daftar Isi", title="Alur Presentasi",
    items=[("Pendahuluan", "Latar belakang dan rumusan masalah"),
           ("Tujuan & Batasan", "Tujuan, manfaat, dan ruang lingkup"),
           ("Tinjauan Pustaka", "Penelitian terdahulu dan kerangka"),
           ("Hipotesis", "Dugaan sementara penelitian"),
           ("Metodologi", "Alur, populasi, sampel, analisis"),
           ("Jadwal", "Rencana waktu pelaksanaan")],
)

S_JADWAL = dict(
    type="gantt", kicker="Rencana", title="Jadwal Penelitian",
    months=["Jan", "Feb", "Mar", "Apr", "Mei", "Jun"],
    rows=[("Penyusunan proposal", 0, 1), ("Seminar proposal", 1, 1),
          ("Penyusunan instrumen", 1, 2), ("Pengumpulan data", 2, 3),
          ("Analisis data", 3, 4), ("Penulisan laporan", 4, 5), ("Sidang skripsi", 5, 5)],
)


def div(num, title, sub):
    return dict(type="divider", num=num, title=title, subtitle=sub)


SIDANG = [
    dict(type="cover", **COVER),
    AGENDA_SIDANG,
    div("01", "Pendahuluan", "Latar belakang, rumusan masalah, tujuan, dan batasan penelitian"),
    S_LATAR, S_RUMUSAN, S_TUJUAN, S_BATASAN,
    div("02", "Kajian dan Metode", "Penelitian terdahulu, kerangka pemikiran, dan metodologi"),
    S_KAJIAN, S_KERANGKA, S_METODE, S_SAMPEL,
    div("03", "Hasil dan Pembahasan", "Data penelitian, uji hipotesis, dan pembahasan temuan"),
    S_HASIL, S_GRAFIK, S_UJI, S_FOTO, S_BAHAS,
    div("04", "Penutup", "Kesimpulan, saran, dan daftar pustaka"),
    S_KESIMPULAN, S_PUSTAKA,
    dict(type="closing", **CLOSING),
]

PROPOSAL = [
    dict(type="cover", **{**COVER, "jenis": "Seminar Proposal"}),
    AGENDA_PROPOSAL,
    div("01", "Pendahuluan", "Latar belakang, rumusan masalah, tujuan, dan batasan penelitian"),
    S_LATAR, S_RUMUSAN, S_TUJUAN, S_BATASAN,
    div("02", "Tinjauan Pustaka", "Penelitian terdahulu, kerangka pemikiran, dan hipotesis"),
    S_KAJIAN, S_KERANGKA, S_HIPOTESIS,
    div("03", "Metodologi", "Rancangan, populasi dan sampel, serta jadwal penelitian"),
    S_METODE, S_SAMPEL, S_JADWAL, S_PUSTAKA,
    dict(type="closing", **CLOSING),
]

DECKS = [
    # (nama file, judul tampilan, slide, meta footer)
    ("Sidang-Skripsi", "Sidang Skripsi", SIDANG, META),
    ("Seminar-Proposal", "Seminar Proposal", PROPOSAL, META_PROPOSAL),
]
