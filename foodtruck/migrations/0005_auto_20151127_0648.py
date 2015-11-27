# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtruck', '0004_auto_20151127_0641'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='foodtruck',
            unique_together=set([('truck_name', 'latitude', 'longitude')]),
        ),
    ]
