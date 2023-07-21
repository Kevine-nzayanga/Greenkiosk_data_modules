from django.db import models

class Review(models.Model):
    customer_name = models.CharField(max_length=52)
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField()
    
def __str__(self):
      return self.customer_name    
# Create your models here.
