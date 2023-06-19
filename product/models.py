from django.contrib.auth.models import User
from django.db import models
import os


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to=os.path.join(os.path.dirname(
        __file__)[:-8], 'store', 'static', 'product_images'))
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
