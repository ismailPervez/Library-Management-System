from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'Student/dashboard.html', {'title': 'students dashboard page'})