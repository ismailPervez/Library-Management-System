from django.forms import CharField, EmailInput, ModelForm, TextInput
from .models import Student

class StudentRegistrationForm(ModelForm):
    first_name = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'e.g John'
    }))

    last_name = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'e.g Doe'
    }))

    student_ID = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'e.g 1673827'
    }))

    email = CharField(widget=EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'e.g johndoe@gmail.com'
    }))

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_ID', 'email']