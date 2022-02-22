from django.db import models
from Library.models import BaseUser

class Librarian(BaseUser):
    staff_ID = models.CharField(max_length=30)