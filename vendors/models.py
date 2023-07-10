from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phoneNumber=models.CharField(max_length=15)
    address = models.CharField(max_length=100)

    def __str__(self):
     return self.name
# Create your models here.
