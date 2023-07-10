from django.db import models

class Review(models.Model):
    customer_name = models.CharField(max_length=52)
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField()
# Create your models here.
