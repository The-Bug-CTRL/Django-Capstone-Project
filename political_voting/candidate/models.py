# candidate/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Poll(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)

    def __str__(self):
        return self.question

