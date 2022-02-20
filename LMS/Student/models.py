from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30, null=False, blank=False)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    student_ID = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField()
