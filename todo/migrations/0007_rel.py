# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-20 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20170915_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rel', models.CharField(max_length=30)),
            ],
        ),
    ]