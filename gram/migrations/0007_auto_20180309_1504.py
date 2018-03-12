# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-09 12:04
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gram', '0006_auto_20180305_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='editor',
            name='user_name',
            field=models.CharField(max_length=30, verbose_name=django.contrib.auth.models.User),
        ),
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=tinymce.models.HTMLField(),
        ),
    ]
