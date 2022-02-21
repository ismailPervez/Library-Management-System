import django
from django.shortcuts import render, redirect
from .forms import StudentLoginForm, StudentRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from .models import Student

def index(request):
    return render(request, 'Student/dashboard.html', {'title': 'students dashboard page'})

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            # print('New student registered')
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            student_ID = form.cleaned_data['student_ID']
            password = make_password(form.cleaned_data['password'])
            new_student = Student(
                first_name=first_name,
                last_name=last_name,
                email=email,
                student_ID=student_ID,
                password=password
            )
            new_student.save()
            messages.success(request, 'Registration successfull, you can now login')
    else:
        form = StudentRegistrationForm()

    return render(request, 'Student/register.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            student_obj = Student.objects.get(email=email)
            if student_obj:
                if check_password(password, student_obj.password):
                    login(request, student_obj)
                    messages.success(request, 'login successfull')
                    return redirect('student-home')
                else:
                    messages.info(request, 'login unsuccessfull')
                    return redirect('student-login')
            else:
                messages.info(request, 'That email does not exist!')
                return redirect('student-login')
    else:
        form = StudentLoginForm()
    return render(request, 'Student/login.html', {'form': form})