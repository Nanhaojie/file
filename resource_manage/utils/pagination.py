# !usr/bin/env python
# -*- coding:utf-8 -*-
# create in 2021/4/19
# @author fj
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.pagination import PageNumberPagination
from django.utils.translation import gettext_lazy as _


class ConsumerPaginator(Paginator):
    def validate_number(self, number):
        """Validate the given 1-based page number."""
        try:
            if isinstance(number, float) and not number.is_integer():
                raise ValueError
            number = int(number)
        except (TypeError, ValueError):
            raise PageNotAnInteger(_('That page number is not an integer'))
        if number < 1:
            raise EmptyPage(_('That page number is less than 1'))
        return number


class StandardResultPagination(PageNumberPagination):
    """自定义分页类"""
    # 分页默认页容量
    page_size = 50
    # 获取分页数据时，传递页容量参数名称
    page_size_query_param = 'page_size'
    # 最大页容量
    max_page_size = 100
    django_paginator_class = ConsumerPaginator
