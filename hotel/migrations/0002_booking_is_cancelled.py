# Generated by Django 4.2.6 on 2023-11-03 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_cancelled',
            field=models.BooleanField(default=False),
        ),
    ]