# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-14 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centralmovies', '0002_auto_20170214_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='plataformGames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plataform', models.CharField(max_length=64)),
            ],
        ),
    ]
