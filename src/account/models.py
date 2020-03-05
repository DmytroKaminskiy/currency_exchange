from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Contact(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=256)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
