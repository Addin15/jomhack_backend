from django.db import models
from django.db.models import CASCADE

# Create your models here.


class Provider(models.Model):
    name = models.CharField(max_length=255, unique=True)
    logo = models.URLField()
    about = models.TextField()


class Plans(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    category = models.CharField(max_length=100)
    keys = models.JSONField()
    provider = models.ForeignKey(Provider, on_delete=CASCADE)


class News(models.Model):
    title = models.CharField(max_length=100)
    about = models.TextField()
    category = models.CharField(max_length=100)
    keys = models.JSONField()
    link = models.URLField()
