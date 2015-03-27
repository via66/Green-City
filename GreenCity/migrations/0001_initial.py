# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
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
            name='FacebookUserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('about_me', models.TextField(null=True, blank=True)),
                ('facebook_id', models.BigIntegerField(unique=True, null=True, blank=True)),
                ('access_token', models.TextField(help_text='Facebook token for offline access', null=True, blank=True)),
                ('facebook_name', models.CharField(max_length=255, null=True, blank=True)),
                ('facebook_profile_url', models.TextField(null=True, blank=True)),
                ('website_url', models.TextField(null=True, blank=True)),
                ('blog_url', models.TextField(null=True, blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True, choices=[('m', 'Male'), ('f', 'Female')])),
                ('raw_data', models.TextField(null=True, blank=True)),
                ('facebook_open_graph', models.NullBooleanField(help_text='Determines if this user want to share via open graph')),
                ('new_token_required', models.BooleanField(default=False, help_text='Set to true if the access token is outdated or lacks permissions')),
                ('image', models.ImageField(max_length=255, null=True, upload_to='images/facebook_profiles/%Y/%m/%d', blank=True)),
            ],
            options={
                'abstract': False,
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
            name='GreenCityUserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website', models.URLField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
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
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'swappable': 'AUTH_USER_MODEL',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='greencityuserprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='facebookuserprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='bikerack',
            unique_together=set([('streetSide', 'streetNumber', 'streetName')]),
        ),
    ]
