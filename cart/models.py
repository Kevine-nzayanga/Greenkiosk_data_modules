from django.db import models
from customer.models import Customer
from inventory.models import Product

class CartItem(models.Model):
    # user = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(default=1)
    price=models.IntegerField(null=False,blank=False, default=0)
    discount=models.PositiveIntegerField(default=1)


class Cart(models.Model):
    name = models.CharField(max_length=40, null = True, blank=True)
    items = models.ManyToManyField(CartItem, blank=True)
    timestamp = models.DateField(auto_now_add=True)



    
def __str__(self):
        return self.product 
    
# def get_summed_price(self):
#         #gets the price of all products
#         sum = 0
#         for CartItem in self.CartItem.all():
#             sum += CartItem.product.get_price() * CartItem.product_qty
#         return sum

    
    
    


# Create your models here.
