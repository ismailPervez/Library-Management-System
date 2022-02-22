from django.db import models
from django.contrib.auth.models import AbstractUser

class Book(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField(max_length=150)
    in_store = models.IntegerField()

class BaseUser(AbstractUser):
    is_staff = models.BooleanField(default=False)