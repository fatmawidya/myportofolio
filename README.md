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

### 3. Endpoint Layanan Data
Menyediakan data terstruktur melalui URL:
- `/json/` & `/xml/` (dengan penerapan `use_natural_foreign_keys=True` untuk menjaga kerahasiaan ID internal database).

---

## 📂 Struktur Repositori

```text
myportofolio/
├── main/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── portofolio/
│   ├── settings.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── experience.html
│   ├── educational.html
│   └── components/
├── static/
│   ├── css/
│   └── img/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
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

# TUGAS 4

1. 

---

# AI DISCLOSURE

Pada pengerjaan Tugas 4 ini, Gemini AI hanya digunakan sebagai alat bantu (tool) untuk merapikan struktur penulisan, memformat tata bahasa, dan menyusun dokumentasi teks README yang telah disiapkan secara mandiri. Seluruh logika pemrograman, struktur kode Django, dan pengujian fitur dikerjakan secara langsung tanpa bantuan pembuatan kode otomatis oleh AI.