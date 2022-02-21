from Student.models import Student
from rest_framework.serializers import ModelSerializer

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['username', 'first_name', 'last_name', 'email']