from django.shortcuts import render
from .forms import LibrarianRegistrationForm
from django.contrib import messages

def index(request):
    return render(request, 'Librarian/dashboard.html', {'title': 'Librarian Home Page'})

def register(request):
    if request.method == 'POST':
        form = LibrarianRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successfull, you can now login')
    else:
        form = LibrarianRegistrationForm()

    return render(request, 'Student/register.html', {'form': form})

def log_in(request):
    return render(request, 'Librarian/login.html')