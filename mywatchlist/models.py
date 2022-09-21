from django.db import models

# Fix 1
# Create your models here.
class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.FloatField()
    release_date = models.DateField()
    review = models.TextField()
