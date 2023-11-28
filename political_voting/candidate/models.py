# candidate/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Poll(models.Model):
    """
    Model representing a poll.

    Fields:
    - question (CharField): The question of the poll.
    - option1 (CharField): The first option for the poll.
    - option2 (CharField): The second option for the poll.

    Methods:
    - __str__(): Returns a string representation of the poll (question).

    Usage:
    - This model is used to represent polls in the application.
    """
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)

    def __str__(self):
        """
        Returns a string representation of the poll (question).
        """
        return self.question
