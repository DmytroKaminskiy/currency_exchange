from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser


def avatar_path(instance, filename: str) -> str:
    # ext = filename.split('.')[-1]
    # f = str(uuid4())
    # filename = f'{f}.{ext}'
    # return '/'.join(['hello', filename])

    return '/'.join(['avatar', str(instance.id), str(uuid4()), filename])


class User(AbstractUser):
    avatar = models.ImageField(upload_to=avatar_path,
                               null=True, blank=True,
                               default=None)


class Contact(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=256)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
