from django.db import models
from django.contrib.auth.models import AbstractUser
from Student.models import Student
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField(max_length=150)
    in_store = models.IntegerField()

class TakenBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_taken = models.DateTimeField(default=timezone.now)
    date_to_be_returned = models.DateTimeField()
    date_returned = models.DateTimeField()

class BaseUser(AbstractUser):
    is_staff = models.BooleanField(default=False)