from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()

    def __str__(self):
        return self.title