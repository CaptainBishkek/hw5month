from django.db import models
from django.core import validators


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField(max_length=300, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Review(models.Model):
    text = models.TextField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)])

    def __str__(self):
        return f'{self.text}'
