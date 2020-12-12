from django.db import models

# Create your models here.


class BadWord(models.Model):
    word = models.CharField(max_length=30)