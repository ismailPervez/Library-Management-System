from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Librarian.models import Librarian
from Library.models import Book

@api_view(['PUT'])
def update_user(request, email):
    if request.method == 'PUT':
        data = request.data
        if not data:
            return Response({'msg': 'not data found'}, status=status.HTTP_404_NOT_FOUND)

        user = Librarian.objects.filter(email=email).first()
        if not user:
            return Response({'mag': 'user not found'}, status=status.HTTP_404_NOT_FOUND)

        username = request.data['username']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']

        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return Response({'msg': 'user updated successfully'}, status=status.HTTP_200_OK)

    return Response({'msg': 'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def add_book(request):
    if request.method == 'POST':
        if not request.data:
            return Response({'msg': 'not data found'}, status=status.HTTP_404_NOT_FOUND) 

        new_book = Book(
            title=request.data['title'],
            desc=request.data['desc'],
            in_store=int(request.data['in_store'])
        )
        new_book.save()
        
        return Response({'msg': 'new book has been added to the library'}, status=status.HTTP_201_CREATED)

    else:
        return Response({'msg': 'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)