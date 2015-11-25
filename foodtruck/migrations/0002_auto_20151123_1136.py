# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtruck', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodTruck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('truck_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('schedule_url', models.CharField(max_length=200)),
                ('operation_hours', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='FoodTrucks',
        ),
    ]
