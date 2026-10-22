"""Isi contoh Template PPT Materi Ajar Guru (Kurikulum Merdeka)."""
from templategen.themes_elegan import GURU as THEMES  # noqa: F401

META = "IPA Kelas VIII  ·  Fotosintesis  ·  Nama Guru"

COVER = dict(
    kampus="SMP Negeri Nama Sekolah",
    fakultas="",
    jenis="Ilmu Pengetahuan Alam · Kelas VIII · Fase D",
    judul="Fotosintesis: Cara Tumbuhan Membuat Makanan",
    nama="Nama Guru, S.Pd.",
    nim="Pertemuan 3 · 2 × 40 menit",
    pembimbing="Semester Ganjil 2026/2027",
    tahun="Kurikulum Merdeka",
)

CLOSING = dict(
    judul="Terima Kasih",
    sub="Sampai jumpa di pertemuan berikutnya!",
    kontak=[("book-open", "Buku siswa hlm. 45–52"), ("mail", "guru@sekolah.sch.id"),
            ("clipboard-list", "Tugas: kumpulkan Senin")],
)


def div(num, title, sub):
    return dict(type="divider", num=num, title=title, subtitle=sub)


SLIDES = [
    dict(type="cover", **COVER),
    dict(type="numbered", kicker="Tujuan Pembelajaran", title="Setelah Belajar, Kamu Dapat",
         items=[("Menjelaskan", "pengertian fotosintesis dan tempat terjadinya"),
                ("Menyebutkan", "bahan dan hasil fotosintesis beserta persamaan reaksinya"),
                ("Menganalisis", "faktor yang memengaruhi laju fotosintesis melalui percobaan")]),
    dict(type="big_question", kicker="Pertanyaan Pemantik", title="Coba Pikirkan",
         question="Kita makan nasi dan lauk agar punya energi. Lalu, tumbuhan makan apa?",
         hint="Diskusikan dengan teman sebangku selama 2 menit."),
    dict(type="agenda", kicker="Alur Belajar", title="Kegiatan Hari Ini",
         items=[("Pendahuluan", "Apersepsi dan pertanyaan pemantik"),
                ("Materi", "Pengertian, bahan, dan hasil"),
                ("Contoh Soal", "Membaca persamaan reaksi"),
                ("Percobaan", "Kerja kelompok Ingenhousz"),
                ("Kuis", "Cek pemahaman"),
                ("Refleksi", "Apa yang sudah kamu pelajari")]),
    div("01", "Materi", "Mengenal proses fotosintesis"),
    dict(type="image_text", kicker="Materi", title="Apa Itu Fotosintesis?",
         heading="Proses tumbuhan hijau membuat makanan sendiri dengan bantuan cahaya",
         points=[("leaf", "Di daun", "Terjadi di kloroplas yang mengandung klorofil"),
                 ("sun", "Butuh cahaya", "Cahaya matahari menjadi sumber energi"),
                 ("sprout", "Menghasilkan makanan", "Glukosa dipakai untuk tumbuh")],
         photo="Gambar daun / kloroplas"),
    dict(type="icon_grid", kicker="Materi", title="Bahan dan Hasil Fotosintesis",
         items=[("droplets", "Air (H₂O)", "Diserap akar dari tanah"),
                ("wind", "Karbon dioksida (CO₂)", "Masuk lewat stomata daun"),
                ("candy", "Glukosa (C₆H₁₂O₆)", "Makanan untuk tumbuhan"),
                ("cloud", "Oksigen (O₂)", "Dilepas ke udara, kita hirup")]),
    dict(type="steps", kicker="Materi", title="Tahapan Fotosintesis",
         items=[("sun", "Cahaya diserap", "Klorofil menangkap energi cahaya"),
                ("droplets", "Air dipecah", "Air terurai, oksigen dilepas"),
                ("battery-charging", "Energi disimpan", "Terbentuk ATP dan NADPH"),
                ("wind", "CO₂ diikat", "Siklus Calvin di stroma"),
                ("candy", "Glukosa jadi", "Disimpan sebagai pati")]),
    dict(type="example", kicker="Contoh Soal", title="Membaca Persamaan Reaksi",
         problem="Lengkapi persamaan reaksi fotosintesis berikut:\n\n"
                 "6CO₂ + 6H₂O → ... + 6O₂\n\nZat apa yang dihasilkan selain oksigen?",
         steps=["Identifikasi bahan: karbon dioksida dan air",
                "Ingat hasil fotosintesis: glukosa dan oksigen",
                "Rumus kimia glukosa adalah C₆H₁₂O₆",
                "Periksa jumlah atom C, H, O di kedua ruas sudah seimbang"],
         result="Jawaban: C₆H₁₂O₆ (glukosa)"),
    div("02", "Percobaan", "Belajar dengan mengamati langsung"),
    dict(type="cards3", kicker="Kegiatan Kelompok", title="Percobaan Ingenhousz",
         items=[("flask-conical", "Alat & bahan", "Hydrilla", "Gelas, corong, tabung reaksi, "
                                                              "air, dan tanaman Hydrilla"),
                ("sun", "Perlakuan", "2 lokasi", "Satu di bawah cahaya matahari, satu di "
                                                  "tempat gelap"),
                ("eye", "Amati", "Gelembung", "Hitung gelembung oksigen setiap 5 menit")]),
    dict(type="table_slide", kicker="Lembar Kerja", title="Tabel Pengamatan",
         rows=[["Waktu (menit)", "Tempat Terang", "Tempat Gelap", "Keterangan"],
               ["5", "", "", ""], ["10", "", "", ""], ["15", "", "", ""],
               ["20", "", "", ""]],
         col_widths=[2.6, 3.0, 3.0, 3.3], align=["c", "c", "c", "l"],
         note="Isi jumlah gelembung yang kamu hitung."),
    div("03", "Evaluasi", "Cek pemahaman dan refleksi"),
    dict(type="quiz", kicker="Kuis", title="Soal 1",
         question="Di bagian sel manakah fotosintesis terjadi?",
         options=["Mitokondria", "Kloroplas", "Ribosom", "Inti sel"]),
    dict(type="quiz", kicker="Kuis · Pembahasan", title="Soal 1",
         question="Di bagian sel manakah fotosintesis terjadi?",
         options=["Mitokondria", "Kloroplas", "Ribosom", "Inti sel"], answer="B"),
    dict(type="conclusion", kicker="Rangkuman", title="Yang Kita Pelajari",
         left=("circle-check", "Poin Penting",
               ["Fotosintesis terjadi di kloroplas daun",
                "Bahan: air dan CO₂; hasil: glukosa dan O₂",
                "Cahaya adalah sumber energinya"]),
         right=("lightbulb", "Hubungan dengan Kita",
                ["Oksigen yang kita hirup berasal dari fotosintesis",
                 "Makanan kita bergantung pada tumbuhan",
                 "Menanam pohon menjaga udara tetap bersih"])),
    dict(type="reflection", kicker="Refleksi", title="Refleksi Hari Ini",
         prompts=[("smile", "Hal baru apa yang kamu pelajari hari ini?"),
                  ("circle-help", "Bagian mana yang masih membingungkan?"),
                  ("target", "Apa yang ingin kamu ketahui selanjutnya?")]),
    dict(type="closing", **CLOSING),
]

DECKS = [("Materi-Ajar", "Materi Ajar", SLIDES, META)]
