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

## 🤖 AI Disclosure

Pada revisi perbaikan feedback Tugas 1–3 ini, ChatGPT digunakan sebagai alat bantu untuk:

1. Meninjau feedback tentang deskripsi proyek, instruksi setup, alur data JSON, dan penempatan template.
2. Membantu menyatukan halaman tambah/edit menjadi satu template per model dan memperbaiki format tanggal pada input edit.
3. Membantu menyesuaikan tes lama dengan pemuatan data AJAX serta meninjau tombol Delete agar sesuai izin superuser.
4. Membantu merapikan dokumentasi dan menyiapkan urutan pengerjaan berikutnya.

Bantuan AI mencakup perubahan kode dan pengujian otomatis. Pengujian lokal tidak menggantikan pemeriksaan manual tampilan maupun deployment PWS oleh pemilik. Jawaban Tugas 6 akan ditambahkan pada tahap dokumentasi tugas tersebut.
