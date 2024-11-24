# Generated by Django 5.0.6 on 2024-05-29 03:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0007_delete_flight'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='seats',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='route',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='plane',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(choices=[('O', 'Outbound'), ('I', 'Inbound')], max_length=1)),
                ('seats_available', models.IntegerField(default=0)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airline.route')),
            ],
        ),
    ]