from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # birth_date = models.DateTimeField()
    nickname = models.CharField(max_length=20)