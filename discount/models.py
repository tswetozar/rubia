from django.db import models


# Create your models here.

class CsvFile(models.Model):
    csv_file = models.FileField(max_length=255, upload_to='private/documents')


class Card(models.Model):
    name = models.CharField(max_length=50, blank=True)
    card_number = models.PositiveBigIntegerField(blank=False)
    rating = models.PositiveIntegerField(default=0, editable=False)
