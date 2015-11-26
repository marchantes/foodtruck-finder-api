# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtrucks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtruck',
            name='city',
            field=models.CharField(max_length=50, default='Mexico City'),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='photo',
            field=models.ImageField(upload_to='img/foodtrucks/'),
        ),
    ]
