from operator import mod
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    is_director = models.BooleanField(default=False)
    is_producer = models.BooleanField(default=False)
