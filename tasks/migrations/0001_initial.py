# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 20:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=4000)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('status', models.IntegerField(choices=[('0', 'Pending'), ('1', 'Completed')], default='0')),
                ('create_time', models.DateTimeField()),
                ('deadline', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]