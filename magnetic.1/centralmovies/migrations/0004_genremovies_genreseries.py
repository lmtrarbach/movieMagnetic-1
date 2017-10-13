# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-14 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centralmovies', '0003_plataformgames'),
    ]

    operations = [
        migrations.CreateModel(
            name='genreMovies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='genreSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=64)),
            ],
        ),
    ]