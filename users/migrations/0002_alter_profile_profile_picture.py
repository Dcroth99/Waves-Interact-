# Generated by Django 5.0.6 on 2024-06-24 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_picture",
            field=models.ImageField(blank=True, upload_to="profile_pics/"),
        ),
    ]
