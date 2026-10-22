# Template-Dokumen

Pabrik produk digital template (PPT, CV, dokumen) untuk dijual di **Lynk.id, Shopee, dan Gumroad**.
Semua file dibuat otomatis dari kode Python, jadi desain konsisten dan mudah diperbarui.

![Foto utama paket Sidang Skripsi](preview/sidang_skripsi/01-foto-utama.jpg)

## Daftar paket

| # | Paket | Isi | Status |
|---|-------|-----|--------|
| 1 | [Template PPT Sidang Skripsi & Seminar Proposal](preview/sidang_skripsi/) | 5 tema × (22 + 17 slide) = 195 slide, PPTX + PDF | ✅ Selesai (v1.0) |
| 2 | [Template CV ATS & Surat Lamaran](preview/cv_ats/) | 5 desain CV + 5 surat lamaran, Word (.docx) + PDF | ✅ Selesai (v1.0) |
| 3 | [Template PPT Presentasi Tugas Kuliah](preview/tugas_kuliah/) | 5 tema baru (Ceria, Neo Brutal, Alam, Tekno, Retro) × 20 slide, PPTX + PDF | ✅ Selesai (v1.0) |
| 4 | [Template Laporan Praktikum](preview/laporan_praktikum/) | 4 contoh (Kimia, Biologi, Fisika, Informatika) + 1 versi kosong, Word + PDF, daftar isi otomatis | ✅ Selesai (v1.0) |
| 5 | Pitch Deck Bisnis / UMKM | 5 tema, slide investor & proposal usaha | ⏳ Antre |
| 6 | Template Instagram Jualan | Feed & story 1080 px, PPTX bisa diedit | ⏳ Antre |
| 7 | Notion Planner Kuliah | Template Notion + panduan impor | ⏳ Antre |

## Isi tiap paket

Setiap paket menghasilkan:

- **ZIP untuk pembeli**: file yang bisa diedit (.pptx / .docx), versi PDF, `CARA-PAKAI.txt`, `LISENSI.txt`
- **Bahan jualan** (`marketing/`): foto produk 1080×1080 (foto utama, per tema, isi paket),
  banner 1280×720 untuk Gumroad, PDF pratinjau bertanda air, dan deskripsi jualan bahasa Indonesia

Pratinjau yang sudah jadi bisa dilihat di folder [`preview/`](preview/).

## Cara mendapatkan ZIP siap jual

**Lewat GitHub Actions (tanpa instal apa pun):**
1. Buka tab **Actions** > workflow **Build paket siap jual** > run terbaru.
2. Unduh artifact **zip-siap-jual** (file untuk pembeli) dan **bahan-marketing**.
3. Untuk rilis permanen, buat tag `v1.0` dst.: ZIP otomatis terlampir di halaman **Releases**.

**Di komputer sendiri:**
```bash
sudo apt install libreoffice-impress libreoffice-writer poppler-utils fonts-crosextra-carlito fonts-crosextra-caladea
pip install -r requirements.txt
python build.py                  # semua paket
python build.py sidang_skripsi   # satu paket
python build.py --fast           # hanya .pptx, tanpa PDF & mockup
```
Hasil ada di `dist/<paket>/`.

## Struktur

```
build.py                  # bangun paket -> dist/
templategen/
  core.py                 # helper bentuk, teks, ikon, grafik, tabel (python-pptx)
  docx_kit.py             # helper dokumen Word ramah ATS (python-docx)
  themes.py               # 5 tema skripsi: Modern, Minimalis, Akademik Biru, Gelap Elegan, Pastel
  themes_kuliah.py        # 5 tema kuliah: Ceria, Neo Brutal, Alam, Tekno, Retro
  slides.py               # tata letak slide isi (agenda, statistik, grafik, Gantt, ...)
  mockup.py               # foto produk & PDF pratinjau (slide 16:9 dan dokumen A4)
  render.py               # PPTX -> PDF -> PNG (LibreOffice + Poppler)
paket/<nama>/
  content.py              # isi slide
  package.py              # metadata, panduan pembeli, deskripsi jualan
assets/icons/             # ikon Lucide (ISC)
assets/fonts/             # Inter (OFL), hanya untuk mockup
preview/                  # salinan mockup untuk dilihat di GitHub
```

## Catatan kualitas

- Warna slide memakai **warna tema PowerPoint**, jadi pembeli bisa ganti palet lewat Design > Variants > Colors.
- Font slide hanya font bawaan Office (Calibri, Cambria, Arial), aman di laptop mana pun.
- Grafik dan tabel adalah objek asli PowerPoint (bisa Edit Data), bukan gambar.
- Tiap paket dicek visual (render semua slide) sebelum di-commit. Tetap cek ulang sebelum diunggah ke toko.

## Lisensi aset

- Ikon: [Lucide](https://lucide.dev) — ISC
- Font mockup: Inter — SIL Open Font License
