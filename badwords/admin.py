from django.contrib import admin

# Register your models here.
from badwords.models import BadWord

admin.site.register(BadWord)
