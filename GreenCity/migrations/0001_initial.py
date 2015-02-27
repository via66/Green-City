# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodMarkets',
            fields=[
                ('feature_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='GreenCity.Feature')),
                ('year', models.IntegerField()),
                ('market_type', models.CharField(max_length=100)),
                ('operator', models.CharField(max_length=50)),
                ('street_num', models.CharField(max_length=10)),
                ('street_dir', models.CharField(max_length=10)),
                ('street_name', models.CharField(max_length=10)),
                ('street_type', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=50)),
                ('market_dir', models.CharField(max_length=10)),
                ('website', models.URLField()),
                ('day', models.CharField(max_length=10)),
                ('open', models.CharField(max_length=5)),
                ('close', models.CharField(max_length=5)),
                ('months', models.CharField(max_length=20)),
                ('num_vendors', models.IntegerField()),
                ('offerings', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=('GreenCity.feature',),
        ),
        migrations.CreateModel(
            name='GreenProject',
            fields=[
                ('feature_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='GreenCity.Feature')),
                ('map_id', models.CharField(max_length=6)),
                ('cat_1', models.CharField(max_length=50)),
                ('cat_2', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('url_1', models.URLField()),
                ('url_2', models.URLField()),
                ('url_3', models.URLField()),
            ],
            options={
            },
            bases=('GreenCity.feature',),
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('feature_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='GreenCity.Feature')),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=('GreenCity.feature',),
        ),
    ]
