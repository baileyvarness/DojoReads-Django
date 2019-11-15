# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-13 23:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojoreads_app', '0002_auto_20191113_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authors',
            name='books',
        ),
        migrations.RemoveField(
            model_name='books',
            name='reviews',
        ),
        migrations.AddField(
            model_name='books',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='dojoreads_app.Authors'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='book',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='dojoreads_app.Books'),
            preserve_default=False,
        ),
    ]