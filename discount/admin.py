from django.contrib import admin

# Register your models here.
from discount.models import CsvFile, Card

admin.site.register(CsvFile)
admin.site.register(Card)
