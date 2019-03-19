from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=32, unique=True)


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=99.99)
    stock = models.IntegerField(default=1000)
    sold = models.IntegerField(default=0)
    publisher = models.ForeignKey(to='Publisher', related_name='books')


class Author(models.Model):
    name = models.CharField(max_length=32)
    books = models.ManyToManyField(to='Book')


class Person(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=18)
    birthday = models.DateField(auto_now_add=True)