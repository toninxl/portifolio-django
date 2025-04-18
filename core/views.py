from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'core/projects.html', {'projects': projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'core/project_detail.html', {'project': project})

def contato(request):
    return render(request, 'core/contato.html')
