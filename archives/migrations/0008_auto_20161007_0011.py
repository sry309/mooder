# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 16:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0007_auto_20161006_0057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_time'], 'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archives.Comment', verbose_name='父评论'),
        ),
    ]