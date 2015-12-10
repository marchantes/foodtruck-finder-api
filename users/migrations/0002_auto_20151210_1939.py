# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fav',
            name='foodtruck',
            field=models.ForeignKey(to='foodtrucks.Foodtruck'),
        ),
        migrations.AlterUniqueTogether(
            name='fav',
            unique_together=set([('user', 'foodtruck')]),
        ),
    ]
