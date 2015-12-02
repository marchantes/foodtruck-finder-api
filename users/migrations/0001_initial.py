# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('foodtrucks', '0004_auto_20151128_0148'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fav',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('foodtruck', models.ForeignKey(to='foodtrucks.Foodtruck')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1)),
            ],
        ),
    ]
