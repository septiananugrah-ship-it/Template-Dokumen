"""Isi contoh paket Template Presentasi Tugas Kuliah (kelompok)."""
from templategen.themes_kuliah import THEMES  # noqa: F401  (dipakai build.py)

META = "Tugas Kelompok  ·  Mata Kuliah  ·  Kelompok 3"

COVER = dict(
    kampus="Universitas Nama Kampus",
    fakultas="Fakultas Ilmu Sosial dan Ilmu Politik",
    jenis="Tugas Kelompok · Psikologi Sosial",
    judul="Dampak Media Sosial terhadap Kesehatan Mental Remaja",
    nama="Kelompok 3",
    nim="Kelas B · Semester 3",
    pembimbing="Dosen Pengampu: Dr. Nama Dosen, M.Si.",
    pembimbing_list="Dr. Nama Dosen, M.Si.",
    tahun="Tahun Akademik 2025/2026",
)

CLOSING = dict(
    judul="Terima Kasih",
    sub="Ada pertanyaan? Mari berdiskusi!",
    kontak=[("mail", "kelompok3@kampus.ac.id"), ("users", "Kelompok 3 · Kelas B"),
            ("at-sign", "@kelompok3")],
)


def div(num, title, sub):
    return dict(type="divider", num=num, title=title, subtitle=sub)


SLIDES = [
    dict(type="cover", **COVER),
    dict(type="team", kicker="Kelompok 3", title="Anggota Kelompok",
         members=[("Aulia Rahma", "2301110021", "Ketua"),
                  ("Bima Saputra", "2301110034", "Materi"),
                  ("Citra Lestari", "2301110047", "Data"),
                  ("Dimas Prakoso", "2301110058", "Desain"),
                  ("Eka Putri", "2301110063", "Notulen")]),
    dict(type="agenda", kicker="Daftar Isi", title="Yang Akan Kami Bahas",
         items=[("Pendahuluan", "Latar belakang dan tujuan"),
                ("Pengertian", "Definisi menurut para ahli"),
                ("Perkembangan", "Sejarah singkat media sosial"),
                ("Data & Fakta", "Pola penggunaan remaja"),
                ("Dampak", "Sisi positif dan negatif"),
                ("Solusi", "Langkah yang bisa dilakukan")]),
    div("01", "Pendahuluan", "Mengapa topik ini penting untuk dibahas"),
    dict(type="text_stats", kicker="Pendahuluan", title="Latar Belakang",
         paragraphs=["Media sosial sudah menjadi bagian dari keseharian remaja: untuk "
                     "berteman, belajar, hingga mencari hiburan.",
                     "Di balik manfaatnya, banyak penelitian menemukan hubungan antara "
                     "penggunaan berlebihan dengan kecemasan, gangguan tidur, dan rasa "
                     "rendah diri.",
                     "Kelompok kami merangkum temuan tersebut dan menawarkan solusi praktis."],
         stats=[("167 jt", "pengguna media sosial di Indonesia (contoh data)"),
                ("3,5 jam", "rata-rata waktu remaja di media sosial per hari"),
                ("1 dari 3", "remaja merasa cemas jika tidak membuka ponsel")]),
    dict(type="numbered", kicker="Pendahuluan", title="Tujuan Pembahasan",
         items=[("Memahami", "Menjelaskan pengertian media sosial dan kesehatan mental"),
                ("Menganalisis", "Mengidentifikasi dampak positif dan negatif bagi remaja"),
                ("Memberi solusi", "Merumuskan langkah bijak menggunakan media sosial")]),
    div("02", "Pembahasan", "Pengertian, perkembangan, data, dan dampak"),
    dict(type="quotes", kicker="Pengertian", title="Definisi Menurut Para Ahli",
         items=[("Media sosial adalah sekelompok aplikasi berbasis internet yang "
                 "memungkinkan penciptaan dan pertukaran konten buatan pengguna.",
                 "Kaplan & Haenlein (2010)"),
                ("Kesehatan mental adalah kondisi sejahtera ketika individu menyadari "
                 "kemampuannya dan dapat mengatasi tekanan hidup yang wajar.",
                 "WHO (2022)"),
                ("Remaja adalah masa transisi dari kanak-kanak ke dewasa yang ditandai "
                 "perubahan fisik, emosi, dan sosial.", "Santrock (2019)")]),
    dict(type="icon_grid", kicker="Pembahasan", title="Platform yang Paling Sering Dipakai",
         items=[("message-circle", "Pesan Instan", "Mengobrol dengan teman dan grup kelas"),
                ("image", "Berbagi Foto", "Mengunggah momen dan mengikuti tren"),
                ("video", "Video Pendek", "Hiburan dan konten edukasi singkat"),
                ("users", "Komunitas", "Forum hobi, fandom, dan diskusi"),
                ("gamepad-2", "Game Online", "Bermain sambil bersosialisasi"),
                ("newspaper", "Berita & Info", "Mengikuti kabar terbaru")]),
    dict(type="timeline", kicker="Pembahasan", title="Perkembangan Media Sosial",
         items=[("1997", "Six Degrees", "Situs jejaring sosial pertama"),
                ("2004", "Facebook", "Jejaring sosial mulai populer"),
                ("2010", "Instagram", "Era berbagi foto"),
                ("2016", "TikTok", "Video pendek mendunia"),
                ("2024", "Era AI", "Konten dibantu kecerdasan buatan")]),
    dict(type="chart_bar", kicker="Data & Fakta", title="Durasi Penggunaan per Hari",
         chart_title="Rata-rata jam per hari menurut usia (data contoh)",
         categories=["13–15 th", "16–18 th", "19–21 th"],
         series=[("Hari sekolah", (2.4, 3.1, 3.6)), ("Akhir pekan", (3.8, 4.6, 4.9))],
         insights=[("4,9 jam", "waktu tertinggi, pada usia 19–21 tahun di akhir pekan"),
                   ("+48%", "kenaikan rata-rata saat akhir pekan dibanding hari sekolah")]),
    dict(type="compare", kicker="Dampak", title="Dampak Positif dan Negatif",
         left=("thumbs-up", "Dampak Positif",
               ["Mudah terhubung dengan teman dan keluarga",
                "Akses informasi dan materi belajar",
                "Wadah menyalurkan kreativitas",
                "Dukungan dari komunitas sehobi"]),
         right=("thumbs-down", "Dampak Negatif",
                ["Membandingkan diri dengan orang lain",
                 "Kurang tidur karena terus menggulir layar",
                 "Rentan perundungan siber",
                 "Kecanduan dan sulit fokus belajar"])),
    dict(type="chart_mix", kicker="Data & Fakta", title="Hasil Survei Kelompok",
         pie=dict(title="Perasaan setelah bermedia sosial (n=120)",
                  categories=["Senang", "Biasa saja", "Cemas", "Iri"],
                  values=(35, 30, 20, 15)),
         line=dict(title="Jam tidur vs durasi media sosial", min=5,
                   categories=["<1 j", "1–2 j", "2–3 j", "3–4 j", "4–5 j", ">5 j"],
                   series=[("Jam tidur", (8.1, 7.8, 7.3, 6.9, 6.4, 5.9))])),
    dict(type="discussion", kicker="Studi Kasus", title="Studi Kasus",
         quote="“Aku merasa hidupku biasa saja setiap melihat unggahan teman-teman.”",
         source="Responden, 17 tahun",
         points=["Fenomena: FOMO (fear of missing out) dan perbandingan sosial",
                 "Pemicu: melihat unggahan yang sudah disaring dan diedit",
                 "Akibat: rasa rendah diri dan cemas",
                 "Pelajaran: yang tampil di media sosial bukan gambaran utuh"]),
    dict(type="steps", kicker="Solusi", title="Tips Bijak Bermedia Sosial",
         items=[("clock", "Batasi Waktu", "Pakai fitur pengingat durasi di ponsel"),
                ("user-minus", "Saring Akun", "Berhenti mengikuti akun yang membuat cemas"),
                ("moon", "Jeda Malam", "Tanpa ponsel 1 jam sebelum tidur"),
                ("heart-handshake", "Cerita", "Bicarakan perasaan dengan orang terdekat"),
                ("activity", "Aktivitas Nyata", "Olahraga dan hobi di luar layar")]),
    div("03", "Penutup", "Kesimpulan, saran, dan bahan diskusi"),
    dict(type="conclusion", kicker="Penutup", title="Kesimpulan dan Saran",
         left=("circle-check", "Kesimpulan",
               ["Media sosial punya manfaat besar bagi remaja",
                "Penggunaan berlebihan berkaitan dengan cemas dan kurang tidur",
                "Kuncinya adalah kendali diri dan literasi digital"]),
         right=("lightbulb", "Saran",
                ["Remaja: atur waktu dan pilih konten yang sehat",
                 "Orang tua: dampingi tanpa menghakimi",
                 "Sekolah: adakan kelas literasi digital"])),
    dict(type="numbered", kicker="Diskusi", title="Pertanyaan Diskusi",
         items=[("Pengalaman", "Pernahkah kamu merasa cemas setelah membuka media sosial?"),
                ("Peran", "Siapa yang paling bertanggung jawab: pengguna, orang tua, "
                          "atau platform?"),
                ("Aturan", "Perlukah batas usia minimal yang lebih ketat untuk media "
                           "sosial?")]),
    dict(type="references", kicker="Referensi", title="Daftar Pustaka",
         refs=["Kaplan, A. M., & Haenlein, M. (2010). Users of the world, unite! Business "
               "Horizons, 53(1), 59–68.",
               "Santrock, J. W. (2019). Adolescence (17th ed.). New York: McGraw-Hill.",
               "Twenge, J. M. (2017). iGen. New York: Atria Books.",
               "World Health Organization. (2022). Mental health: Strengthening our response. "
               "Diakses dari who.int.",
               "Nama Penulis. (2023). Judul artikel jurnal yang relevan. Nama Jurnal, 5(2), "
               "10–20."]),
    dict(type="closing", **CLOSING),
]

DECKS = [("Presentasi-Tugas-Kuliah", "Presentasi Tugas Kuliah", SLIDES, META)]
