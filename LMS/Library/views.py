from django.shortcuts import render
from .models import Book, WishList

def index(request):
    return render(request, 'Library/index.html')

def register(request):
    return render(request, 'Library/register.html')

def login(request):
    return render(request, 'Library/login.html')

def explore(request):
    books = Book.objects.all()
    return render(request, 'Library/explore.html', {'books': books})

def get_book(request, book_id):
    book = Book.objects.get(pk=book_id)

    if book:
        if request.user:
            in_wishlist = WishList.objects.filter(book=book, student=request.user).first()
            if in_wishlist is not None:
                return render(request, 'Library/book.html', {'book': book, 'in_wishlist': True})
            
            else:
                return render(request, 'Library/book.html', {'book': book, 'in_wishlist': False})
        else:
            return render(request, 'Library/book.html', {'book': book})

def search(request, query):
    books = Book.objects.all()
    results = [book for book in books if query.lower() in book.title.lower()]
    print(results)
    return render(request, 'Library/results.html', {'books': results, 'query': query})
    