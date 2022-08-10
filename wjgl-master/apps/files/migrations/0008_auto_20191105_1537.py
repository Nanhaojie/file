# Generated by Django 2.2.3 on 2019-11-05 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0007_auto_20191104_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApproveLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileid', models.IntegerField(verbose_name='文件编号')),
                ('filename', models.CharField(max_length=200, verbose_name='文件名称')),
                ('filepath', models.CharField(max_length=200, verbose_name='文件路径')),
                ('owner', models.CharField(max_length=200, verbose_name='文件所属用户')),
                ('add_time', models.DateTimeField(verbose_name='上传时间')),
                ('is_approve', models.CharField(choices=[('2', '已驳回'), ('1', '已审批')], max_length=1, verbose_name='终审')),
                ('approve_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='审批时间')),
            ],
            options={
                'verbose_name': '文件审批日志',
                'verbose_name_plural': '文件审批日志',
            },
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='is_approve',
            field=models.CharField(blank=True, choices=[('2', '已驳回'), ('1', '已审批'), ('0', '未审批')], default='0', max_length=1, verbose_name='终审'),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='is_check',
            field=models.CharField(blank=True, choices=[('1', '已审批'), ('0', '未审批')], default='0', max_length=1, verbose_name='初审'),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='is_confirm',
            field=models.CharField(blank=True, choices=[('1', '已审批'), ('0', '未审批')], default='0', max_length=1, verbose_name='二审'),
        ),
    ]
