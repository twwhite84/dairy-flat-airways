# Generated by Django 5.0.6 on 2024-06-02 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0021_booking_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='direction',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
