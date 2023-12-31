from django.contrib import admin
from device.models import RFIDDevice, RFIDTag

# Register your models here.


@admin.register(RFIDTag)
class RFIDTagAdmin(admin.ModelAdmin):
    """
    Admin View for RFIDTag
    """

    list_display = ("tag_uid", "profile", "overall_attends", "registered")
    list_filter = ("attendance__subject", "registered")
    search_fields = ('profile__name', 'profile__enroll_no')


admin.site.register(RFIDDevice)
