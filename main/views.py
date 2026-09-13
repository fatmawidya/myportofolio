from django.shortcuts import render
from main.models import Education, Experience

def show_main(request): #view untuk profil
    context = {
        "name": "Fatma Widya Rachma",
        "npm": "2506533614",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "IS @ Universitas Indonesia, interested in bridging business and technology."
        ),
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Fatma Widya Rachma",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "name": "Fatma Widya Rachma", # Nama untuk header/footer
        "education_list": Education.objects.all(), # Ambil seluruh data dari tabel Education
        }
    return render(request, "education.html", context)  # Kirim data ke template education.html baru