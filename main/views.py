from django.shortcuts import render
from main.models import Experience

def show_main(request):
    context = {
        "name": "Fatma Widya Rachma",
        "npm": "2506533614",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "IS @Universitas Indonesia with strong organizational, communication, marketing, and public-facing experience, interested in bridging business and technology."
        ),
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Fatma Widya Rachma",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)