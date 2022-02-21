from django.db import models
from django.contrib.auth.models import AbstractUser

class Student(AbstractUser):
    student_ID = models.CharField(max_length=30)