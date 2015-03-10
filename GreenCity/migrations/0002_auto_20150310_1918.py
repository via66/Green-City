# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'GreenCity', b'0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name=b'feature',
            name=b'name',
            field=models.CharField(max_length=250),
        ),
    ]
