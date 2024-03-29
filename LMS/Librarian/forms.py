from django.forms import ModelForm, CharField, PasswordInput, TextInput, EmailInput, Form
from .models import Librarian

class LibrarianRegistrationForm(ModelForm):  
    username = CharField(widget=TextInput(attrs={
        'class': 'form-control shadow-none',
        'placeholder': 'e.g john_doe',
        'required': True
    }))

    first_name = CharField(widget=TextInput(attrs={
        'class': 'form-control shadow-none',
        'placeholder': 'e.g John',
        'required': True
    }))

    last_name = CharField(widget=TextInput(attrs={
        'class': 'form-control shadow-none',
        'placeholder': 'e.g Doe',
        'required': True
    }))

    staff_ID = CharField(widget=TextInput(attrs={
        'class': 'form-control shadow-none',
        'placeholder': 'e.g 1673827',
        'required': True
    }))

    email = CharField(widget=EmailInput(attrs={
        'class': 'form-control shadow-none',
        'placeholder': 'e.g johndoe@gmail.com',
        'required': True
    }))

    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control shadow-none',
        'placeholder': 'enter a strong password',
        'required': True
    }))

    confirm_password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control shadow-none',
        'placeholder': 'confirm your password',
        'label': 'confirm password',
        'required': True
    }))

    class Meta:
        model = Librarian
        fields = ['username', 'first_name', 'last_name', 'staff_ID', 'email', 'password', 'confirm_password']

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(LibrarianRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super(LibrarianRegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('confirm_password', 'passwords do not match')

        return cleaned_data

class LibrarianLoginForm(Form):
    email = CharField(widget=EmailInput(attrs={
        'class': 'form-control shadow-none',
        'placeholder': 'e.g johndoe@gmail.com',
        'required': True
    }))

    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control shadow-none',
        'placeholder': 'enter a strong password',
        'required': True
    }))