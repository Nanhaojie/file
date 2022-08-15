# Generated by Django 2.2.3 on 2022-08-15 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileno', models.CharField(max_length=18, verbose_name='文件编号')),
                ('filename', models.CharField(max_length=200, verbose_name='文件名称')),
                ('filepath', models.CharField(max_length=200, verbose_name='文件路径')),
                ('owner', models.CharField(max_length=30, verbose_name='文件所属用户')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='上传时间')),
                ('first_check', models.CharField(choices=[('0', '未付费'), ('1', '已付费'), ('2', '不需要付费')], default='0', max_length=1, verbose_name='是否付费')),
                ('second_check', models.CharField(choices=[('0', '删除'), ('1', '已删除')], default='0', max_length=1, verbose_name='删除')),
                ('isapprove', models.CharField(choices=[('0', '需要付费'), ('1', '不需要付费')], default='0', max_length=1, verbose_name='是否需要付费')),
                ('remark', models.CharField(blank=True, max_length=256, null=True, verbose_name='文件备注')),
            ],
            options={
                'verbose_name': '文件',
                'verbose_name_plural': '文件',
            },
        ),
    ]
