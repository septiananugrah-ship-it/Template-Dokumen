"""Isi contoh Pitch Deck Bisnis/UMKM. Brand dan angka fiktif."""
from templategen.themes_elegan import THEMES  # noqa: F401

META = "KopiKita  ·  Pitch Deck 2026  ·  Rahasia"

COVER = dict(
    brand="KopiKita",
    jenis="Pitch Deck · Pendanaan Tahap Awal",
    judul="Kopi Susu Gula Aren Siap Minum untuk Semua",
    tagline="Rasa kedai kopi, harga warung, tersedia di 1.200 toko di Jawa Barat.",
    meta="Jakarta, Oktober 2026  ·  Nama Pendiri, CEO",
    photo="Foto produk",
)

CLOSING = dict(
    judul="Mari Tumbuh Bersama",
    sub="Terima kasih. Kami siap berdiskusi lebih lanjut.",
    kontak=[("mail", "halo@kopikita.id"), ("phone", "0812-3456-7890"),
            ("globe", "kopikita.id")],
)


def div(num, title, sub):
    return dict(type="divider", num=num, title=title, subtitle=sub)


SLIDES = [
    dict(type="cover", **COVER),
    dict(type="agenda", kicker="Ringkasan", title="Isi Presentasi",
         items=[("Masalah & Solusi", "Peluang yang kami lihat"),
                ("Produk", "Apa yang kami jual"),
                ("Pasar", "Ukuran dan target pasar"),
                ("Model Bisnis & Traksi", "Cara kami menghasilkan uang"),
                ("Tim", "Orang di balik KopiKita"),
                ("Pendanaan", "Kebutuhan dan penggunaan dana")]),
    div("01", "Masalah & Solusi", "Mengapa KopiKita perlu ada"),
    dict(type="numbered", kicker="Masalah", title="Masalah yang Kami Lihat",
         items=[("Mahal", "Segelas kopi susu di kedai rata-rata Rp22.000, berat untuk "
                          "pelajar dan pekerja harian"),
                ("Sulit dijangkau", "Kedai kopi terkonsentrasi di kota besar; 70% kecamatan "
                                    "belum punya kedai kopi modern"),
                ("Tidak awet", "Kopi susu segar hanya tahan beberapa jam, sulit dijual di "
                               "warung dan minimarket")]),
    dict(type="image_text", kicker="Solusi", title="Solusi Kami",
         heading="Kopi susu gula aren dalam kemasan, tahan 6 bulan tanpa pengawet",
         points=[("badge-check", "Rasa konsisten", "Resep barista, diproduksi dengan "
                                                   "standar HACCP"),
                 ("wallet", "Harga terjangkau", "Rp8.000 per botol 200 mL"),
                 ("store", "Ada di dekatmu", "Dijual di warung, minimarket, dan e-commerce")],
         photo="Foto produk"),
    div("02", "Produk & Pasar", "Apa yang kami jual dan untuk siapa"),
    dict(type="cards3", kicker="Produk", title="Lini Produk",
         items=[("coffee", "Andalan", "Gula Aren", "Kopi susu gula aren klasik, 65% "
                                                    "dari penjualan"),
                ("leaf", "Baru", "Oat Latte", "Pilihan susu nabati untuk konsumen sehat"),
                ("package", "Grosir", "Literan 1 L", "Untuk kafe dan katering kantor")]),
    dict(type="market", kicker="Pasar", title="Ukuran Pasar",
         levels=[("TAM", "Rp24 T", "Pasar kopi siap minum di Indonesia per tahun"),
                 ("SAM", "Rp6,1 T", "Segmen kopi susu kemasan di Pulau Jawa"),
                 ("SOM", "Rp180 M", "Target pangsa 3% dalam 3 tahun")],
         note="Sumber: contoh data. Ganti dengan riset pasar Anda (BPS, laporan industri)."),
    dict(type="check_table", kicker="Kompetitor", title="Posisi Kami di Pasar",
         headers=["Fitur", "KopiKita", "Kedai Kopi", "Kopi Sachet", "Merek Kemasan X"],
         rows=[["Harga di bawah Rp10.000", "v", "x", "v", "x"],
               ["Rasa kopi susu kedai", "v", "v", "x", "v"],
               ["Tahan lama tanpa kulkas", "v", "x", "v", "v"],
               ["Ada di warung kecil", "v", "x", "v", "x"],
               ["Bahan lokal (gula aren)", "v", "v", "x", "x"]]),
    div("03", "Bisnis & Traksi", "Bagaimana kami tumbuh"),
    dict(type="steps", kicker="Model Bisnis", title="Cara Kami Menjual",
         items=[("factory", "Produksi", "Pabrik mitra bersertifikat BPOM & halal"),
                ("truck", "Distribusi", "Distributor regional ke 1.200 toko"),
                ("store", "Toko & Warung", "Margin 25% untuk mitra toko"),
                ("shopping-cart", "Online", "Shopee, Tokopedia, TikTok Shop"),
                ("repeat", "Langganan", "Paket mingguan untuk kantor")]),
    dict(type="chart_bar", kicker="Traksi", title="Pertumbuhan Penjualan",
         chart_title="Penjualan bulanan (ribu botol)",
         categories=["Jan", "Mar", "Mei", "Jul", "Sep"],
         series=[("Penjualan", (18, 32, 51, 76, 112))],
         insights=[("6,2×", "pertumbuhan penjualan dalam 8 bulan"),
                   ("38%", "pembeli melakukan pembelian ulang tiap bulan")],
         number_format="0"),
    dict(type="table_slide", kicker="Keuangan", title="Proyeksi Keuangan",
         rows=[["(Rp juta)", "2026", "2027", "2028"],
               ["Pendapatan", "4.800", "11.500", "24.000"],
               ["Laba kotor", "1.900", "4.900", "10.800"],
               ["Margin kotor", "40%", "43%", "45%"],
               ["Laba bersih", "-350", "1.150", "3.600"]],
         col_widths=[4.0, 2.6, 2.6, 2.6], align=["l", "c", "c", "c"],
         note="Proyeksi berdasarkan asumsi penambahan 600 toko per tahun."),
    dict(type="team_photo", kicker="Tim", title="Tim Pendiri",
         members=[("Nama Pendiri", "CEO", "10 tahun di industri FMCG"),
                  ("Nama Pendiri", "COO", "Mantan manajer pabrik minuman"),
                  ("Nama Pendiri", "CMO", "Membangun 3 merek viral di TikTok"),
                  ("Nama Pendiri", "Head of R&D", "Q-grader kopi bersertifikat")]),
    dict(type="timeline", kicker="Rencana", title="Peta Jalan",
         items=[("Q1 2026", "Pabrik sendiri", "Kapasitas 300 ribu botol/bulan"),
                ("Q3 2026", "Jawa Tengah", "Masuk 800 toko baru"),
                ("Q1 2027", "Varian baru", "Teh susu & cokelat"),
                ("Q3 2027", "Ekspor", "Uji pasar Malaysia"),
                ("2028", "Seri A", "Ekspansi nasional")]),
    dict(type="funds", kicker="Pendanaan", title="Kebutuhan Dana",
         amount="Rp2,5 M",
         caption="Pendanaan tahap awal untuk 18 bulan operasional, ditukar dengan 15% saham.",
         uses=[("Mesin produksi", 40, "Mesin pengisian & sterilisasi"),
               ("Pemasaran", 30, "Iklan digital & promosi toko"),
               ("Distribusi", 20, "Armada & gudang regional"),
               ("Operasional", 10, "Tim & perizinan")]),
    dict(type="closing", **CLOSING),
]

DECKS = [("Pitch-Deck", "Pitch Deck", SLIDES, META)]
