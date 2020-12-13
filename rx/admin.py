from django.contrib import admin

# Register your models here.
from rx.models import Rx, OnHold, Prepared, Ready, Finished

admin.site.register(Rx)
admin.site.register(OnHold)
admin.site.register(Prepared)
admin.site.register(Ready)
admin.site.register(Finished)
