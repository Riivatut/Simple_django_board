# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BoardApp', '0002_auto_20161011_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
    ]