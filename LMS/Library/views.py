from django.shortcuts import render
from .models import Book

def index(request):
    return render(request, 'Library/index.html')

def register(request):
    return render(request, 'Library/register.html')

def login(request):
    return render(request, 'Library/login.html')

def explore(request):
    books = Book.objects.all()
    return render(request, 'Library/explore.html', {'books': books})