from rest_framework.generics import CreateAPIView

from college.apis.serializers import AttendanceSerializer
from device.apis.serializers import DeviceSerializer
from device.models import RFIDDevice, RFIDTag


class AttendanceCreateAPIView(CreateAPIView):
    serializer_class = AttendanceSerializer

    def create(self, request, *args, **kwargs):
        device = RFIDDevice.objects.get(device_no=request.data.get("device"))
        tag, created = RFIDTag.objects.get_or_create(tag_uid=request.data.get("tag"))

        request.data.update(tag=tag.id, **DeviceSerializer(device).data)
        request.data["device"] = device.id

        return super().create(request, *args, **kwargs)
