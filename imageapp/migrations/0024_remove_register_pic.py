# Generated by Django 4.2.2 on 2023-07-15 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("imageapp", "0023_register_pic"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="register",
            name="pic",
        ),
    ]
