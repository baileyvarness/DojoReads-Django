# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-13 23:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('review', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reviews', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='dojoreads_app.Review')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='reviews',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='dojoreads_app.Review'),
        ),
        migrations.AddField(
            model_name='authors',
            name='books',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='dojoreads_app.Books'),
        ),
    ]
