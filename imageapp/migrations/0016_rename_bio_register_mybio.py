# Generated by Django 4.2.2 on 2023-06-30 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("imageapp", "0015_alter_register_bio"),
    ]

    operations = [
        migrations.RenameField(
            model_name="register",
            old_name="bio",
            new_name="mybio",
        ),
    ]
