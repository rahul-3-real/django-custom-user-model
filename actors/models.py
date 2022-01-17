from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.


class Actor(models.Model):
    name = models.CharField(max_length=200)
    is_star = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'
