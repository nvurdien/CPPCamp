# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 21:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fill_in',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='lesson_num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fill_in',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.Question'),
        ),
    ]
