from django.db import models

class PaymentMethod(models.Model):
    userId= models.IntegerField()
    orderId = models.IntegerField()
    payment_method = models.CharField(max_length=64)
    payment_amount = models.DecimalField(max_digits=100000, decimal_places=2)
    transactionId = models.IntegerField()

# Create your models here.
