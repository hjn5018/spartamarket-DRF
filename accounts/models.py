from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    gender_choices = {
        
    }


    birth_date = models.DateTimeField(null=True)
    nickname = models.CharField(max_length=20, blank=True)
    gender = models.CharField()