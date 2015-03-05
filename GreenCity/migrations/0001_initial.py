# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BikeRack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('streetNumber', models.CharField(max_length=250)),
                ('streetName', models.CharField(max_length=250)),
                ('numberOfRacks', models.IntegerField()),
                ('longitude', models.DecimalField(max_digits=18, decimal_places=15)),
                ('latitude', models.DecimalField(max_digits=18, decimal_places=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CommunityFoodMarket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('year', models.DateField()),
                ('marketType', models.CharField(max_length=250)),
                ('operator', models.CharField(max_length=250)),
                ('streetNumber', models.CharField(max_length=250)),
                ('streetName', models.CharField(max_length=250)),
                ('url', models.URLField()),
                ('day', models.CharField(max_length=10)),
                ('openHours', models.TimeField()),
                ('closeHours', models.TimeField()),
                ('monthsOfOperations', models.CharField(max_length=250)),
                ('numberOfVendors', models.IntegerField()),
                ('offerings', models.CharField(max_length=250)),
                ('longitude', models.DecimalField(max_digits=18, decimal_places=15)),
                ('latitude', models.DecimalField(max_digits=18, decimal_places=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CommunityGarden',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('streetNumber', models.CharField(max_length=10)),
                ('streetName', models.CharField(max_length=250)),
                ('longitude', models.DecimalField(max_digits=18, decimal_places=15)),
                ('latitude', models.DecimalField(max_digits=18, decimal_places=15)),
                ('numberOfPlots', models.IntegerField()),
                ('numberOfFoodTrees', models.IntegerField()),
                ('foodTreeVarieties', models.CharField(max_length=250)),
                ('jurisdiction', models.CharField(max_length=250)),
                ('stewarsOrManagingOrganization', models.CharField(max_length=250)),
                ('publicEmail', models.EmailField(max_length=75)),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ElectricVehicleChargingStation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('longitude', models.DecimalField(max_digits=18, decimal_places=15)),
                ('latitude', models.DecimalField(max_digits=18, decimal_places=15)),
                ('lotOperator', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GreenCityProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('category1', models.CharField(max_length=250)),
                ('category2', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('shortDescription', models.TextField()),
                ('url1', models.URLField()),
                ('url2', models.URLField()),
                ('url3', models.URLField()),
                ('longitude', models.DecimalField(max_digits=18, decimal_places=15)),
                ('latitude', models.DecimalField(max_digits=18, decimal_places=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('street_number', models.CharField(max_length=250)),
                ('street_name', models.CharField(max_length=250)),
                ('longitude', models.DecimalField(max_digits=18, decimal_places=15)),
                ('latitude', models.DecimalField(max_digits=18, decimal_places=15)),
                ('hectare', models.DecimalField(max_digits=6, decimal_places=2)),
                ('neighbourhoodName', models.CharField(max_length=250)),
                ('neighbourhoodURL', models.URLField()),
                ('url', models.URLField()),
                ('washrooms', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
