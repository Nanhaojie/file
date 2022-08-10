# Generated by Django 2.2.3 on 2019-10-28 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_auto_20191025_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhiteList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('white_name', models.CharField(blank=True, max_length=300, verbose_name='白名单')),
                ('host_ip', models.CharField(blank=True, max_length=300, verbose_name='公用电脑ip')),
            ],
            options={
                'verbose_name': '白名单',
                'verbose_name_plural': '白名单',
            },
        ),
        migrations.DeleteModel(
            name='WhiteName',
        ),
    ]
