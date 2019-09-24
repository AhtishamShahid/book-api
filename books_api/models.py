from django.db import models


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    isbn = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    number_of_pages = models.IntegerField()
    publisher = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    released = models.DateField()
