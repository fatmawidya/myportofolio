import uuid
from django.db import models

class Experience(models.Model): # Buat tabel 'Experience' di database
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'), # Opsi 1: ('nilai_di_database', 'teks_tampilan')
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]

    # Primary key pakai UUID biar acak & unik
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # Primary key pakai UUID acak, gak bisa diedit manual
    title = models.CharField(max_length=255) # judul (maksimal 255 karakter (pendek)) 
    description = models.TextField() #deskripsi (panjang)
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time') # Kolom pilihan jenis pengalaman
    thumbnail = models.URLField(blank=True, null=True) # Kolom link gambar, boleh kosong di form maupun database
    started_at = models.DateTimeField(auto_now_add=True) # Tanggal dimulai, otomatis terisi waktu saat data masuk
    ended_at = models.DateTimeField(blank=True, null=True) # Tanggal selesai, boleh kosong kalau masih berjalan

    def __str__(self): # Fungsi bawaan Python buat ngatur representasi teks dari objek
        return self.title # nampilin judul pengalaman pas objek ini dipanggil/dilihat
    
    @property
    def is_ongoing(self): # Fungsi buat ngecek apakah posisi ini masih berjalan
        return self.ended_at is None # Mengembalikan True jika ended_at kosong (belum selesai)

# ============== EDUCATION ====================

class Education(models.Model):  
    DEGREE_CHOICES = [  
        ('elementary', 'Elementary School'),  
        ('junior_high', 'Junior High School'),  
        ('high_school', 'High School'),  
        ('bachelor', 'Bachelor Degree'),  
        ('master', 'Master Degree'),  
        ('doctoral', 'Doctoral Degree'),  
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Primary key UUID acak
    institution = models.CharField(max_length=255)  # Kolom nama kampus/sekolah 
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES, default='bachelor')  # Kolom jenjang pendidikan
    field_of_study = models.CharField(max_length=255)  # Kolom jurusan / bidang studi 
    start_year = models.IntegerField()  # Kolom tahun masuk (tipe data angka bulat)
    end_year = models.IntegerField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)

    def __str__(self):  
        return f"{self.institution} - {self.field_of_study}"  # nampilin format "Nama Sekolah/Kampus - Jurusan"
    
    @property  
    def is_current(self):  # Fungsi buat ngecek apakah masih status siswa/mahasiswa aktif
        return self.end_year is None  # Mengembalikan True jika end_year kosong
