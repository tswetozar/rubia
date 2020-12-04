from django.db import models


# Create your models here.

class Rx(models.Model):
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('H', 'On Hold'),
        ('P', 'Prepared'),
        ('R', 'Ready For Pick-up'),
        ('F', 'Finished'),
    )
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    age = models.IntegerField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        blank=True,
        default='A'
    )
    image = models.ImageField(max_length=255, upload_to='public/rx')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age}'


