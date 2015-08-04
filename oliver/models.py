import hashlib
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from restapp import settings


class Account(models.Model):
    SEXS = (
        ('m', 'Man'),
        ('w', 'Woman'),

    )

    id=models.AutoField(primary_key=True,auto_created=True)
    created = models.DateTimeField(auto_now_add=True)
    accountName=models.CharField(unique=True,max_length=200,null=True)
    password=models.CharField(max_length=200)
    nick=models.CharField(max_length=100)
    sex=models.CharField(max_length=10,choices=SEXS)









