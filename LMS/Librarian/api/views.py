from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Librarian.models import Librarian
from Library.models import Book, TakenBook
from Student.models import Student
from django.utils.dateparse import parse_date
import pytz

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
            return Response({'msg': 'data not found'}, status=status.HTTP_404_NOT_FOUND) 

        new_book = Book(
            title=request.data['title'],
            desc=request.data['desc'],
            in_store=int(request.data['in_store'])
        )
        new_book.save()
        
        return Response({'msg': 'new book has been added to the library'}, status=status.HTTP_201_CREATED)

    else:
        return Response({'msg': 'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def  register_taken_book(request):
    if request.method == 'POST':
        data = request.data
        if not data:
            return Response({'msg': 'data not found'}, status=status.HTTP_404_NOT_FOUND) 

        else:
            book_title = request.data['book_title']
            student_id = request.data['student_id']
            date_to_return = request.data['date_to_return']

            book = Book.objects.filter(title=book_title).first()
            student = Student.objects.filter(student_ID=student_id).first()

            if book is None:
                return Response({'msg': 'book not found'}, status=status.HTTP_404_NOT_FOUND)  

            elif student is None:
                return Response({'msg': 'student not found'}, status=status.HTTP_404_NOT_FOUND) 
            
            else:
                new_taken_book = TakenBook(
                    book=book,
                    student=student,
                    date_to_be_returned=date_to_return
                )

                # print(date_to_return)
                # print(type(date_to_return))

                # print('---------------------')

                # print(parse_date(date_to_return))
                # print(type(parse_date(date_to_return)))
                # print(pytz.utc.localize(parse_date(date_to_return)))

                new_taken_book.save()

                return Response({'msg': f"added book to {student.username}'s borrowed list"}, status=status.HTTP_200_OK) 

                # send an email to student - notification
        
    else:
        return Response({'msg': 'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)