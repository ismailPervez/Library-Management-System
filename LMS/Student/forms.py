from django.forms import ModelForm
from .models import Student

class StudentRegistrationForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_ID', 'email']