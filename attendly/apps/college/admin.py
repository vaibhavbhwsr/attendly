from django.contrib import admin
from college.models import (
    Campus,
    Stream,
    Course,
    Subject,
    Workshop,
    Room,
    Attendance,
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


admin.site.register(Campus)
admin.site.register(Stream)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Workshop)
admin.site.register(Room)
