from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.FloatField()
    release_date = models.DateField()
    review = models.TextField()
    # item_price = models.BigIntegerField()
    # item_stock = models.IntegerField()
    # description = models.TextField()
    # rating = models.IntegerField()
    # item_url = models.URLField()
