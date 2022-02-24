from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Student.models import Student
from Library.models import Book, WishList
from .serializers import WishlistSerializer

@api_view(['PUT'])
def update_student(request, email):
    if request.method == 'PUT':
        student = Student.objects.filter(email=email).first()
        # print(request.data)
        data = request.data
        if not student:
            return Response({'msg': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        
        student.username = data['username']
        student.first_name = data['first_name']
        student.last_name = data['last_name']
        student.email = data['email']
        student.save()

        return Response({'msg': 'user updated successfully!'}, status=status.HTTP_200_OK)
    
    return Response({'msg': 'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def add_to_wishlist(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(pk=book_id)

        if book is None:
            return Response({'msg': 'book not found', 'status_code': 404}, status=status.HTTP_404_NOT_FOUND)

        else:
            if not request.user.is_authenticated:
                return Response({'msg': 'you need to be logged in', 'status_code': 401}, status=status.HTTP_401_UNAUTHORIZED)

            else:
                student = Student.objects.filter(username=request.user.username).first()
                print(student)
                if student:
                    new_wishlist = WishList(
                        book=book,
                        student=student
                    )

                    new_wishlist.save()

                else:
                    return Response({'msg': 'not a valid user'}, status=status.HTTP_401_UNAUTHORIZED)

                return Response({'msg': 'book added to wishlist!', 'status_code': 200}, status=status.HTTP_200_OK)

    else:
        return Response({'msg': 'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
def remove_wishlist(request, book_id):
    if request.method == 'DELETE':
        book = Book.objects.get(pk=book_id)

        if book is None:
            return Response({'msg': 'book not found'}, status=status.HTTP_404_NOT_FOUND)

        else:
            if not request.user.is_authenticated:
                return Response({'msg': 'you need to be logged in'}, status=status.HTTP_401_UNAUTHORIZED)

            else:
                student = Student.objects.filter(username=request.user.username).first()
                if student:
                    wishlist = WishList.objects.filter(book=book, student=student)
                    wishlist.delete()

                    wishlist_books = WishList.objects.filter(student=student).all()
                    JSON_wishlist = WishlistSerializer(wishlist_books, many=True)

                else:
                    return Response({'msg': 'not a valid user'}, status=status.HTTP_401_UNAUTHORIZED)

                return Response({'msg': 'book removed from wishlist!', 'wishlist': JSON_wishlist.data, 'status_code': 200}, status=status.HTTP_200_OK)
    
    else:
        return Response({'msg': 'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)