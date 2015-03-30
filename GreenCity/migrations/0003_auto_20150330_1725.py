# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GreenCity', '0002_feature_keywords'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='greencityuserprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='GreenCityUserProfile',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='keywords',
        ),
    ]
