from django.urls import path
from college.apis import views

app_name = "college"

urlpatterns = [
    path("attendance/", views.AttendanceCreateAPIView.as_view(), name="attendance"),
]
