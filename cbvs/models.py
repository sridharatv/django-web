from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    publisher = models.CharField(max_length=128)
    year = models.PositiveIntegerField()
    pages = models.PositiveIntegerField

    def __str__(self):
        return self.title

class Library (models.Model):
    name = models.CharField(max_length=128)
    books = models.ManyToManyField(Book, related_name='books')
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name



