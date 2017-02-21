# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('words', models.CharField(max_length=200)),
                ('created', models.DateTimeField()),
                ('belong_BlogPost', models.ForeignKey(related_name='blog', to='blog.BlogPost')),
                ('belong_user', models.ForeignKey(related_name='user', to='blog.User')),
            ],
        ),
    ]
