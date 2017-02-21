# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170218_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='body',
            new_name='content',
        ),
    ]
