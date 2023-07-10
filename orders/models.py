from django.db import models
from payment.models import PaymentMethod
from customer.models import Customer
from shoppingcart.models import Cart

class Order(models.Model):
    payment= models.OneToOneField(PaymentMethod,on_delete=models.PROTECT,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True)
    products = models.CharField(max_length=32)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    shippingAddress = models.CharField(max_length=100)
    orderDate = models.DateTimeField(auto_now_add=True)
    orderDate_update = models.DateTimeField(auto_now=True)
    cart= models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    


    def __str__(self):
        return self.products
# Create your models here.
