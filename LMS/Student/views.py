import django
from django.shortcuts import render
from .forms import StudentLoginForm, StudentRegistrationForm
from django.contrib import messages

def index(request):
    return render(request, 'Student/dashboard.html', {'title': 'students dashboard page'})

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print('New student registered')
            messages.success(request, 'Registration successfull, you can now login')
    else:
        form = StudentRegistrationForm()

    return render(request, 'Student/register.html', {'form': form})

def log_in(request):
    form = StudentLoginForm()
    return render(request, 'Student/login.html', {'form': form})