# Generated by Django 5.0 on 2023-12-16 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("creators", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="content_set",
                related_query_name="content",
                to="creators.creator",
            ),
        ),
    ]
