from django.db import models

class Cart(models.Model):
    products=models.CharField(max_length=32)
    product_qty = models.IntegerField(default=0)
    price=models.IntegerField(null=False,blank=False, default=0)
    discount=models.IntegerField(default=0)

class CartItem(models.Model):
    
    def __str__(self):
        return self.product 
# Create your models here.
