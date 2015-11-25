# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodTrucks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('truck_name', models.CharField(max_length=200)),
                ('facility_type', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('schedule_url', models.CharField(max_length=200)),
                ('days_hours', models.CharField(max_length=200)),
            ],
        ),
    ]
