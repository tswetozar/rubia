from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from accounts.models import CustomUser
from rx.validators import contains_only_letters, offensive_word


class Rx(models.Model):
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('H', 'On Hold'),
        ('P', 'Prepared'),
        ('R', 'Ready For Pick-up'),
        ('F', 'Finished'),
    )
    first_name = models.CharField(
        max_length=20,
        blank=True,
        validators=(
            contains_only_letters,
            offensive_word,
        )
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
        validators=(
            contains_only_letters,
            offensive_word,
        )
    )
    age = models.IntegerField(
        blank=True,
        validators=(
            MinValueValidator(0),
            MaxValueValidator(130),
        )
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        blank=True,
        default='A'
    )
    image = models.ImageField(max_length=255, upload_to='public/rx')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age}'



class OnHold(models.Model):
    comment = models.CharField(max_length=160, blank=True)
    rx = models.ForeignKey(Rx, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.created}'


# class Prepeared(models.Model):
#     comment = models.CharField(max_length=160, blank=True)
#     rx = models.ForeignKey(Rx, on_delete=models.CASCADE)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.user} {self.created}'
