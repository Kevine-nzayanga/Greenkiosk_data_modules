from django.db import models

class Cart(models.Model):
    product_name=models.CharField(max_length=32)
    product_id=models.IntegerField()
    price=models.IntegerField()
    discount=models.IntegerField()

    def __str__(self):
        return self.product_name
# Create your models here.
