from django.db import models


# Create your models here.
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=20)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=False)
    author = models.CharField(max_length=32, null=False)


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=False)