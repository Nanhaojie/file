# Generated by Django 2.2.3 on 2019-08-20 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190820_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useroperatelog',
            name='content',
            field=models.CharField(max_length=50, verbose_name='操作内容'),
        ),
    ]
