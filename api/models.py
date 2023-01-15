from django.db import models
from django.db.models import CASCADE
from users.models import CustomUser

# Create your models here.


class Provider(models.Model):
    name = models.CharField(max_length=255, unique=True)
    logo = models.URLField()
    about = models.TextField()
    phone = models.CharField(max_length=15, null=True, default=None)
    email = models.EmailField(null=True, default=None)
    website = models.URLField(null=True, default=None)


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


class Assestment(models.Model):
    user_id = models.TextField(unique=True, primary_key=True)
    age = models.IntegerField()
    job_description = models.TextField()
    existing_condition = models.TextField()
    family_history = models.TextField()
    smoker = models.BooleanField()
    married = models.BooleanField()
