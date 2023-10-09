from django.contrib import admin
from device.models import RFIDDevice, RFIDTag

# Register your models here.

admin.site.register(RFIDDevice)
admin.site.register(RFIDTag)
