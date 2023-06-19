from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=32)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()
    category=models.CharField(max_length=50)

# Create your models here.
