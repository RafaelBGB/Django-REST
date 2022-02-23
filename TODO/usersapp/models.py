from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import models


class User(AbstractUser):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    birthday_year = models.PositiveIntegerField(verbose_name='год рождения')
    email = models.EmailField(unique=True)
