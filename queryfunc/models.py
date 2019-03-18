from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=32, unique=True)


class Book(models.Model):
    title = models.CharField(max_length=32)
    publisher = models.ForeignKey(to='Publisher')


class Author(models.Model):
    name = models.CharField(max_length=32)
    books = models.ManyToManyField(to='Book')


class Person(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=18)
    birthday = models.DateField(auto_now_add=True)