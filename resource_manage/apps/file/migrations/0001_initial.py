# Generated by Django 3.2.14 on 2022-08-09 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.CharField(auto_created=True, default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('spare_str1', models.CharField(blank=True, max_length=512, null=True, verbose_name='备用字符串字段1')),
                ('spare_str2', models.CharField(blank=True, max_length=512, null=True, verbose_name='备用字符串字段2')),
                ('spare_str3', models.CharField(blank=True, max_length=512, null=True, verbose_name='备用字符串字段3')),
                ('spare_int1', models.IntegerField(blank=True, null=True, verbose_name='备用int字段1')),
                ('spare_int2', models.IntegerField(blank=True, null=True, verbose_name='备用int字段2')),
                ('spare_int3', models.IntegerField(blank=True, null=True, verbose_name='备用int字段3')),
                ('file_url', models.TextField(blank=True, null=True, verbose_name='文件路径')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='date update')),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_participle', to=settings.AUTH_USER_MODEL, verbose_name='上传文件用户')),
            ],
            options={
                'verbose_name': '文件表',
                'verbose_name_plural': '文件表',
                'db_table': 't_file',
                'ordering': ('-create_time',),
            },
        ),
    ]
