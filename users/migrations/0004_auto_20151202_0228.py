# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20151202_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fav',
            name='foodtruck',
            field=models.OneToOneField(to='foodtrucks.Foodtruck'),
        ),
    ]
