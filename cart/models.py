from django.db import models
from customer.models import Customer
from inventory.models import Product

class CartItem(models.Model):
    # user = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    product_qty = models.IntegerField(default=0)
    price=models.IntegerField(null=False,blank=False, default=0)
    discount=models.PositiveIntegerField(default=1)


class Cart(models.Model):
    # user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem, blank=True)


    
    def __str__(self):
        return self.product 
    


# Create your models here.
