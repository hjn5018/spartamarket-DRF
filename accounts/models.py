from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    gender_choices = {
        ('male','male'),
        ('female','female')
    }
    # 필수 입력
    email = models.EmailField()
    name = models.TextField()
    nickname = models.CharField(max_length=20)
    birth_date = models.DateTimeField()
    
    # 생략 가능한 필드
    gender = models.CharField(max_length=6, choices=gender_choices, blank=True)
    introduce = models.TextField(blank=True)