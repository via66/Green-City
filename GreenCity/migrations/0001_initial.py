# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'auth', b'__first__'),
        (b'contenttypes', b'__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatasetLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url_title', models.CharField(max_length=200)),
                ('url_link', models.URLField(unique=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ElectricVehicleChargingStation',
            fields=[
                ('feature_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='GreenCity.Feature')),
                ('lotOperator', models.CharField(max_length=250)),
                ('address', models.CharField(unique=True, max_length=250)),
            ],
            options={
            },
            bases=('GreenCity.feature',),
        ),
        migrations.CreateModel(
            name='CommunityGarden',
            fields=[
                ('feature_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='GreenCity.Feature')),
                ('streetNumber', models.CharField(max_length=10, null=True, blank=True)),
                ('streetName', models.CharField(max_length=250, null=True, blank=True)),
                ('numberOfPlots', models.IntegerField(null=True, blank=True)),
                ('numberOfFoodTrees', models.IntegerField(null=True, blank=True)),
                ('foodTreeVarieties', models.CharField(max_length=250, null=True, blank=True)),
                ('jurisdiction', models.CharField(max_length=250, null=True, blank=True)),
                ('stewarsOrManagingOrganization', models.CharField(max_length=250, null=True, blank=True)),
                ('publicEmail', models.EmailField(max_length=75, null=True, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
            ],
            options={
            },
            bases=('GreenCity.feature',),
        ),
        migrations.CreateModel(
            name='CommunityFoodMarket',
            fields=[
                ('feature_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='GreenCity.Feature')),
                ('year', models.CharField(max_length=10)),
                ('marketType', models.CharField(max_length=250)),
                ('operator', models.CharField(max_length=250)),
                ('streetNumber', models.CharField(max_length=250)),
                ('streetName', models.CharField(max_length=250)),
                ('url', models.URLField()),
                ('day', models.CharField(max_length=10)),
                ('openHours', models.CharField(max_length=10)),
                ('closeHours', models.CharField(max_length=10)),
                ('monthsOfOperations', models.CharField(max_length=250)),
                ('numberOfVendors', models.CharField(max_length=250)),
                ('offerings', models.CharField(max_length=250)),
                ('completeAddress', models.CharField(unique=True, max_length=250)),
            ],
            options={
            },
            bases=('GreenCity.feature',),
        ),
        migrations.CreateModel(
            name='BikeRack',
            fields=[
                ('feature_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='GreenCity.Feature')),
                ('streetNumber', models.CharField(max_length=250)),
                ('streetName', models.CharField(max_length=250)),
                ('streetSide', models.CharField(max_length=250)),
                ('numberOfRacks', models.IntegerField()),
                ('completeAddress', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=('GreenCity.feature',),
        ),
        migrations.CreateModel(
            name='GreenCityProject',
            fields=[
                ('feature_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='GreenCity.Feature')),
                ('category1', models.CharField(max_length=250)),
                ('category2', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('shortDescription', models.TextField()),
                ('url1', models.URLField()),
                ('url2', models.URLField()),
                ('url3', models.URLField()),
            ],
            options={
            },
            bases=('GreenCity.feature',),
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('feature_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='GreenCity.Feature')),
                ('streetNumber', models.CharField(max_length=250)),
                ('streetName', models.CharField(max_length=250)),
                ('hectare', models.DecimalField(max_digits=6, decimal_places=2)),
                ('neighbourhoodName', models.CharField(max_length=250)),
                ('neighbourhoodURL', models.URLField()),
                ('washrooms', models.BooleanField(default=False)),
                ('completeAddress', models.CharField(unique=True, max_length=250)),
            ],
            options={
            },
            bases=('GreenCity.feature',),
        ),
        migrations.AlterUniqueTogether(
            name='bikerack',
            unique_together=set([('streetSide', 'streetNumber', 'streetName')]),
        ),
    ]
