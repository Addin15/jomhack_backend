
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, User

# Create your models here.


class CustomUser(AbstractBaseUser):
    username = None
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', default=None, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.name
