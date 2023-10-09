# Generated by Django 4.2.6 on 2023-10-09 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("college", "0007_remove_attendance_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="attendance",
            name="subject",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="college.subject",
            ),
        ),
    ]