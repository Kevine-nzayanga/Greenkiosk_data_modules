from django.db import models

class Discount(models.Model):
    code = models.IntegerField()
    percentage = models.DecimalField(max_digits=4, decimal_places=2)
    expiry_date = models.DateField(auto_now_add=True)


# Create your models here.
