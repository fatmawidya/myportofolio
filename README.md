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
- **About Me:** Profil, foto, NPM, program studi, dan waktu login terakhir.
- **Experience:** Pengalaman kerja/organisasi dalam accordion, dengan kategori, periode, status, deskripsi, dan star.
- **Education:** Timeline pendidikan dengan institusi, jenjang, jurusan, periode, status, dan star.

### 2. Autentikasi & Otorisasi Pengguna (RBAC)
Experience menjadi model padanan Tutorial 7, sedangkan Education menerapkan Tugas 6. Keduanya mempertahankan hak Editor dari proyek sebelumnya: boleh PUT/PATCH, tetapi tidak boleh membuat atau menghapus data.

| Peran | Baca/cari keduanya | Star/unstar keduanya | Edit Experience | Edit Education | Tambah/hapus keduanya |
|---|---|---|---|---|---|
| Guest | Ya | Tidak | Tidak | Tidak | Tidak |
| Pengguna terdaftar | Ya | Ya | Tidak | Tidak | Tidak |
| Editor (Group `Editor`) | Ya | Ya | Ya | Ya | Tidak |
| Superuser (pemilik) | Ya | Ya | Ya | Ya | Ya |

Izin diperiksa di server dan diterapkan pula pada halaman/form lama. Status staff saja tidak memberikan hak kelola API.

### 3. Django REST Framework, AJAX & Keamanan
- **API versi 1:** Halaman memakai `/api/v1/experience/` dan `/api/v1/education/`, dengan query pencarian `?search=...`.
- **Daftar/detail:** GET pada URL daftar atau `<uuid>/`; JSON memakai field langsung, termasuk `id`, `star_count`, dan `is_starred`.
- **Tambah/edit/hapus:** POST ke daftar, PATCH dari halaman edit ke detail, dan DELETE ke detail, tanpa reload saat submit. Detail juga mendukung PUT.
- **Star:** POST ke `<uuid>/star/`, selalu memakai akun dari session login.
- **Interaktivitas:** Debounce 300 ms, AbortController, modal, toast, dan state loading/kosong/error.
- **Validasi:** ModelSerializer dengan field eksplisit, sanitasi `strip_tags`, validasi periode, serta informasi star read-only. Frontend tetap melakukan escaping.
- **Session dan CSRF:** SessionAuthentication dan header `X-CSRFToken` pada operasi tulis. Endpoint JSON/XML lama dipertahankan untuk kompatibilitas, tetapi halaman utama memakai API DRF.

---

## 📂 Struktur Repositori

```text
myportofolio/
├── main/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── api_urls.py
│   ├── api_views.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── tests_api.py
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
│   ├── css/style.css
│   ├── img/fatma.jpeg
│   └── js/toast.js
├── templates/
│   ├── components/
│   │   ├── education_delete_model.html
│   │   ├── education_form_modal.html
│   │   ├── experience_delete_model.html
│   │   ├── experience_form_modal.html
│   │   ├── experience_star.html
│   │   └── toast.html
│   ├── base.html
│   ├── education_form.html
│   ├── educational.html
│   ├── experience.html
│   ├── experience_form.html
│   ├── index.html
│   ├── login.html
│   └── register.html
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

`env/`, `.env`, database SQLite, dan cadangan `tmp/` merupakan berkas lokal yang tidak dimasukkan ke Git. Satu full-page form per model digunakan bersama untuk tambah dan edit.

---

## 🛠️ Langkah Menjalankan Proyek Lokal

### 1. Clone repositori

```bash
git clone https://github.com/fatmawidya/myportofolio.git
cd myportofolio
```

### 2. Buat dan aktifkan virtual environment

Windows (Command Prompt):

```cmd
python -m venv env
env\Scripts\activate
```

Windows (PowerShell):

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependency

```bash
python -m pip install -r requirements.txt
```

Secara default proyek memakai SQLite lokal (`PRODUCTION=False`). Jika `.env` sudah ada, pertahankan konfigurasi lokal yang digunakan.

### 4. Terapkan migrasi dan buat pemilik portofolio

```bash
python manage.py migrate
python manage.py createsuperuser
```

Database baru belum berisi data. Login sebagai superuser untuk menambah Experience dan Education. `makemigrations` hanya diperlukan ketika mengubah model, bukan pada setup biasa.

### 5. Buat akun biasa dan Editor

Buat akun melalui `/register/`. Untuk Editor, login sebagai superuser di `/admin/`, buat Group dengan nama persis `Editor`, kemudian tambahkan akun yang dipilih ke grup tersebut. Editor dapat mengedit Experience dan Education, tetapi tidak dapat membuat atau menghapus data.

### 6. Jalankan pemeriksaan dan server

```bash
python manage.py check
python manage.py test main
python manage.py runserver
```

Buka `http://127.0.0.1:8000/`. Untuk menjalankan tes API saja, gunakan `python manage.py test main.tests_api`.

---

## 🌐 Live Website

[Fatma's Portfolio Web](https://fatma-widya-myportofolio.pws.cs.ui.ac.id/)

Gunakan konfigurasi database PWS yang sudah ada: `PRODUCTION=True`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, dan `SCHEMA`. Environment lokal dan database PWS terpisah; akun dan data lokal tidak otomatis tersedia di PWS.

Deployment perlu meng-install `requirements.txt`, menerapkan migrasi termasuk `0006_education_starred_by`, dan menjalankan `collectstatic --noinput`. Setelah deploy, cek baca data, login, dan operasi tulis sesuai peran pada kedua halaman melalui HTTPS.

---

### Tugas 6



1. **Apa itu REST, mengapa JSON saja tidak cukup, dan apa perbedaan PUT/PATCH?**

   REST adalah gaya arsitektur yang memperlakukan data sebagai resource, memberi alamat resource yang jelas, menggunakan antarmuka HTTP secara konsisten, serta mempertukarkan representasi. JSON hanyalah format representasi; endpoint JSON dengan semua aksi memakai GET belum mengikuti semantik REST. PUT digunakan untuk mengganti representasi field yang dapat ditulis secara lengkap, misalnya mengganti seluruh detail Education. PATCH memperbarui sebagian field, misalnya hanya `description`, sambil mempertahankan field lain. Di API ini PUT mewajibkan field wajib, sedangkan PATCH memakai `partial=True`. SessionAuthentication menyimpan session di server, sehingga implementasi ini merupakan pilihan praktis untuk web AJAX dan tidak sepenuhnya stateless seperti REST ideal.


2. **Apa peran serializer DRF dan keuntungannya dibanding dictionary JsonResponse?**

   Serializer menerjemahkan model menjadi representasi yang bisa dirender sebagai JSON serta memvalidasi input sebelum create/update. ModelSerializer menyediakan konversi tipe, validasi field, error terstruktur, dan penyimpanan model. Dibanding merakit dictionary secara manual, daftar field, validasi, dan field hasil perhitungan dapat dipakai ulang pada daftar/detail/tambah/edit. Di sini field ditulis eksplisit; `star_count` dan `is_starred` read-only, teks dibersihkan dengan `strip_tags`, dan validasi tanggal memperhitungkan nilai lama saat PATCH. Serializer tidak menggantikan permission atau escaping frontend.


3. **Apa perbedaan autentikasi dan otorisasi, serta mengapa permission wajib di server?**

   Autentikasi menentukan siapa pengirim request: SessionAuthentication membaca session login. Otorisasi menentukan apakah akun tersebut boleh menjalankan aksi: permission mengizinkan publik membaca, akun login memberi star, Editor mengedit Experience dan Education, sedangkan superuser juga dapat membuat dan menghapus data. Menyembunyikan tombol hanya membantu tampilan; pengguna tetap bisa mengirim request melalui Console atau klien HTTP. Permission di server menolak request tersebut sebelum database diubah. Endpoint star memakai IsAuthenticated dan selalu memilih `request.user`, bukan ID akun dari payload.


4. **Mengapa SessionAuthentication tetap memerlukan CSRF dan mengapa force_authenticate tidak cukup?**

   Browser otomatis menyertakan cookie session sehingga situs lain dapat mencoba memicu request atas nama akun yang sedang login. Request perubahan data harus menyertakan token CSRF yang diperiksa server; frontend mengirim header `X-CSRFToken` pada POST/PATCH/DELETE. Halaman daftar memakai `ensure_csrf_cookie` agar akun biasa dan Editor juga mendapat cookie token. `force_authenticate` memasukkan identitas langsung dan melewati autentikasi session sehingga tidak membuktikan CSRF bekerja. Tes memakai `APIClient(enforce_csrf_checks=True)` dengan `.login()` sungguhan: POST tanpa token ditolak 403 tanpa perubahan database, lalu POST dengan token berhasil 201.


Referensi teknis: [DRF serializers](https://www.django-rest-framework.org/api-guide/serializers/), [SessionAuthentication](https://www.django-rest-framework.org/api-guide/authentication/#sessionauthentication), dan [DRF testing](https://www.django-rest-framework.org/api-guide/testing/).

---

## 🤖 AI Disclosure

Pada pengerjaan Tutorial 7 dan Tugas 6, saya menggunakan ChatGPT sebagai alat bantu selama proses belajar dan pengembangan proyek. Ketika ada bagian yang belum saya pahami, saya meminta penjelasan atau arahan agar dapat memahami langkah pengerjaannya. Saya juga menggunakan ChatGPT untuk membantu memeriksa kode dan mencari penyebab kesalahan.

Bantuan yang saya gunakan meliputi:
1. Membantu memahami feedback tugas sebelumnya dan mencocokkan implementasi dengan ketentuan tutorial serta tugas.
2. Memberikan penjelasan dan saran perbaikan terkait serializer, permission, endpoint Django REST Framework, relasi star Education, serta migrasi.
3. Membantu memahami dan memperbaiki penggunaan fetch untuk menghubungkan halaman Experience dan Education dengan API, termasuk fitur pencarian, tambah, edit, hapus, star, validasi, dan CSRF.
4. Membantu menyusun pengujian serta meninjau hasilnya untuk memeriksa kesesuaian fitur dengan ketentuan tugas.
5. Membantu merapikan draf jawaban reflektif, template form, dan pengelompokan perubahan sebelum commit. Commit dan push saya lakukan sendiri.

### Strategi prompting dan ringkasan interaksi

Saya memulai dengan meminta ChatGPT meninjau dokumen, feedback, dan kode proyek yang sudah ada. Jika ada ketentuan atau bagian implementasi yang belum saya pahami, saya meminta arahan lebih lanjut. Saya kemudian memperjelas permintaan agar saran yang diberikan tetap mengikuti pola tutorial dan sesuai dengan model, field, serta tampilan portofolio saya.

Beberapa arahan yang saya berikan dalam percakapan adalah:

- “Aku masih belum paham perbedaan serializer dan view. Bisa bantu jelaskan?”
- “Bagaimana cara memeriksa apakah permission yang aku buat sudah sesuai ketentuan tugas?”
- “Fetch yang aku buat masih error. Bisa bantu arahkan bagian mana yang perlu aku periksa?”

Interaksi dilakukan secara bertahap sesuai kebutuhan, mulai dari konfigurasi, backend API, integrasi halaman, hingga dokumentasi. Saya menggunakan jawaban AI sebagai bahan pertimbangan dan meminta penyesuaian ketika hasilnya belum sesuai dengan kebutuhan proyek atau ketentuan tutorial.

### Evaluasi bantuan AI dan keterbatasan

ChatGPT saya gunakan sebagai alat bantu ketika ada konsep atau langkah pengerjaan yang belum saya pahami. Saya meminta penjelasan, arahan untuk memeriksa kesalahan, serta bantuan meninjau dan memperbaiki kode. Saran yang diberikan tetap perlu dicocokkan dengan materi tutorial dan kebutuhan proyek karena tidak selalu langsung sesuai.

Dalam pengujian, ChatGPT membantu memberikan arahan mengenai bagian yang perlu diperiksa dan membantu meninjau hasilnya. Hasil pengujian tersebut menjadi bahan evaluasi, tetapi belum menjamin seluruh fitur berjalan dengan benar pada server PWS yang sebenarnya.

Melalui proses ini, saya belajar untuk lebih jelas menyampaikan pertanyaan dan menilai kesesuaian jawaban AI. Saya tetap perlu memahami kode dan memeriksa kembali saran sebelum menggunakannya. Keputusan penggunaan saran dan tanggung jawab atas hasil akhir tetap berada pada saya.