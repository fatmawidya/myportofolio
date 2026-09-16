from django.shortcuts import render, redirect, get_object_or_404
from main.models import Education, Experience
from main.forms import ExperienceForm, EducationForm  # Tambahkan EducationForm
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse

def show_main(request):
    context = {
        "name": "Fatma Widya Rachma",
        "npm": "2506533614",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "IS @ Universitas Indonesia, interested in bridging business and technology."
        ),
    }
    return render(request, "index.html", context)

# ================= EXPERIENCE =================
def show_experience(request):
    search_query = request.GET.get("search", "").strip()
    experiences = Experience.objects.all().order_by('-started_at')
    if search_query:
        experiences = experiences.filter(title__icontains=search_query)

    context = {
        "name": "Fatma Widya Rachma",
        "experience_list": experiences, 
        "search_query": search_query,
    }
    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience successfully added!")
        return redirect('main:show_experience')

    context = {
        'form': form,
        'name': 'Fatma Widya Rachma', 
    }
    return render(request, "create_experience.html", context)

def edit_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience successfully updated!")
        return redirect('main:show_experience')

    context = {
        'form': form,
        'name': 'Fatma Widya Rachma', 
        'experience': experience, 
    }
    return render(request, "components/edit_experience.html", context)

def delete_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience deleted successfully!")
        return redirect("main:show_experience")
    return redirect("main:show_experience")

# API Endpoints
def get_experience_json(request):
    search_query = request.GET.get("search", "").strip()
    experiences = Experience.objects.all().order_by('-started_at')
    
    if search_query:
        experiences = experiences.filter(title__icontains=search_query)
        
    data = serializers.serialize("json", experiences)
    return HttpResponse(data, content_type="application/json")

def get_experience_xml(request):
    experiences = Experience.objects.all()
    data = serializers.serialize("xml", experiences)
    return HttpResponse(data, content_type="application/xml")


# ================= EDUCATION =================
def show_education(request):
    context = {
        "name": "Fatma Widya Rachma",
        "education_list": Education.objects.all().order_by('-start_year'),
    }
    return render(request, "educational.html", context)

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education successfully added!")
        return redirect('main:show_education')

    context = {
        'form': form,
        'name': 'Fatma Widya Rachma', 
    }
    return render(request, "create_education.html", context)

def edit_education(request, id):
    education = get_object_or_404(Education, pk=id)
    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education successfully updated!")
        return redirect('main:show_education')

    context = {
        'form': form,
        'name': 'Fatma Widya Rachma', 
        'education': education, 
    }
    return render(request, "components/edit_education.html", context)

def delete_education(request, id):
    education = get_object_or_404(Education, pk=id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Education deleted successfully!")
        return redirect("main:show_education")
    return redirect("main:show_education")