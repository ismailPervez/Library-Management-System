from django.shortcuts import render, redirect
from Library.models import TakenBook, Book
from .forms import LibrarianRegistrationForm, LibrarianLoginForm
from .models import Librarian
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    librarian = Librarian.objects.filter(username=request.user.username).first()
    if librarian is None:
        return redirect('student-home')
    book_count = sum([book.in_store for book in Book.objects.all()])
    out_count = len(TakenBook.objects.all())
    in_count = book_count - out_count
    context = {
        'title': 'Librarian Home Page',
        'book_count': book_count,
        'out_count': out_count,
        'in_count': in_count,
        'staff_id': librarian.staff_ID
    }
    return render(request, 'Librarian/dashboard.html', context)

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
    if request.method == 'POST':
        form = LibrarianLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            librarian_obj = Librarian.objects.get(email=email)
            print(librarian_obj)
            if librarian_obj:
                print(password)
                if check_password(password, librarian_obj.password):
                    login(request, librarian_obj)
                    messages.success(request, 'login successfull')
                    return redirect('librarian-home')
                else:
                    messages.info(request, 'login unsuccessfull')
                    return redirect('student-login')
            else:
                messages.info(request, 'That email does not exist!')
                return redirect('student-login')
    else:
        form = LibrarianLoginForm()
    return render(request, 'Librarian/login.html', {'form': form})