# Generated by Django 4.2.6 on 2023-11-18 10:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hotel", "0006_hotel_on_main"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guest_reviews",
            name="email",
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
