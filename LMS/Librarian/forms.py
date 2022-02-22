from django.forms import forms
from .models import Librarian

class LibrarianRegistrationForm(forms.Form):
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