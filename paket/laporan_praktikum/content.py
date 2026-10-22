"""Isi contoh laporan praktikum. Data percobaan adalah contoh yang wajar,
bukan hasil pengukuran sungguhan; pembeli mengganti dengan datanya sendiri."""

COMMON = dict(
    univ="UNIVERSITAS NAMA KAMPUS",
    fakultas="FAKULTAS MATEMATIKA DAN ILMU PENGETAHUAN ALAM",
    tahun="2026",
    nama="Nama Lengkap Praktikan",
    nim="2201234567",
    kelompok="Kelompok 2 / Kelas A",
    asisten="Nama Asisten Praktikum",
    dosen="Dr. Nama Dosen, M.Si.",
    kota="Kota",
    tanggal="22 Oktober 2026",
)

KIMIA = dict(
    COMMON,
    key="kimia", label="Kimia",
    mk="Kimia Analitik Dasar",
    no="III",
    judul="Penentuan Kadar Asam Asetat dalam Cuka Makan dengan Titrasi Asam-Basa",
    prodi="PROGRAM STUDI KIMIA",
    lab="LABORATORIUM KIMIA ANALITIK",
    latar=[
        "Cuka makan adalah larutan asam asetat (CH₃COOH) yang banyak dipakai sebagai bumbu "
        "dan pengawet makanan. SNI 01-3711-1995 mensyaratkan kadar asam asetat cuka makan "
        "minimal 4%. Karena itu, kadar asam asetat perlu diuji agar produk aman dan sesuai "
        "label.",
        "Titrasi asam-basa adalah cara sederhana dan teliti untuk menentukan kadar asam. "
        "Dalam percobaan ini, asam asetat dalam sampel cuka dititrasi dengan larutan baku "
        "NaOH 0,1 M menggunakan indikator fenolftalein.",
    ],
    tujuan=["Menstandarisasi larutan NaOH dengan larutan baku primer asam oksalat.",
            "Menentukan kadar asam asetat dalam sampel cuka makan dengan titrasi asam-basa."],
    teori=[
        ("Titrasi Asam-Basa",
         ["Titrasi asam-basa adalah analisis volumetri yang didasarkan pada reaksi "
          "netralisasi antara asam dan basa. Titik ekuivalen tercapai ketika jumlah mol asam "
          "sama dengan jumlah mol basa (Day & Underwood, 2002).",
          "Reaksi yang terjadi: CH₃COOH(aq) + NaOH(aq) → CH₃COONa(aq) + H₂O(l)."]),
        ("Indikator Fenolftalein",
         ["Fenolftalein tidak berwarna dalam suasana asam dan berubah menjadi merah muda pada "
          "rentang pH 8,2–10,0. Indikator ini cocok untuk titrasi asam lemah dengan basa kuat "
          "karena titik ekuivalennya berada pada pH basa."]),
    ],
    alat=[("Buret 50 mL", "1 buah"), ("Erlenmeyer 250 mL", "3 buah"),
          ("Pipet volume 10 mL", "1 buah"), ("Labu ukur 100 mL", "1 buah"),
          ("Statif dan klem", "1 set"), ("Gelas kimia 100 mL", "2 buah")],
    bahan=[("Larutan NaOH", "± 0,1 M"), ("Asam oksalat dihidrat", "0,1 M"),
           ("Cuka makan (sampel)", "10 mL"), ("Indikator fenolftalein", "3 tetes/titrasi"),
           ("Akuades", "secukupnya")],
    prosedur=["Pipet 10 mL sampel cuka, masukkan ke labu ukur 100 mL, encerkan dengan akuades "
              "sampai tanda batas, lalu kocok hingga homogen.",
              "Pipet 10 mL larutan encer tersebut ke dalam erlenmeyer dan tambahkan 3 tetes "
              "indikator fenolftalein.",
              "Titrasi dengan larutan NaOH dari buret sampai muncul warna merah muda yang "
              "stabil selama 30 detik.",
              "Catat volume NaOH yang terpakai. Ulangi titrasi sebanyak tiga kali."],
    data_title="Data titrasi sampel cuka dengan NaOH 0,1002 M",
    data=[["Titrasi ke-", "V awal (mL)", "V akhir (mL)", "V NaOH (mL)"],
          ["1", "0,00", "7,10", "7,10"], ["2", "7,10", "14,15", "7,05"],
          ["3", "14,15", "21,30", "7,15"], ["Rata-rata", "", "", "7,10"]],
    hitung=["mol NaOH = M × V = 0,1002 M × 7,10 mL = 0,7114 mmol",
            "mol CH₃COOH dalam 10 mL larutan encer = 0,7114 mmol",
            "Faktor pengenceran = 100/10 = 10 → mol dalam 10 mL cuka = 7,114 mmol",
            "Massa CH₃COOH = 7,114 mmol × 60,05 mg/mmol = 427,2 mg",
            "Kadar = 427,2 mg / 10 mL × 100% = 4,27% (b/v)"],
    bahas=[
        "Hasil titrasi menunjukkan kadar asam asetat sampel sebesar 4,27% (b/v). Nilai ini "
        "memenuhi syarat SNI (minimal 4%) dan mendekati kadar pada label kemasan (4,5%).",
        "Selisih kecil dengan label dapat disebabkan oleh kesalahan membaca meniskus buret, "
        "penentuan titik akhir yang sedikit terlambat, atau penguapan asam asetat saat "
        "sampel disimpan terbuka.",
        "Ketiga data titrasi memiliki selisih kurang dari 0,1 mL sehingga presisi percobaan "
        "dinilai baik.",
    ],
    figure="Perubahan warna larutan pada titik akhir titrasi",
    simpulan=["Konsentrasi larutan NaOH hasil standarisasi adalah 0,1002 M.",
              "Kadar asam asetat dalam sampel cuka makan adalah 4,27% (b/v) dan memenuhi SNI."],
    saran=["Gunakan latar putih di bawah erlenmeyer agar perubahan warna lebih mudah diamati.",
           "Simpan sampel dalam wadah tertutup untuk mencegah penguapan."],
    pustaka=["Badan Standardisasi Nasional. (1995). SNI 01-3711-1995 Cuka makan. Jakarta: BSN.",
             "Day, R. A., & Underwood, A. L. (2002). Analisis kimia kuantitatif (Edisi ke-6). "
             "Jakarta: Erlangga.",
             "Harris, D. C. (2016). Quantitative chemical analysis (9th ed.). New York: "
             "W. H. Freeman."],
)

BIOLOGI = dict(
    COMMON,
    key="biologi", label="Biologi",
    mk="Biologi Sel",
    no="II",
    judul="Pengamatan Struktur Sel Tumbuhan dan Sel Hewan menggunakan Mikroskop Cahaya",
    prodi="PROGRAM STUDI BIOLOGI",
    lab="LABORATORIUM BIOLOGI DASAR",
    latar=[
        "Sel adalah unit struktural dan fungsional terkecil makhluk hidup. Walaupun sel "
        "tumbuhan dan sel hewan sama-sama eukariotik, keduanya memiliki perbedaan struktur "
        "yang khas, seperti dinding sel, plastida, dan vakuola.",
        "Mikroskop cahaya memungkinkan pengamatan bagian-bagian sel tersebut. Praktikum ini "
        "membandingkan sel epidermis bawang merah dengan sel epitel pipi manusia.",
    ],
    tujuan=["Mengamati struktur sel tumbuhan pada epidermis bawang merah.",
            "Mengamati struktur sel hewan pada epitel rongga pipi.",
            "Membandingkan ciri sel tumbuhan dan sel hewan."],
    teori=[
        ("Sel Tumbuhan",
         ["Sel tumbuhan memiliki dinding sel dari selulosa yang membuat bentuknya tetap, "
          "vakuola sentral yang besar, dan plastida (Campbell et al., 2017)."]),
        ("Sel Hewan",
         ["Sel hewan tidak memiliki dinding sel sehingga bentuknya lebih bervariasi. Sel "
          "hewan memiliki sentriol dan vakuola berukuran kecil atau tidak ada."]),
    ],
    alat=[("Mikroskop cahaya", "1 unit"), ("Kaca objek & kaca penutup", "4 pasang"),
          ("Pipet tetes", "2 buah"), ("Silet / cutter", "1 buah"), ("Tusuk gigi steril", "2 buah")],
    bahan=[("Umbi bawang merah", "1 siung"), ("Larutan metilen biru 1%", "secukupnya"),
           ("Larutan iodin", "secukupnya"), ("Akuades", "secukupnya")],
    prosedur=["Kupas lapisan tipis epidermis bawang merah dan letakkan di kaca objek.",
              "Tetesi larutan iodin, tutup dengan kaca penutup, lalu amati dengan perbesaran "
              "10× dan 40×.",
              "Kerok pelan bagian dalam pipi dengan tusuk gigi steril, oleskan ke kaca objek.",
              "Tetesi metilen biru, tutup dengan kaca penutup, lalu amati.",
              "Gambar dan beri keterangan bagian sel yang terlihat."],
    data_title="Hasil pengamatan sel",
    data=[["Preparat", "Perbesaran", "Bentuk sel", "Bagian yang terlihat"],
          ["Epidermis bawang merah", "400×", "Persegi panjang, teratur",
           "Dinding sel, sitoplasma, inti"],
          ["Epitel pipi", "400×", "Bulat pipih, tidak teratur",
           "Membran sel, sitoplasma, inti"]],
    hitung=None,
    bahas=[
        "Sel epidermis bawang merah tampak tersusun rapat dan berbentuk persegi panjang "
        "karena memiliki dinding sel. Inti sel terlihat jelas setelah ditetesi iodin.",
        "Sel epitel pipi tampak terpisah-pisah dengan bentuk tidak beraturan. Pewarnaan "
        "metilen biru membuat inti sel lebih kontras terhadap sitoplasma.",
        "Kloroplas tidak teramati pada bawang merah karena umbi tidak melakukan fotosintesis.",
    ],
    figure="Sel epidermis bawang merah, perbesaran 400×",
    simpulan=["Sel tumbuhan berbentuk tetap karena memiliki dinding sel.",
              "Sel hewan tidak memiliki dinding sel sehingga bentuknya tidak beraturan.",
              "Inti sel terlihat pada kedua jenis sel setelah diwarnai."],
    saran=["Ambil lapisan epidermis setipis mungkin agar sel tidak bertumpuk.",
           "Atur diafragma mikroskop untuk mendapatkan kontras terbaik."],
    pustaka=["Campbell, N. A., Urry, L. A., Cain, M. L., et al. (2017). Biology (11th ed.). "
             "New York: Pearson.",
             "Karp, G. (2013). Cell and molecular biology (7th ed.). Hoboken: Wiley."],
)

FISIKA = dict(
    COMMON,
    key="fisika", label="Fisika",
    mk="Fisika Dasar I",
    no="IV",
    judul="Penentuan Percepatan Gravitasi Bumi dengan Bandul Matematis",
    prodi="PROGRAM STUDI FISIKA",
    lab="LABORATORIUM FISIKA DASAR",
    latar=[
        "Percepatan gravitasi (g) adalah besaran penting dalam fisika. Nilainya bervariasi "
        "sedikit tergantung lintang dan ketinggian tempat, dengan nilai standar 9,80665 m/s².",
        "Bandul matematis menyediakan cara sederhana untuk mengukur g, karena periode "
        "ayunannya hanya bergantung pada panjang tali dan percepatan gravitasi.",
    ],
    tujuan=["Menentukan hubungan antara panjang tali dan periode bandul.",
            "Menentukan nilai percepatan gravitasi di laboratorium."],
    teori=[
        ("Bandul Matematis",
         ["Untuk simpangan kecil (< 10°), periode bandul memenuhi T = 2π√(L/g), sehingga "
          "g = 4π²L/T² (Halliday et al., 2014)."]),
    ],
    alat=[("Statif dan penjepit", "1 set"), ("Beban bandul 50 g", "1 buah"),
          ("Tali / benang", "1,5 m"), ("Mistar 100 cm", "1 buah"), ("Stopwatch", "1 buah"),
          ("Busur derajat", "1 buah")],
    bahan=[],
    prosedur=["Gantung beban pada tali dengan panjang 30 cm dari titik gantung ke pusat beban.",
              "Simpangkan bandul sekitar 5° lalu lepaskan tanpa dorongan.",
              "Ukur waktu untuk 10 ayunan penuh dengan stopwatch.",
              "Ulangi untuk panjang tali 40, 50, 60, dan 70 cm."],
    data_title="Data waktu 10 ayunan untuk berbagai panjang tali",
    data=[["L (m)", "t 10 ayunan (s)", "T (s)", "T² (s²)", "g (m/s²)"],
          ["0,30", "11,02", "1,102", "1,214", "9,75"], ["0,40", "12,70", "1,270", "1,613", "9,79"],
          ["0,50", "14,18", "1,418", "2,011", "9,82"], ["0,60", "15,56", "1,556", "2,421", "9,78"],
          ["0,70", "16,79", "1,679", "2,819", "9,80"], ["Rata-rata", "", "", "", "9,79"]],
    hitung=["Contoh untuk L = 0,50 m: T = 14,18 s / 10 = 1,418 s",
            "g = 4π²L / T² = 4 × (3,1416)² × 0,50 / (1,418)² = 9,82 m/s²",
            "Ralat relatif terhadap nilai standar = |9,79 − 9,81| / 9,81 × 100% = 0,2%"],
    bahas=[
        "Nilai rata-rata g yang diperoleh adalah 9,79 m/s², dengan ralat relatif 0,2% "
        "terhadap nilai standar. Hasil ini menunjukkan metode bandul cukup akurat.",
        "Grafik T² terhadap L berbentuk garis lurus, sesuai persamaan T² = (4π²/g)L.",
        "Sumber kesalahan utama adalah reaksi saat menekan stopwatch dan simpangan awal "
        "yang tidak selalu sama.",
    ],
    figure="Grafik hubungan T² terhadap panjang tali L",
    simpulan=["Periode bandul bertambah seiring bertambahnya panjang tali (T² ∝ L).",
              "Percepatan gravitasi di laboratorium adalah 9,79 m/s²."],
    saran=["Ukur waktu 20 ayunan untuk mengurangi pengaruh waktu reaksi.",
           "Gunakan sensor gerbang cahaya bila tersedia."],
    pustaka=["Halliday, D., Resnick, R., & Walker, J. (2014). Fundamentals of physics "
             "(10th ed.). Hoboken: Wiley.",
             "Giancoli, D. C. (2014). Physics: Principles with applications (7th ed.). "
             "Boston: Pearson."],
)

INFORMATIKA = dict(
    COMMON,
    key="informatika", label="Informatika",
    mk="Struktur Data",
    no="V",
    judul="Implementasi Stack dan Queue menggunakan Bahasa Python",
    prodi="PROGRAM STUDI INFORMATIKA",
    fakultas="FAKULTAS TEKNIK",
    lab="LABORATORIUM PEMROGRAMAN",
    latar=[
        "Stack dan queue adalah struktur data linear yang paling sering dipakai, misalnya "
        "untuk fitur undo pada editor (stack) dan antrean cetak dokumen (queue).",
        "Praktikum ini mengimplementasikan kedua struktur data tersebut dan menguji "
        "operasinya untuk memahami prinsip LIFO dan FIFO.",
    ],
    tujuan=["Mengimplementasikan stack dengan operasi push, pop, dan peek.",
            "Mengimplementasikan queue dengan operasi enqueue dan dequeue.",
            "Menguji kebenaran program dengan beberapa kasus uji."],
    teori=[
        ("Stack",
         ["Stack bekerja dengan prinsip Last In First Out (LIFO): elemen terakhir yang masuk "
          "adalah elemen pertama yang keluar (Goodrich et al., 2013)."]),
        ("Queue",
         ["Queue bekerja dengan prinsip First In First Out (FIFO): elemen pertama yang masuk "
          "adalah elemen pertama yang keluar."]),
    ],
    alat=[("Laptop / PC", "1 unit"), ("Python 3.12", "-"), ("Visual Studio Code", "-")],
    bahan=[],
    prosedur=["Buat file stack_queue.py.",
              "Tulis kelas Stack dan Queue seperti kode di bawah.",
              "Jalankan kasus uji dan catat keluarannya."],
    code="""class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if self.items else None""",
    data_title="Hasil pengujian program",
    data=[["No", "Operasi", "Keluaran yang diharapkan", "Hasil", "Status"],
          ["1", "push 1, 2, 3 lalu pop", "3", "3", "Lulus"],
          ["2", "pop pada stack kosong", "None", "None", "Lulus"],
          ["3", "enqueue A, B, C lalu dequeue", "A", "A", "Lulus"],
          ["4", "dequeue pada queue kosong", "None", "None", "Lulus"]],
    hitung=None,
    bahas=[
        "Seluruh kasus uji lulus, sehingga implementasi stack dan queue sudah sesuai prinsip "
        "LIFO dan FIFO.",
        "Operasi pop(0) pada list Python berkompleksitas O(n). Untuk queue berukuran besar, "
        "collections.deque lebih efisien karena operasi di kedua ujungnya O(1).",
    ],
    figure="Tangkapan layar keluaran program di terminal",
    simpulan=["Stack dan queue berhasil diimplementasikan dan lulus 4 kasus uji.",
              "deque lebih tepat dipakai untuk queue yang sering diakses."],
    saran=["Tambahkan pengujian otomatis dengan modul unittest.",
           "Bandingkan waktu eksekusi list dan deque untuk data besar."],
    pustaka=["Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2013). Data structures and "
             "algorithms in Python. Hoboken: Wiley.",
             "Python Software Foundation. (2024). collections — Container datatypes. "
             "Diakses dari docs.python.org."],
)

KOSONG = dict(
    COMMON,
    key="kosong", label="Kosong (Panduan)",
    mk="[Nama Mata Kuliah]",
    no="[No]",
    judul="[Judul Percobaan]",
    prodi="PROGRAM STUDI [NAMA PRODI]",
    fakultas="FAKULTAS [NAMA FAKULTAS]",
    lab="LABORATORIUM [NAMA LABORATORIUM]",
    latar=["[Jelaskan mengapa percobaan ini penting: fenomena, manfaat, atau masalah yang "
           "ingin dijawab. 1–3 paragraf.]",
           "[Sebutkan secara singkat metode yang dipakai dalam percobaan.]"],
    tujuan=["[Tujuan pertama, diawali kata kerja: menentukan, mengamati, mengukur, ...]",
            "[Tujuan kedua]"],
    teori=[("[Subjudul Teori 1]", ["[Tuliskan konsep atau rumus yang mendasari percobaan, "
                                   "lengkap dengan sitasi (Penulis, Tahun).]"]),
           ("[Subjudul Teori 2]", ["[Teori pendukung lain.]"])],
    alat=[("[Nama alat]", "[Jumlah]"), ("[Nama alat]", "[Jumlah]"), ("[Nama alat]", "[Jumlah]")],
    bahan=[("[Nama bahan]", "[Jumlah/konsentrasi]"), ("[Nama bahan]", "[Jumlah/konsentrasi]")],
    prosedur=["[Langkah pertama]", "[Langkah kedua]", "[Langkah ketiga]"],
    data_title="[Judul tabel data pengamatan]",
    data=[["[Kolom 1]", "[Kolom 2]", "[Kolom 3]", "[Kolom 4]"],
          ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]],
    hitung=["[Tuliskan rumus, substitusi angka, dan hasil perhitungan.]"],
    bahas=["[Jelaskan arti data yang diperoleh.]",
           "[Bandingkan dengan teori atau literatur; jelaskan bila ada perbedaan.]",
           "[Sebutkan sumber kesalahan yang mungkin terjadi.]"],
    figure="[Keterangan gambar]",
    simpulan=["[Jawaban untuk tujuan pertama]", "[Jawaban untuk tujuan kedua]"],
    saran=["[Saran untuk praktikum berikutnya]"],
    pustaka=["[Penulis, A. (Tahun). Judul buku. Kota: Penerbit.]",
             "[Penulis, B. (Tahun). Judul artikel. Nama Jurnal, Volume(Nomor), halaman.]"],
)

REPORTS = [KIMIA, BIOLOGI, FISIKA, INFORMATIKA, KOSONG]
