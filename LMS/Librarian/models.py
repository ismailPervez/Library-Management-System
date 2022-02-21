from django.db import models
from django.contrib.auth.models import AbstractUser

class Librarian(AbstractUser):
    staff_ID = models.CharField(max_length=30)