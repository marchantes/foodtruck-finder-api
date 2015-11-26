# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foodtrucks', '0002_auto_20151126_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=255)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('likes', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='photo',
            field=models.ImageField(upload_to='img/foodtrucks/', blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='foodtruck',
            field=models.ForeignKey(to='foodtrucks.Foodtruck'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
        ),
    ]
