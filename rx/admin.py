from django.contrib import admin

# Register your models here.
from rx.models import Rx, OnHold

admin.site.register(Rx)
admin.site.register(OnHold)