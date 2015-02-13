# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GreenProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('map_id', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=100)),
                ('cat_1', models.CharField(max_length=50)),
                ('cat_2', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('url_1', models.URLField()),
                ('url_2', models.URLField()),
                ('url_3', models.URLField()),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
