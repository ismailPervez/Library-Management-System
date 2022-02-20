from django.shortcuts import render

def index(request):
    return render(request, 'Student/dashboard.html', {'title': 'students dashboard page'})