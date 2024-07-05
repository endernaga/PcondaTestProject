from django.db import models


class Book(models.Model):  # Creating a book model using Django ORM
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(auto_now=True)
    isbn = models.CharField(max_length=255, unique=True)
    pages = models.IntegerField()
