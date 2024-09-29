from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(blank=True)