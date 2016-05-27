# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-22 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=200)),
                ('contactperson', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
