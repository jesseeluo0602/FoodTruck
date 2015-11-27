# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtruck', '0003_auto_20151127_0634'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='foodtruck',
            unique_together=set([]),
        ),
    ]
