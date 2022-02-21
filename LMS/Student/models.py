from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    student_ID = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=60, null=True)