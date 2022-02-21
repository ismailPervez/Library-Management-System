from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField(max_length=150)
    in_store = models.IntegerField()
    