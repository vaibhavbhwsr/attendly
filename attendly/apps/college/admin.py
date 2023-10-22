from django.contrib import admin

from college.models import (
    Attendance,
    AttendanceInsight,
    Campus,
    Course,
    Room,
    Stream,
    Subject,
    Workshop,
)

# Register your models here.


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    """
    Admin View for Attendance
    """

    list_display = ("__str__", "subject", "workshop")
    list_filter = ("tag", "subject", "room", "workshop")
    search_fields = ("tag__profile__name",)


@admin.register(AttendanceInsight)
class AttendanceInsightView(admin.ModelAdmin):
    """
    Admin View for Attendance analysis.
    """

    list_display = ("name", "enroll_no", "course", "overall_attends")
    list_filter = (
        "course",
        "course__stream",
        "rfidtag__attendance__subject__name",
        "created_at",
    )
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ("name", "enroll_no")

    @admin.display(description="Overall Attendance")
    def overall_attends(self, obj):
        return obj.rfidtag.overall_attends()


admin.site.register(Campus)
admin.site.register(Stream)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Workshop)
admin.site.register(Room)
