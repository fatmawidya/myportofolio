# MY PORTFOLIO — Fatma Widya Rachma

Website portofolio pribadi yang memuat profil, riwayat pengalaman, serta latar belakang pendidikan.

---

## 👤 Identitas

- **Nama:** Fatma Widya Rachma
- **NPM:** 2506533614
- **Program Studi:** S1 Sistem Informasi
- **Kelas:** PBP A

---

## 🛠️ Ringkasan Fitur & Halaman

### 1. Navigasi Utama & Konten
- **About Me:** Memuat informasi dasar, latar belakang, foto profil, dan status waktu login terakhir (*session*).
- **Experience:** Komponen kartu pengalaman kerja/organisasi yang dilengkapi periode, deskripsi, indikator status (*ongoing* atau *finished*), serta fitur apresiasi berupa *star*.
- **Education:** Rekam jejak jenjang pendidikan formal yang menampilkan institusi, jurusan, dan status keaktifan.

### 2. Autentikasi & Otorisasi Pengguna (RBAC)
Menerapkan 4 tingkatan hak akses berbasis peran:
- **Pengunjung (Guest):** Hanya dapat membaca konten dan endpoint API.
- **Pengguna Terdaftar:** Dapat membaca konten dan memberikan *toggle star* pada Experience.
- **Editor:** Memiliki akses pembaca, *toggle star*, serta pengubahan (*edit*) data Experience dan Education.
- **Superuser (Pemilik):** Memiliki kontrol penuh atas seluruh tindakan *Create, Read, Update,* dan *Delete* (CRUD).

### 3. Interaktivitas AJAX & Keamanan (Tugas 5)
- **Data Loading via AJAX:** Halaman Experience dan Education memuat data secara asinkron menggunakan Fetch API (`get_experience_json` & `get_education_json`).
- **Pencarian Real-Time (Debouncing):** Fitur pencarian interaktif tanpa *reload* halaman menggunakan teknik *debouncing* (300ms).
- **AJAX Form Modal:** Penambahan data dilakukan via Modal Popover tanpa *reload* dengan validasi respon HTTP (201, 400, 403).
- **Proteksi XSS:** Penerapan sanitasi *server-side* (`strip_tags`) di `ModelForm` dan *client-side escaping* (`escapeHtml`) pada perakitan DOM JavaScript.

---

## 📂 Struktur Repositori

```text
myportofolio/
├── main/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── portofolio/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── static/
│   ├── css/
│   │   └── style.css
│   ├── img/
│   │   └── fatma.jpeg
│   └── js/
│       └── toast.js
├── templates/
│   ├── components/
│   │   ├── edit_education.html
│   │   ├── edit_experience.html
│   │   ├── education_delete_modal.html
│   │   ├── education_form_modal.html
│   │   ├── experience_delete_modal.html
│   │   ├── experience_form_modal.html
│   │   ├── experience_star.html
│   │   └── toast.html
│   ├── base.html
│   ├── create_education.html
│   ├── create_experience.html
│   ├── educational.html
│   ├── experience.html
│   ├── index.html
│   ├── login.html
│   └── register.html
├── .env
├── .env.prod
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```

---

## 🛠️ Langkah Menjalankan Proyek Lokal

### 1. Clone repositori:

```bash
git clone <URL_REPOSITORY_KAMU>
cd myportofolio
```

### 2. Buat dan aktifkan virtual environment:

#### Windows:
```cmd
python -m venv env
env\Scripts\activate
```

#### macOS / Linux:
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install paket dependensi:

```bash
pip install -r requirements.txt
```

### 4. Jalankan migrasi database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Jalankan server pengembangan:

```bash
python manage.py runserver
```

Akses aplikasi melalui peramban di `http://127.0.0.1:8000/`.

---

## 🌐 Live Website

Aplikasi portofolio ini telah di-deploy dan dapat diakses secara langsung melalui tautan berikut:  
👉 [Fatma's Portfolio Web](https://fatma-widya-myportofolio.pws.cs.ui.ac.id/)

---

### Tugas 5

1. **Jelaskan apa itu debouncing dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!**  
   *Jawaban:*  
   Debouncing adalah teknik optimasi yang menunda eksekusi suatu fungsi hingga durasi waktu tertentu (misalnya 300ms) berlalu tanpa adanya pemicuan (*event*) baru dari pengguna.  
   Pada fitur pencarian berbasis AJAX, debouncing sangat penting karena tanpa teknik ini, setiap kali pengguna mengetik satu karakter di kolom pencarian, browser akan langsung mengirimkan HTTP request ke server. Jika pengguna mengetik kata yang panjang secara cepat, puluhan request akan terkirim secara berurutan. Hal ini menyebabkan lonjakan beban server, pemborosan bandwidth, serta risiko *race condition* (di mana respon dari request lama tiba belakangan dan menimpa data terbaru). Dengan debouncing, request AJAX hanya terkirim satu kali setelah pengguna berhenti mengetik sejenak.

2. **Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?**  
   *Jawaban:*  
   Fungsi `await` adalah menunda eksekusi baris kode berikutnya di dalam `async function` sampai proses asinkron dari `fetch()` selesai (*resolved*) dan mengembalikan objek `Response` atau data JSON yang siap digunakan.  
   Jika tidak menggunakan `await`, eksekusi kode JavaScript akan terus berjalan secara sinkron tanpa menunggu respon dari server. Variabel penampung hanya akan berisi objek `Promise <pending>`, bukan data asli dari server. Ketika kode berikutnya mencoba membaca data tersebut (seperti melakukan `.json()` atau mengiterasi array data), akan terjadi *runtime error* (misalnya `TypeError: Cannot read properties of undefined`).

3. **Jelaskan apa itu serangan XSS (Cross-Site Scripting) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui template Django!**  
   *Jawaban:*  
   XSS (Cross-Site Scripting) adalah celah keamanan web di mana penyerang berhasil menyisipkan skrip berbahaya (seperti kode JavaScript atau atribut HTML `onerror`) ke dalam basis data aplikasi, yang kemudian dieksekusi oleh peramban pengguna lain saat mengakses halaman web tersebut.  
   Data yang ditampilkan melalui AJAX/JavaScript lebih rentan karena saat kita menyisipkan data hasil Fetch API ke dalam DOM menggunakan JavaScript (seperti melalui `innerHTML` atau *template literals*), browser menafsirkan string tersebut secara langsung sebagai elemen HTML tanpa sanitasi otomatis. Sebaliknya, mesin template bawaan Django (`{{ variable }}`) secara otomatis menerapkan *auto-escaping* pada karakter-karakter khusus HTML (`<`, `>`, `"`, `'`, `&`), sehingga skrip jahat secara otomatis dikonversi menjadi teks biasa yang aman.

---

## 🤖 AI Disclosure

Pada pengerjaan Tugas 5 ini, Gemini AI digunakan sebagai alat bantu (*tool*) untuk:
1. Membantu melakukan pengujian (*debugging*) alur AJAX POST, penanganan status HTTP (201, 400, 403), dan validasi token CSRF.
2. Membimbing struktur penulisan fungsi sanitasi XSS (`escapeHtml` di frontend dan `strip_tags` di backend).
3. Merapikan format tata bahasa serta menyusun dokumentasi README dan jawaban pertanyaan reflektif Tugas 5 secara terstruktur.

Seluruh logika utama Django, struktur berkas HTML/CSS, konfigurasi endpoint API, dan eksekusi pengujian fitur dikerjakan dan diverifikasi secara mandiri.