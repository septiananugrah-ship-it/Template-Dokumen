"""Paket 2: Template CV ATS & Surat Lamaran Kerja (Word)."""
from __future__ import annotations

from .designs import DESIGNS


def make(prod):
    groups = []
    for i, d in enumerate(DESIGNS, 1):
        folder = prod / f"{i}. {d.label}"
        folder.mkdir(parents=True, exist_ok=True)
        cv = folder / f"CV_{d.key}.docx"
        letter = folder / f"Surat-Lamaran_{d.key}.docx"
        d.cv(cv)
        d.letter(letter)
        accent = d.accent if d.accent != "111111" else "0E9F76"
        groups.append((f"Desain {d.label}", accent, [cv, letter]))
    return groups


PACKAGE = dict(
    kind="docs",
    title="Template CV ATS & Surat Lamaran Kerja",
    short="Template CV ATS + Surat Lamaran",
    folder="Template-CV-ATS-dan-Surat-Lamaran",
    version="1.0",
    badge="5 DESAIN · CV + SURAT LAMARAN",
    headline=["Template CV ATS", "& Surat Lamaran", "Siap Kirim"],
    tagline="Format Word, tinggal ganti isi, lolos sistem ATS.",
    chips=["Word · Google Docs · WPS", "Contoh isi lengkap"],
    features=[
        "5 desain CV + 5 surat lamaran serasi",
        "Ramah ATS: teks asli, tanpa text box",
        "Format Word (.docx) + PDF, ukuran A4",
        "Contoh isi 5 profesi + fresh graduate",
    ],
    docs={
        "CARA-PAKAI.txt": """
TEMPLATE CV ATS & SURAT LAMARAN KERJA
=====================================

Isi paket (5 folder desain):
  1. ATS Klasik          - paling aman untuk sistem ATS perusahaan besar/BUMN
  2. Modern Dua Kolom    - kolom samping berwarna untuk kontak & keahlian
  3. Minimalis           - bersih, cocok untuk desain, kreatif, startup
  4. Profesional Elegan  - untuk posisi senior / manajerial
  5. Fresh Graduate      - ada kotak foto, pendidikan & organisasi di depan
Tiap folder: CV_<desain>.docx, Surat-Lamaran_<desain>.docx, dan versi PDF.

CARA MENGEDIT
1. Buka .docx di Microsoft Word, Google Docs (File > Open > Upload),
   atau WPS Office.
2. Ganti teks contoh dengan datamu. Hapus bagian yang tidak perlu.
3. Tambah poin pengalaman: taruh kursor di akhir poin, tekan Enter.
4. Tambah pengalaman kerja: blok satu pengalaman (judul sampai poin
   terakhir), Copy, lalu Paste di bawahnya.
5. Foto (desain Fresh Graduate): klik di kotak FOTO, hapus teksnya,
   lalu Insert > Pictures. Atur ukuran foto 3x4 cm.
6. Simpan sebagai PDF sebelum dikirim: File > Save As > PDF.

TIPS AGAR LOLOS ATS & HRD
- Pakai kata kunci dari iklan lowongan (nama software, keahlian).
- Tulis pencapaian dengan angka: "menaikkan penjualan 20%",
  bukan "bertanggung jawab atas penjualan".
- Maksimal 1-2 halaman. Urutkan pengalaman dari yang terbaru.
- Nama file: CV_NamaLengkap_Posisi.pdf
- Untuk ATS paling ketat, pilih desain ATS Klasik.

FONT
Calibri, Cambria, dan Arial (bawaan Windows/Office). Tidak perlu instal font.

Ada kendala? Hubungi penjual lewat chat toko.
""",
        "LISENSI.txt": """
LISENSI PENGGUNAAN

BOLEH
- Dipakai untuk melamar kerja, magang, beasiswa, dll. (pribadi).
- Diedit dan diubah sesuka hati, dipakai berkali-kali.
- Membantu teman/keluarga membuat CV dari template ini (bukan dijual).

TIDAK BOLEH
- Menjual ulang atau membagikan file template ini sebagai template.
- Memakai template ini untuk jasa pembuatan CV berbayar.
""",
    },
    description="""
# Template CV ATS & Surat Lamaran Kerja (5 Desain, Word)

**Judul produk (Shopee):**
Template CV ATS Friendly + Surat Lamaran Kerja Word 5 Desain Bisa Edit Fresh Graduate

**Harga saran:** Rp25.000 (coret Rp49.000) · Gumroad: $3

---

CV kamu sering tidak dibalas? Bisa jadi CV-nya tidak terbaca sistem ATS. Template ini dibuat **ramah ATS**: semua teks asli (tanpa text box atau gambar tulisan), judul bagian standar, dan tata letak rapi yang tetap terbaca mesin maupun HRD.

## Isi paket
- **5 desain CV**: ATS Klasik, Modern Dua Kolom, Minimalis, Profesional Elegan, Fresh Graduate (dengan kotak foto)
- **5 surat lamaran kerja** dengan desain yang serasi
- Format **Word (.docx)** yang bisa diedit + **PDF**
- **Contoh isi lengkap** 5 profesi: akuntansi, digital marketing, UI/UX, project manager, fresh graduate IT
- Panduan cara edit + tips lolos ATS (bahasa Indonesia)

## Kelebihan
- Ukuran **A4**, muat 1 halaman
- Font bawaan Office, tampilan sama di semua laptop
- Bisa diedit di **Microsoft Word, Google Docs, WPS** (bahkan dari HP)
- Contoh kalimat pencapaian pakai angka, tinggal disesuaikan
- Cocok untuk melamar ke BUMN, perusahaan swasta, startup, magang, dan beasiswa

## Cara pembelian
1. Checkout, file dikirim otomatis (Lynk.id/Gumroad) atau lewat chat (Shopee)
2. Unduh ZIP, ekstrak, buka file .docx
3. Ganti isinya, simpan sebagai PDF, kirim lamaran!

## Catatan
- Produk digital, tidak ada barang fisik
- Untuk pemakaian pribadi, dilarang dijual ulang

**Tag:** template cv, cv ats, cv ats friendly, surat lamaran kerja, cv fresh graduate, cv word, template resume, cv kreatif, lamaran kerja
""",
)
