# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 14:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogsPost',
            new_name='BlogPost',
        ),
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ('-timestamp',)},
        ),
    ]
