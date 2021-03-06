import django
from django.shortcuts import render, redirect
from .forms import StudentLoginForm, StudentRegistrationForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password, check_password
from .models import Student
from django.contrib.auth.decorators import login_required
from Library.models import TakenBook, WishList

@login_required()
def index(request):
    user = request.user
    student = Student.objects.filter(username=user.username).first()
    if student is None:
        return redirect('librarian-home')
    taken_books = TakenBook.objects.filter(student=request.user).all()
    wishlist = WishList.objects.filter(student=request.user).all()
    context = {
        'title': 'students dashboard page',
        'taken_books': taken_books,
        'wishlist': wishlist,
        'student_id': student.student_ID
    }
    return render(request, 'Student/dashboard.html', context)

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
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
            print(student_obj)
            if student_obj:
                print(password)
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