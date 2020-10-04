from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def blog(request):
    return render(request, "blog.html")

def projects(request):
    return render(request, "projects.html")

def photography(request):
    return render(request, "photography.html")

def about(request):
    return render(request, "about.html")