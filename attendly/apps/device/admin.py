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
        import ipdb; ipdb.set_trace()
        return self.attendance_set.count()


admin.site.register(RFIDDevice)
