# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GreenCity', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='park',
            old_name='street_name',
            new_name='streetName',
        ),
        migrations.RenameField(
            model_name='park',
            old_name='street_number',
            new_name='streetNumber',
        ),
    ]
