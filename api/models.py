from django.db import models

# Create your models here.

class Keywords(models.Model):
    keyword = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now=True)

class Sources(models.Model):
    source = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now=True)

class News(models.Model):
    headline = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    source = models.CharField(max_length=60)
    keyword_id = models.ForeignKey(Keywords, on_delete=models.CASCADE)
    expiry_date = models.DateTimeField()

class NewsHistory(models.Model):
    headline = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    source = models.CharField(max_length=60)
    keyword_id = models.ForeignKey(Keywords, on_delete=models.CASCADE)
    expiry_date = models.DateTimeField()