from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Book(models.Model):
    title = models.CharField(max_length=30)
    total_pages = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    isbn = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.CharField(max_length=30)
    year = models.CharField(max_length=20)

    def __str__(self):
        return self.title
