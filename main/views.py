from django.shortcuts import render, redirect, get_object_or_404
from main.models import Education, Experience
from main.forms import ExperienceForm, EducationForm 
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied       
import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q

# Helper untuk mengecek apakah user adalah Editor
def is_editor_user(user):
    return user.is_authenticated and user.groups.filter(name='Editor').exists()

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
        messages.success(request, "Account created successfully. Please log in.")
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
    context = {
        "name": "Fatma Widya Rachma",
        "search_query": search_query,
        "is_editor": is_editor_user(request.user),
        "form": ExperienceForm(),
    }
    return render(request, "experience.html", context)

@login_required(login_url="/login/")
def create_experience(request):
    # HANYA SUPERUSER
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
    # SUPERUSER ATAU EDITOR
    if not (request.user.is_superuser or is_editor_user(request.user)):
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
    # HANYA SUPERUSER
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
    experiences = Experience.objects.prefetch_related('starred_by').all().order_by('-started_at')

    if search_query:
        experiences = experiences.filter(title__icontains=search_query)
        
    data = []
    for exp in experiences:
        starred_users = exp.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        
        data.append({
            "pk": str(exp.id),
            "fields": {
                "title": exp.title,
                "category": exp.category,
                "category_display": exp.get_category_display() if hasattr(exp, 'get_category_display') else exp.category,
                "thumbnail": exp.thumbnail if exp.thumbnail else "",
                "description": exp.description,
                "is_ongoing": exp.is_ongoing,
                "started_at": exp.started_at.strftime("%Y") if exp.started_at else "",
                "ended_at": exp.ended_at.strftime("%Y") if exp.ended_at else None,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
            }
        })
        
    return JsonResponse(data, safe=False)

def get_experience_xml(request):
    experiences = Experience.objects.all()
    data = serializers.serialize("xml", experiences)
    return HttpResponse(data, content_type="application/xml")

@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add experiences."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Experience added successfully.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

# ================= EDUCATION =================
def show_education(request):
    context = {
        "name": "Fatma Widya Rachma",
        "is_editor": is_editor_user(request.user),
        "search_query": request.GET.get("search", ""),
        "form": EducationForm(),
    }
    return render(request, "educational.html", context)

@login_required(login_url="/login/")
def create_education(request):
    # HANYA SUPERUSER
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

@login_required(login_url="/login/")
def edit_education(request, id):
    #SUPERUSER ATAU EDITOR
    if not (request.user.is_superuser or is_editor_user(request.user)):
        raise PermissionDenied
    
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

@login_required(login_url="/login/")
def delete_education(request, id):
    # HANYA SUPERUSER
    if not request.user.is_superuser:
        raise PermissionDenied
    
    education = get_object_or_404(Education, pk=id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Education deleted successfully!")
        return redirect("main:show_education")
    return redirect("main:show_education")

def get_education_json(request):
    query = request.GET.get("search", "").strip()
    educations = Education.objects.all()

    if query:
        educations = educations.filter(
        Q(institution__icontains=query) |
        Q(field_of_study__icontains=query) |
        Q(degree__icontains=query)
    ).distinct()

    data = []
    for edu in educations:
        data.append({
            "pk": str(edu.id),
            "fields": {
                "institution": edu.institution,
                "degree": edu.degree,
                "degree_display": edu.get_degree_display() if hasattr(edu, 'get_degree_display') else edu.degree,
                "field_of_study": edu.field_of_study,
                "start_year": edu.start_year,
                "end_year": edu.end_year,
                "is_current": edu.is_current,
                "description": edu.description,
                "thumbnail": edu.thumbnail if hasattr(edu, 'thumbnail') else '',
            }
        })
    return JsonResponse(data, safe=False)


@require_POST
def create_education_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add education."},
            status=403,
        )

    form = EducationForm(request.POST)
    if form.is_valid():
        education = form.save()
        return JsonResponse(
            {"message": "Education added successfully.", "pk": str(education.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)