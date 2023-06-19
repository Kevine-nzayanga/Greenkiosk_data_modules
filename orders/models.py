from django.db import models

class Orders(models.Model):
    userId = models.IntegerField()
    products = models.CharField(max_length=32)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    shippingAddress = models.CharField(max_length=100)
    orderDate = models.DateTimeField(auto_now_add=True)
    orderDate_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.products
# Create your models here.
