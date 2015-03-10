# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'GreenCity', b'0002_auto_20150310_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name=b'communitygarden',
            name='completeAddress',
        ),
    ]
