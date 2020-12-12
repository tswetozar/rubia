from django.db import models


# Create your models here.

class OffensiveWord(models.Model):
    word = models.CharField(max_length=30)
