from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    date_of_birth= models.DateField()
    email=models.EmailField()
    phone_number=models.CharField(max_length=13)
    password=models.CharField(max_length=8)

def __str__(self):
 return self.first_name
# Create your models here.
