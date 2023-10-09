from rest_framework import serializers
from device.models import RFIDDevice


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RFIDDevice
        fields = ("device_no", "room", "course", "subject", "workshop")
