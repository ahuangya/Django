# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170218_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='belong_BlogPost',
            new_name='blog',
        ),
    ]
