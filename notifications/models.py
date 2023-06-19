from django.db import models

class Notifications(models.Model):
    userId = models.IntegerField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
# Create your models here.
