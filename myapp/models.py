from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title

class SoftInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=64)
    size = models.CharField(max_length=64)

    def __str__(self):
        return self.product.__str__()

class HardInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.CharField(max_length=64)
    height = models.CharField(max_length=64)

    def __str__(self):
        return self.product.__str__()

class Item(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title
