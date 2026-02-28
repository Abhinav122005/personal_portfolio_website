from django.shortcuts import render
from projects.models import Project

def home_view(request):
    projects = Project.objects.all().order_by('-created_at')[:3]
    return render(request, 'home/index.html', {'projects': projects})

def resume(request):
    return render(request, "home/resume.html")