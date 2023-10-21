from django.db import models
from profiles.models import UserProfile
from core.models import BaseModel

# Create your models here.


class RFIDDevice(BaseModel):
    device_no = models.CharField(max_length=50)
    room = models.ForeignKey("college.Room", on_delete=models.CASCADE)
    course = models.ForeignKey(
        "college.Course", on_delete=models.CASCADE, null=True, blank=True
    )
    subject = models.ForeignKey(
        "college.Subject", on_delete=models.CASCADE, null=True, blank=True
    )
    workshop = models.ForeignKey(
        "college.Workshop", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return str(self.device_no)


class RFIDTag(models.Model):
    profile = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, null=True, blank=True
    )
    tag_uid = models.CharField(unique=True, max_length=50, db_index=True)
    registered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.tag_uid)

    def save(self, *args, **kwargs):
        self.checked_registered()
        return super().save(*args, **kwargs)

    def checked_registered(self):
        if self.profile:
            self.registered = True
