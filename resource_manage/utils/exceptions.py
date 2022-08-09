# !usr/bin/env python
# -*- coding:utf-8 -*-
# create in 2021/4/19
# @author fj
import logging

import requests
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
from rest_framework import status, serializers

from django.db import DatabaseError
from redis.exceptions import RedisError

# 获取在配置文件中定义的logger，用来记录日志
logger = logging.getLogger('django')


def exception_handler(exc, context):
    """
    自定义异常处理
    :param exc: 异常信息
    :param context: 抛出异常的上下文
    :return: Response响应对象
    """
    # 调用drf框架原生的异常处理方法
    response = drf_exception_handler(exc, context)
    # 获取视图对象
    view = context['view']
    logger.error('[%s]:%s' % (view, type(exc)), exc_info=True)
    if not response:
        if isinstance(exc, requests.exceptions.ReadTimeout):
            return Response({'detail': '文件准备超时'}, status=status.HTTP_503_SERVICE_UNAVAILABLE, exception=True)
        elif isinstance(exc, DatabaseError) or isinstance(exc, RedisError):
            return Response({'detail': '服务异常'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
        return Response({'detail': f'服务异常: {exc}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=True)

    try:
        if isinstance(exc, serializers.ValidationError):
            field, errorDetail = exc.detail.popitem()
            errorDetail = str(errorDetail[0])
            if errorDetail.startswith('该字段'):
                exc = f"{field}{errorDetail.strip('该')}"
            elif errorDetail.startswith('请确保这个字段'):
                exc = f"{field}{errorDetail.strip('请确保这个')}"
            else:
                exc = errorDetail
    except Exception:
        logger.warning('获取detail信息失败', exc_info=True)

    return Response({'detail': str(exc)}, status=response.status_code)
