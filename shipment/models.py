from django.db import models

class Shipment(models.Model):
    orders= models.ManyToManyField(Order)
    tracking_number = models.CharField(max_length=128)
    destination = models.CharField(max_length=128)
    date_shipped = models.DateTimeField()
    
    def __str__(self):
        return self.tracking_number
    
# Create your models here.
