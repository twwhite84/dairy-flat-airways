# Generated by Django 5.0.6 on 2024-05-29 03:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0010_remove_flight_date_remove_flight_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrival_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
