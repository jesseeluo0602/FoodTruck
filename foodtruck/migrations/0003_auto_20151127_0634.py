# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtruck', '0002_auto_20151123_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodtruck',
            name='food_items',
            field=models.CharField(default='no', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='foodtruck',
            unique_together=set([('truck_name', 'latitude', 'longitude')]),
        ),
    ]
