from django.db import models


class Refund(models.Model):
    orderId = models.IntegerField()
    refundId = models.IntegerField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    reason = models.TextField(blank=False)
    status = models.CharField(max_length=52)
    requestDate = models.DateTimeField(auto_now_add=True)
    processedDate = models.DateTimeField()

# Create your models here.
