# Generated by Django 4.2.3 on 2023-08-16 21:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Course", "0003_course_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="last_updated",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="последнее обновление"
            ),
        ),
    ]
