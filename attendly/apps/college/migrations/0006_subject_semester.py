# Generated by Django 4.2.6 on 2023-10-09 12:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("college", "0005_remove_course_code_alter_course_name_subject"),
    ]

    operations = [
        migrations.AddField(
            model_name="subject",
            name="semester",
            field=models.IntegerField(default=1),
        ),
    ]
