from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)


class Product(models.Model):
    code = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Stock(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='stock', null=True, blank=True)
