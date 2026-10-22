"""Isi contoh Template Instagram Jualan (toko fiktif tas rajut handmade)."""
from templategen.social import FEED, STORY
from templategen.themes_elegan import THEMES as _A, KULIAH as _B

# lima tema elegan untuk feed toko (gabungan palet yang paling cocok untuk jualan)
THEMES = [_A[0], _A[1], _A[3], _B[0], _B[2]]  # Monokrom, Hitam Emas, Batu, Marun, Hutan

BRAND = "Laras Rajut"
HANDLE = "@larasrajut"

FEED_POSTS = [
    dict(type="new_arrival", kicker="New Arrival", name="Tas Rajut Senja", price="Rp189.000",
         note="Stok terbatas"),
    dict(type="promo", kicker="Promo Gajian", big="40%", sub="Diskon semua tas rajut",
         period="25–30 November 2026", cta="Belanja Sekarang"),
    dict(type="grid4", title="Koleksi Terlaris",
         items=[("Tas Senja", "Rp189rb"), ("Pouch Mini", "Rp79rb"),
                ("Totebag Laut", "Rp159rb"), ("Dompet Koin", "Rp49rb")]),
    dict(type="testimonial",
         quote="Rajutannya rapi banget, warnanya sama persis kayak di foto. Pasti order lagi!",
         name="Nadia, Bandung", detail="Membeli Tas Rajut Senja"),
    dict(type="carousel_cover", kicker="Tips Perawatan",
         title="5 Cara Merawat Tas Rajut agar Awet Bertahun-tahun"),
    dict(type="carousel_item", num=1, total=5, icon="droplets", title="Cuci dengan tangan",
         body="Rendam di air dingin dengan sabun lembut. Hindari mesin cuci agar bentuk "
              "rajutan tidak melar."),
    dict(type="carousel_item", num=2, total=5, icon="sun", title="Jemur di tempat teduh",
         body="Sinar matahari langsung membuat warna benang cepat pudar. Keringkan dengan "
              "posisi tidur, jangan digantung."),
    dict(type="price_list", title="Daftar Harga",
         rows=[("Tas Rajut Senja", "Ukuran 30 × 25 cm", "Rp189.000"),
               ("Totebag Laut", "Muat laptop 14 inci", "Rp159.000"),
               ("Pouch Mini", "Untuk kosmetik & kabel", "Rp79.000"),
               ("Dompet Koin", "Ritsleting YKK", "Rp49.000"),
               ("Custom Warna", "Pengerjaan 7 hari", "+Rp20.000")],
         note="Harga belum termasuk ongkos kirim"),
    dict(type="before_after", title="Dari Benang Jadi Tas", left="Proses", right="Hasil"),
    dict(type="bundle", kicker="Paket Hemat", name="Paket Kado Spesial",
         items=["1 Tas Rajut Senja", "1 Pouch Mini", "Kartu ucapan & kotak kado"],
         old="Rp268.000", new="Rp229.000"),
    dict(type="how_to_order", title="Cara Order",
         steps=[("message-circle", "Chat admin", "Kirim foto produk & warna pilihan"),
                ("credit-card", "Transfer", "Bayar ke rekening atau e-wallet"),
                ("package-check", "Dikemas", "Pesanan dikemas rapi dalam 1×24 jam"),
                ("truck", "Dikirim", "Nomor resi dikirim lewat WhatsApp")],
         contact="WA 0812-3456-7890"),
    dict(type="giveaway", title="Menangkan Tas Rajut Gratis!", prize="Untuk 3 pemenang",
         steps=["Follow akun @larasrajut", "Like & simpan postingan ini",
                "Tag 3 teman di kolom komentar"],
         deadline="Berakhir 30 November 2026"),
    dict(type="faq", title="Sering Ditanyakan",
         items=[("Bisa custom warna?", "Bisa, pilih dari 24 warna benang. Pengerjaan 7 hari."),
                ("Pengiriman dari mana?", "Dari Yogyakarta, bisa ke seluruh Indonesia."),
                ("Bisa COD?", "Bisa lewat marketplace Shopee dan Tokopedia kami.")]),
    dict(type="announcement", kicker="Pengumuman", title="Toko Libur Sementara",
         body="Pesanan yang masuk selama libur akan diproses mulai 2 Januari 2027.",
         date_text="29 Desember – 1 Januari"),
    dict(type="quote", text="Dibuat pelan-pelan, dengan tangan, untuk dipakai lama.",
         author="Laras Rajut"),
    dict(type="thanks", title="Terima Kasih!",
         sub="Sudah mendukung produk lokal buatan tangan."),
]

STORY_POSTS = [
    dict(type="story_promo", kicker="Flash Sale", big="50%", sub="Hanya hari ini, 12.00–15.00",
         cta="Cek Sekarang"),
    dict(type="story_product", kicker="Baru Rilis", name="Totebag Laut", price="Rp159.000"),
    dict(type="story_testimonial", quote="“Totebagnya kuat, muat laptop dan bekal!”",
         name="Rina, Jakarta"),
    dict(type="story_question", title="Mau warna apa untuk koleksi berikutnya?",
         prompt="Tulis jawabanmu"),
    dict(type="story_countdown", kicker="Segera Hadir", title="Koleksi Akhir Tahun",
         date_text="Rilis 1 Desember 2026, pukul 19.00"),
    dict(type="story_link", title="Belanja Lebih Mudah", sub="Semua produk ada di link bio "
                                                             "dan Shopee kami",
         cta="Klik Link di Bio"),
]


def _feed(theme, meta):
    from templategen.social import SocialBuilder
    return SocialBuilder(theme, FEED, BRAND, HANDLE)


def _story(theme, meta):
    from templategen.social import SocialBuilder
    return SocialBuilder(theme, STORY, BRAND, HANDLE)


DECKS = [("Feed-Instagram", "Feed 1:1", FEED_POSTS, "", _feed),
         ("Story-Instagram", "Story 9:16", STORY_POSTS, "", _story)]
