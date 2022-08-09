# !usr/bin/env python
# -*- coding:utf-8 -*-
# create in 2021/4/19
# @author nhj
from django.db import models


class BaseModel(models.Model):
    """为模型类补充字段"""
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        # 说明是抽象模型类，数据库迁移时不会生成表
        abstract = True


class SpareFieldModel(models.Model):
    """为模型类补充备用字段"""
    spare_str1 = models.CharField(max_length=512, null=True, blank=True, verbose_name='备用字符串字段1')
    spare_str2 = models.CharField(max_length=512, null=True, blank=True, verbose_name='备用字符串字段2')
    spare_str3 = models.CharField(max_length=512, null=True, blank=True, verbose_name='备用字符串字段3')
    spare_int1 = models.IntegerField(null=True, blank=True, verbose_name='备用int字段1')
    spare_int2 = models.IntegerField(null=True, blank=True, verbose_name='备用int字段2')
    spare_int3 = models.IntegerField(null=True, blank=True, verbose_name='备用int字段3')

    class Meta:
        # 说明是抽象模型类，数据库迁移时不会生成表
        abstract = True
