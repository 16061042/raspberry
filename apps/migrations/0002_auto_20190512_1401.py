# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-12 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='设备id')),
                ('device_name', models.CharField(max_length=20, verbose_name='设备')),
                ('status', models.IntegerField(default=0, verbose_name='状态')),
                ('arg_type', models.IntegerField(default=0, verbose_name='参数类型')),
                ('arg', models.FloatField(default=0, verbose_name='参数值')),
            ],
            options={
                'verbose_name': '设备',
                'verbose_name_plural': '设备',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=20, verbose_name='房间名称')),
            ],
            options={
                'verbose_name': '房间',
                'verbose_name_plural': '房间',
            },
        ),
        migrations.CreateModel(
            name='RoomDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField(verbose_name='房间id')),
                ('device_id', models.IntegerField(verbose_name='设备id')),
            ],
            options={
                'verbose_name': '房间设备分配表',
                'verbose_name_plural': '房间设备分配表',
            },
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scene_name', models.CharField(max_length=20, verbose_name='场景名称')),
                ('status', models.IntegerField(default=0, verbose_name='状态')),
            ],
            options={
                'verbose_name': '场景',
                'verbose_name_plural': '场景',
            },
        ),
        migrations.DeleteModel(
            name='info',
        ),
    ]