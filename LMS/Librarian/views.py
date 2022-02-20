from django.shortcuts import render

def index(request):
    return render(request, 'Librarian/dashboard.html', {'title': 'Librarian Home Page'})