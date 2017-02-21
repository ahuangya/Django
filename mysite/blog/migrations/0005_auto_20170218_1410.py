# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='belong_user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='words',
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='belong_BlogPost',
            field=models.ForeignKey(verbose_name=b'blog', to='blog.BlogPost'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(null=True),
        ),
    ]
