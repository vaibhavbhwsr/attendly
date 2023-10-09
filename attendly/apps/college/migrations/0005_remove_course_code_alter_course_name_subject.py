# Generated by Django 4.2.6 on 2023-10-09 12:36

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):
    dependencies = [
        ("college", "0004_alter_room_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="code",
        ),
        migrations.AlterField(
            model_name="course",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.CreateModel(
            name="Subject",
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
                ("code", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=50)),
                ("full_form", models.CharField(max_length=100)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="college.course"
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
