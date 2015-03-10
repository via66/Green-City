# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'GreenCity', b'0003_remove_communitygarden_completeaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name=b'greencityproject',
            name=b'address',
            field=models.CharField(max_length=250),
        ),
    ]
