# Generated by Django 5.0.2 on 2024-02-22 01:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("rides", "0002_person_email_person_last_name_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="person",
            old_name="origination",
            new_name="origination_city",
        ),
    ]