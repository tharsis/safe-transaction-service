# Generated by Django 3.1.2 on 2020-10-15 11:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("history", "0024_auto_20201014_1523"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ethereumevent",
            name="arguments",
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name="ethereumtx",
            name="logs",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.JSONField(), default=None, null=True, size=None
            ),
        ),
        migrations.AlterField(
            model_name="internaltxdecoded",
            name="arguments",
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name="multisigtransaction",
            name="failed",
            field=models.BooleanField(db_index=True, default=None, null=True),
        ),
    ]
