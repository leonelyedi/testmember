from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Fitness(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    premium = models.BooleanField(default=True)
