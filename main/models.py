import uuid
from django.db import models
from django.contrib.auth.models import User

class Experience(models.Model): 
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'), 
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
    started_at = models.DateTimeField() # Tanggal dimulai
    ended_at = models.DateTimeField(blank=True, null=True) # Tanggal selesai, boleh kosong kalau masih berjalan

    starred_by = models.ManyToManyField(
        User, related_name="starred_projects", blank=True
    )
    
    def __str__(self): 
        return self.title 
    
    @property
    def is_ongoing(self):
        return self.ended_at is None 

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
    description = models.TextField() #deskripsi (panjang)

    def __str__(self):  
        return f"{self.institution} - {self.field_of_study}"  # nampilin format "Nama Sekolah/Kampus - Jurusan"
    
    @property  
    def is_current(self):  # Fungsi buat ngecek apakah masih status siswa/mahasiswa aktif
        return self.end_year is None  # Mengembalikan True jika end_year kosong
