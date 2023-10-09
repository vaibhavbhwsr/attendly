from django.db import models
from core.models import BaseModel

# Create your models here.


class Campus(BaseModel):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Stream(BaseModel):
    name = models.CharField(max_length=50)
    full_form = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Course(BaseModel):
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    full_form = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Subject(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.IntegerField(default=1)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    full_form = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.full_form})"


class Workshop(BaseModel):
    name = models.CharField(max_length=50)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, null=True, blank=True)
    start_dt = models.DateTimeField()
    end_dt = models.DateTimeField()

    def __str__(self):
        return str(self.name)


class Room(BaseModel):
    name = models.CharField(max_length=50)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    department = models.ForeignKey(
        Stream, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.department} | {self.name}"


class Attendance(BaseModel):
    device = models.ForeignKey("device.RFIDDevice", on_delete=models.CASCADE)
    tag = models.ForeignKey("device.RFIDTag", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, null=True, blank=True
    )
    workshop = models.ForeignKey(
        Workshop, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.tag.profile.name} | {self.room}"
