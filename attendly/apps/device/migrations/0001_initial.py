# Generated by Django 4.2.6 on 2023-10-09 12:17

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("profiles", "0001_initial"),
        ("college", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RFIDTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tag_uid", models.CharField(max_length=50, unique=True)),
                (
                    "profile",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profiles.userprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RFIDDevice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False, help_text="Used for soft delete"
                    ),
                ),
                ("device_no", models.CharField(max_length=50)),
                (
                    "course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="college.course",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="college.room"
                    ),
                ),
                (
                    "workshop",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="college.workshop",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("all_objects", django.db.models.manager.Manager()),
            ],
        ),
    ]
