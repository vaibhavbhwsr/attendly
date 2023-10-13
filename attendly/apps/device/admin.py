from django.contrib import admin
from device.models import RFIDDevice, RFIDTag

# Register your models here.


@admin.register(RFIDTag)
class RFIDTagAdmin(admin.ModelAdmin):
    """
    Admin View for RFIDTag
    """

    list_display = ("tag_uid", "profile", "overall_attends")
    list_filter = ("attendance__subject",)
    search_fields = ('profile__name', 'profile__enroll_no')

    @admin.display(ordering="attends", description="Overall Attendance")
    def overall_attends(self, obj):
        return obj.attendance_set.count()


admin.site.register(RFIDDevice)
