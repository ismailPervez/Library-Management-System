from django.db import models
from Library.models import BaseUser
from Library.models import Book

class Student(BaseUser):
    student_ID = models.CharField(max_length=30)
    is_librarian = models.BooleanField(default=False)