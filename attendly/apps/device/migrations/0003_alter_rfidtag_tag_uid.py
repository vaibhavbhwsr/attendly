# Generated by Django 4.2.6 on 2023-10-09 18:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("device", "0002_rfiddevice_subject"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rfidtag",
            name="tag_uid",
            field=models.CharField(db_index=True, max_length=50, unique=True),
        ),
    ]
