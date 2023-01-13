
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, User

# Create your models here.
class CustomUser(User):
    username = None
    name = models.CharField(max_length=255)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    objects = UserManager()

    def __str__(self):
        return self.name

