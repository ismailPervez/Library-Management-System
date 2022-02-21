from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Student.models import Student

@api_view(['PUT'])
def update_student(request, email):
    if request.method == 'PUT':
        student = Student.objects.filter(email=email).first()
        print(request.data)
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