from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Menstrual(models.Model):
    bloody = models.BooleanField(default=False)
    date = models.DateField()
    flow = models.TextField()
    cramps = models.BooleanField(default=False)
    migraine = models.BooleanField(default=False)
    bloating = models.BooleanField(default=False)
    emo = models.BooleanField(default=False)
    anger = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    sex = models.BooleanField(default=False)
    nausea = models.BooleanField(default=False)
    sore = models.BooleanField(default=False)
    fatigue = models.BooleanField(default=False)
    aches = models.BooleanField(default=False)
    patriarchy = models.BooleanField(default=False)

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
  

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']