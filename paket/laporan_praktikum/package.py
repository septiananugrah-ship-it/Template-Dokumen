"""Paket 4: Template Laporan Praktikum (Word)."""
from __future__ import annotations

from .content import REPORTS
from .report import build_with_toc


def make(prod):
    groups = []
    work = prod.parent / "_toc"
    work.mkdir(exist_ok=True)
    for i, data in enumerate(REPORTS, 1):
        folder = prod / f"{i}. {data['label']}"
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / f"Laporan-Praktikum_{data['key']}.docx"
        build_with_toc(data, path, work)
        groups.append((f"Versi {data['label']}", "1F3A5F", [path]))
    work.rmdir()
    return groups


PACKAGE = dict(
    kind="docs",
    title="Template Laporan Praktikum",
    short="Template Laporan Praktikum (Word)",
    folder="Template-Laporan-Praktikum",
    version="1.0",
    badge="5 VERSI · FORMAT KAMPUS",
    headline=["Template", "Laporan Praktikum", "Siap Pakai"],
    tagline="Sampul, pengesahan, daftar isi otomatis, BAB I–V.",
    chips=["Word · Google Docs · WPS", "Contoh isi lengkap"],
    show=[0, 2, 3, 6],
    features=[
        "4 contoh: Kimia, Biologi, Fisika, Informatika",
        "+ 1 versi kosong berpanduan untuk semua jurusan",
        "Daftar isi otomatis & nomor halaman i, ii / 1, 2",
        "Times New Roman 12, spasi 1,5, margin 4-3-3-3",
    ],
    docs={
        "CARA-PAKAI.txt": """
TEMPLATE LAPORAN PRAKTIKUM
==========================

Isi paket (5 folder):
  1. Kimia        - contoh: titrasi asam-basa (kadar asam asetat cuka)
  2. Biologi      - contoh: pengamatan sel tumbuhan & hewan
  3. Fisika       - contoh: percepatan gravitasi dengan bandul
  4. Informatika  - contoh: stack & queue (ada kotak kode program)
  5. Kosong       - semua bagian berisi petunjuk [dalam kurung siku]
Tiap folder berisi file .docx (bisa diedit) dan versi PDF.

Struktur laporan:
  Sampul - Lembar Pengesahan - Daftar Isi - BAB I Pendahuluan -
  BAB II Tinjauan Pustaka - BAB III Metodologi - BAB IV Hasil &
  Pembahasan - BAB V Kesimpulan & Saran - Daftar Pustaka - Lampiran

Format: A4, Times New Roman 12, spasi 1,5, margin kiri 4 cm, atas/kanan/
bawah 3 cm. Halaman awal bernomor romawi (i, ii), isi bernomor 1, 2, 3.
Silakan sesuaikan dengan pedoman kampusmu.

CARA MENGEDIT
1. Buka .docx di Microsoft Word / Google Docs / WPS.
2. Ganti teks contoh. Data percobaan di contoh adalah data karangan,
   wajib diganti dengan data hasil praktikummu sendiri.
3. DAFTAR ISI: setelah selesai mengedit, klik kanan daftar isi >
   Update Field > Update entire table. Nomor halaman menyesuaikan.
   (Google Docs: Insert > Table of contents untuk membuat ulang.)
4. Tambah subbab: ketik judul, lalu pilih style "Heading 2" agar ikut
   masuk daftar isi. Judul BAB memakai style "Heading 1".
5. Gambar: klik kotak bertuliskan "Tempel foto / gambar di sini", hapus
   teksnya, lalu Insert > Pictures.
6. Tabel: klik kanan baris > Insert > Insert Rows Below.
7. Logo kampus di sampul: klik kotak LOGO KAMPUS, hapus teks, Insert >
   Pictures, atur ukuran sekitar 4 x 4 cm.

Ada kendala? Hubungi penjual lewat chat toko.
""",
        "LISENSI.txt": """
LISENSI PENGGUNAAN

BOLEH: dipakai untuk laporan praktikum/tugas pribadi, diedit dan
dipakai berkali-kali.

TIDAK BOLEH: menjual ulang atau membagikan file template ini sebagai
template. Contoh isi hanya ilustrasi; jangan dikumpulkan sebagai hasil
praktikum tanpa data milikmu sendiri.
""",
    },
    description="""
# Template Laporan Praktikum Word (5 Versi, Daftar Isi Otomatis)

**Judul produk (Shopee):**
Template Laporan Praktikum Word Kimia Biologi Fisika Informatika Daftar Isi Otomatis Bisa Edit

**Harga saran:** Rp15.000 (coret Rp35.000) · Gumroad: $2

---

Capek merapikan format laporan praktikum setiap minggu? Pakai template ini: sampul, lembar pengesahan, daftar isi, sampai lampiran sudah tertata. Kamu tinggal fokus ke isi dan data.

## Isi paket
- **4 contoh lengkap**: Kimia (titrasi), Biologi (pengamatan sel), Fisika (bandul), Informatika (stack & queue, dengan kotak kode program)
- **1 versi kosong berpanduan** yang cocok untuk semua jurusan
- Format **Word (.docx)** + **PDF**

## Sudah termasuk
- Sampul dengan tempat logo kampus
- Lembar pengesahan (tanda tangan asisten, praktikan, dosen)
- **Daftar isi otomatis** (klik kanan > Update Field)
- Nomor halaman **romawi (i, ii)** untuk bagian awal dan **angka (1, 2, 3)** untuk isi
- BAB I–V, tabel alat & bahan, tabel data, kotak gambar dengan keterangan, perhitungan
- Daftar pustaka format APA

## Format
A4 · Times New Roman 12 · spasi 1,5 · margin 4-3-3-3 cm (bisa disesuaikan pedoman kampus)

## Catatan
- Contoh data adalah ilustrasi, ganti dengan data praktikummu sendiri
- Produk digital, untuk pemakaian pribadi, dilarang dijual ulang

**Tag:** template laporan praktikum, laporan praktikum word, format laporan praktikum, laporan kimia, laporan biologi, laporan fisika, template word kuliah, daftar isi otomatis
""",
)
