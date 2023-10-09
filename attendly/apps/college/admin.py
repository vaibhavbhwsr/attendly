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


admin.site.register(Campus)
admin.site.register(Stream)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Workshop)
admin.site.register(Room)
admin.site.register(Attendance)
