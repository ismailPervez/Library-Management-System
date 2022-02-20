from django.shortcuts import render
from .forms import StudentRegistrationForm

def index(request):
    return render(request, 'Student/dashboard.html', {'title': 'students dashboard page'})

def register(request):
    form = StudentRegistrationForm()
    return render(request, 'Student/register.html', {'form': form})