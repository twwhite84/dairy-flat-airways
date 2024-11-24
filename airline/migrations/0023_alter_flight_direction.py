# Generated by Django 5.0.6 on 2024-06-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0022_flight_direction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='direction',
            field=models.CharField(choices=[('O', 'Outbound'), ('I', 'Inbound')], max_length=1, null=True),
        ),
    ]