from django.shortcuts import render
from .forms import StudentRegistrationForm

def index(request):
    return render(request, 'Student/dashboard.html', {'title': 'students dashboard page'})

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print('New student registered')
    else:
        form = StudentRegistrationForm()

    return render(request, 'Student/register.html', {'form': form})