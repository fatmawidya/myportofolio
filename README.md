Nama : Fatma Widya Rachma

NPM : 2506533614

Kelas : PBP A


### Tugas 1

1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti <section>, <article>, atau <aside>? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?
Jawab: Ya, saat merancang struktur HTML untuk website portofolio ini, saya menggunakan elemen-elemen semantik HTML5 seperti <header>, <nav>, <section>, <article>, <footer>, serta tag interaktif bawaan <details> dan <summary> pada komponen My Journey. Menurut saya, penggunaan elemen semantik ini sangat membantu dalam proses pembuatan static web karena kode yang saya tulis menjadi jauh lebih terstruktur dan rapi tanpa terjebak dalam penumpukan tag <div> yang berlebihan (div soup). Selain itu, elemen semantik mempermudah saya dalam menyusun aturan CSS di style.css agar lebih spesifik. Elemen semantik ini juga membantu screen reader dan mesin pencari dalam memahami hirarki serta peran dari setiap bagian konten di halaman web saya secara kontekstual.

2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?
Jawab: Saat mengatur CSS agar tetap responsif, tantangan tata letak utama yang saya temukan adalah menyesuaikan pergeseran struktur halaman dari tampilan desktop dua kolom (multi-column) menjadi tampilan seluler satu kolom (single-column) yang tetap simetris, terutama pada bagian Hero Section dan My Journey. Cara saya mengevaluasi elemen yang harus diubah adalah dengan memprioritaskan informasi penting, seperti Nama dan NPM, agar tetap terlihat di bagian atas layar (above the fold) ketika dibuka melalui HP. Oleh karena itu, saya mengubah tata letak CSS Grid dua kolom pada Hero Section menjadi tumpukan vertikal (stacked layout), memperkecil batas lebar foto menjadi 190px, dan memanfaatkan fungsi clamp() untuk ukuran font. Pada bagian My Journey, saya juga mengurangi nilai padding dan margin kartu melalui media queries agar seluruh isi accordion tetap muat dengan rapi di layar sempit tanpa terpotong.

3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?
Jawab: Batasan utama yang saya rasakan saat membuat website statis murni ini adalah masalah kepraktisan dalam mengelola konten. Semua informasi mengenai diri saya, riwayat pengalaman, dan kontak harus saya tulis satu per satu secara manual (hardcoded) di dalam berkas HTML. Jika suatu saat saya ingin menambahkan pengalaman baru atau sekadar mengubah isi bio, saya wajib membuka kembali VS Code dan mengedit berkas HTML tersebut secara langsung. Proses ini terasa kurang efisien jika isi portofolio terus bertambah di masa depan. Berdasarkan batasan tersebut, fungsionalitas dinamis yang paling ingin saya tambahkan pada iterasi proyek selanjutnya adalah pengintegrasian database menggunakan arsitektur Django MVT. Dengan adanya database dan fitur Django Admin, saya bisa menambah atau memperbarui data portofolio dengan lebih mudah melalui halaman pengelola (dashboard) tanpa perlu mengotak-atik kode HTML lagi. Selain itu, saya juga ingin membuat formulir kontak yang benar-benar dapat memproses pesan pengunjung dan mengirimkannya secara otomatis ke email saya.

### Pengungkapan AI (AI Disclosure)

Dalam pengerjaan Tugas Individu 1 ini, saya memanfaatkan AI (Gemini) teman belajar interaktif saya. Setiap kali menghadapi kendala teknis, kebingungan sintaks, atau mencari ide tampilan, AI membantu saya memahami konsep dasar di balik permasalahan tersebut. 

Saya tidak pernah langsung menyalin dan menempelkan (copy-paste) kode yang berikan oleh AI ke dalam proyek saya begitu saja. Setiap saran atau snippet kode yang diberikan selalu saya pelajari terlebih dahulu alur logikanya, saya uji coba secara bertahap di lingkungan lokal, dan saya sesuaikan secara manual agar pas dengan kebutuhan proyek. Banyak rekomendasi AI yang perlu saya ubah atau bahkan saya buang karena tidak sesuai dengan tema neobrutalisme yang saya usung maupun struktur Django yang saya gunakan.

Selain membantu dalam eksplorasi CSS dan pemecahan masalah error pada Git, AI juga saya gunakan sebagai alat bantu untuk merapikan tata bahasa pada jawaban refleksi di README ini. Poin-poin refleksi yang tertulis murni berasal dari pengalaman dan pemahaman nyata yang saya alami selama proses koding, lalu saya meminta bantuan AI untuk merangkai kalimatnya agar lebih runtut dan enak dibaca. Hasil dari perbaikan tata bahasa tersebut tetap saya baca ulang dan saya sesuaikan kembali agar bahasanya tetap natural dan mencerminkan sudut pandang saya sebagai mahasiswa.

Berikut adalah 5 contoh interaksi saya bersama AI selama proses pengerjaan:

1. Eksplorasi Design Neobrutalism
   * Prompt: "Gimana cara bikin tombol di CSS biar keliatan neobrutalism?"
   * Tujuan: Memahami kombinasi warna kontras, ketebalan border, dan shadow yang pas untuk tema neobrutalism.
   * Respon AI: Memberikan contoh CSS tombol dengan border hitam tebal, bayangan (box-shadow) tegas, dan border-radius: 12px.
   * Tindakan Saya: Saya mengambil konsep border dan shadow-nya, tetapi nilai border-radius saya ubah manual menjadi 3px di style.css agar sudutnya tetap tajam dan konsisten.

2. Membuat Accordion untuk Section My Journey
   * Prompt: "Bikin accordion di HTML CSS pake tag details gampang nggak?"
   * Tujuan: Membuat komponen di section My Journey yang bisa diklik (diperluas) tanpa perlu menggunakan JavaScript.
   * Respon AI: Menjelaskan penggunaan tag bawaan HTML <details> dan <summary> beserta contoh styling CSS Flexbox-nya.
   * Tindakan Saya: Saya menerapkan struktur tag tersebut di index.html lalu menyesuaikan styling CSS-nya agar selaras dengan palet warna website saya.

3. Troubleshooting Error Git saat Push ke PWS
   * Prompt: "Ini knp git push reject mulu sih pas mau push ke pws?"
   * Tujuan: Mengatasi error non-fast-forward saat mencoba melakukan push kode terbaru ke server PWS UI.
   * Respon AI: Menjelaskan bahwa riwayat commit lokal dan remote berbeda, serta memberikan opsi perintah git pull --rebase atau force push.
   * Tindakan Saya: Saya menjalankan perintah git pull pws main --rebase lalu melakukan push ulang hingga kode berhasil ter-update di server PWS.

4. Penataan Layout Responsif pada Hero Section
   * Prompt: "Gimana cara bikin foto sama teks sejajar di laptop tapi pas di HP numpuk ke bawah?"
   * Tujuan: Mengatur tata letak bagian atas web agar tetap simetris di layar PC maupun HP.
   * Respon AI: Memberikan contoh penggunaan media query CSS Grid untuk mengubah layout 2 kolom menjadi 1 kolom saat layar berukuran kecil.
   * Tindakan Saya: Saya menerapkan logika media query tersebut dan menambahkan aturan max-width: 190px secara manual pada foto agar tidak memenuhi layar HP.

5. Perbaikan Tata Bahasa Jawaban Refleksi
   * Prompt: "Tolong benerin tata bahasa refleksi tugas PBP aku dong biar ga kaku dan kalimatnya runtut"
   * Tujuan: Merapikan kalimat pada jawaban refleksi di README agar memenuhi standar pengumpulan tugas tanpa menghilangkan poin utama yang ingin saya sampaikan.
   * Respon AI: Merapikan struktur paragraf dan memperbaiki susunan kata agar kalimat refleksi menjadi lebih jelas dan sistematis.
   * Tindakan Saya: Saya membaca ulang hasilnya, menghapus bagian kalimat yang terasa terlalu rumit atau teoritis, dan menyesuaikannya kembali agar benar-benar mencerminkan pengalaman yang saya alami saat koding.