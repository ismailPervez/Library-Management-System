from django.shortcuts import render

def index(request):
    return render(request, 'Librarian/index.html', {'title': 'Librarian Home Page'})