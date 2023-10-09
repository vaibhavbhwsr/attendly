from college.models import Attendance
from rest_framework import serializers


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ("device", "tag", "room", "course", "subject", "workshop")
