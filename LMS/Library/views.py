from django.shortcuts import render

def index(request):
    return render(request, 'Library/index.html')

def register(request):
    return render(request, 'Library/register.html')