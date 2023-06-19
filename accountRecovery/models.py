from django.db import models

class AccountRecovery(models.Model):
    userId = models.IntegerField()
    email = models.EmailField()
# Create your models here.
