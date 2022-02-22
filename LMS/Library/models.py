from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class BaseUser(AbstractUser):
    pass

# Due to circular imports
from Student.models import Student

class Book(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField(max_length=150)
    in_store = models.IntegerField()

class TakenBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_taken = models.DateTimeField(default=timezone.now)
    date_to_be_returned = models.DateTimeField()
    date_returned = models.DateTimeField(null=True)

class WishList(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)