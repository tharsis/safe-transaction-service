# Generated by Django 3.1.7 on 2021-03-08 13:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("history", "0030_auto_20210203_1541"),
    ]

    operations = [
        migrations.AddField(
            model_name="webhook",
            name="new_safe",
            field=models.BooleanField(default=True),
        ),
    ]
