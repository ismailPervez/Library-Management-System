from django.forms import CharField, EmailInput, ModelForm, PasswordInput, TextInput, Form
from .models import Student

class StudentRegistrationForm(ModelForm):

    # username = CharField(widget=TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'e.g john_doe',
    #     'required': True
    # }))

    # first_name = CharField(widget=TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'e.g John',
    #     'required': True
    # }))

    # last_name = CharField(widget=TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'e.g Doe',
    #     'required': True
    # }))

    # student_ID = CharField(widget=TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'e.g 1673827',
    #     'required': True
    # }))

    # email = CharField(widget=EmailInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'e.g johndoe@gmail.com',
    #     'required': True
    # }))

    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'enter a strong password',
        'required': True
    }))

    confirm_password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'confirm your password',
        'label': 'confirm password',
        'required': True
    }))

    class Meta:
        model = Student
        fields = ['username', 'first_name', 'last_name', 'student_ID', 'email', 'password', 'confirm_password']
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(StudentRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super(StudentRegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('confirm_password', 'passwords do not match')

        return cleaned_data

class StudentLoginForm(Form):
    email = CharField(widget=EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'e.g johndoe@gmail.com',
        'required': True
    }))

    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'enter a strong password',
        'required': True
    }))