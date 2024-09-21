from django.db import models

class Movie(models.Model):
    rdate = models.DateField()
    movie_name = models.CharField(max_length=30)
    actor = models.CharField(max_length=30)
    actress = models.CharField(max_length=30)
    rating = models.IntegerField()
