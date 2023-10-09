from django.db import models
from core.models import BaseModel

# Create your models here.


class UserProfile(BaseModel):
    name = models.CharField(max_length=100)
    enroll_no = models.CharField(unique=True, max_length=15)
    email = models.EmailField(null=True, blank=True)
    mobile_no = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.enroll_no} | {self.name}"
