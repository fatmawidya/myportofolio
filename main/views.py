from django.shortcuts import render, redirect, get_object_or_404
from main.models import Education, Experience
from main.forms import ExperienceForm, EducationForm 
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied       
import datetime

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'No active login session / Cookie not found')
    context = {
        "name": "Fatma Widya Rachma",
        "npm": "2506533614",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "IS @ Universitas Indonesia, interested in bridging business and technology."
        ),
            "last_login": last_login,

    }
    return render(request, "index.html", context)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Fatma",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Fatma",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        # Jika akun ini sudah pernah memberi star, batalkan star-nya.
        # Jika belum, tambahkan star.
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

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

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
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

@login_required(login_url="/login/")
def edit_experience(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
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

@login_required(login_url="/login/")
def delete_experience(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
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
        
    data = serializers.serialize("json", experiences, use_natural_foreign_keys=True)
    return HttpResponse(data, content_type="application/json")

def get_experience_xml(request):
    experiences = Experience.objects.all()
    data = serializers.serialize("xml", experiences)
    return HttpResponse(data, content_type="application/xml")

@login_required(login_url="/login/")
def toggle_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

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