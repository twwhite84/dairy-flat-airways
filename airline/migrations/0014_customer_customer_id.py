# Generated by Django 5.0.6 on 2024-05-31 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0013_airport_customer_plane_booking_route_flight_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_id',
            field=models.IntegerField(default=0),
        ),
    ]
