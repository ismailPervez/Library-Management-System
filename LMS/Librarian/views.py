from django.shortcuts import render

def index(request):
    return render(request, 'Librarian/dashboard.html', {'title': 'Librarian Home Page'})

def register(request):
    return render(request, 'Librarian/register.html')

def log_in(request):
    return render(request, 'Librarian/login.html')