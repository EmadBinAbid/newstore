from django.db import models

# Create your models here.

class News(models.Model):
    headline = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    source = models.CharField(max_length=60)