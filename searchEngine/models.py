from django.db import models

class SearchEngine(models.Model):
    userId = models.IntegerField()
    searchQuerry = models.TextField()
    results = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
# Create your models here.
