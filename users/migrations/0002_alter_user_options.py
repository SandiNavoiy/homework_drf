# Generated by Django 4.2.3 on 2023-08-03 19:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "пользователь",
                "verbose_name_plural": "пользователи",
            },
        ),
    ]
