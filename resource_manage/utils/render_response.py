# !usr/bin/env python
# -*- coding:utf-8 -*-
# create in 2021/5/14
# @author fj
import logging

from rest_framework.renderers import JSONRenderer

logger = logging.getLogger('django')


class CustomJsonRenderer(JSONRenderer):
    # 重构render方法
    def render(self, data, accepted_media_type=None, renderer_context=None):
        ret = None
        code = None
        if renderer_context:
            # 判断是否返回原始数据
            if renderer_context["response"].headers.get("OriginalResponse") == "true":
                return super(CustomJsonRenderer, self).render(data, accepted_media_type, renderer_context)
            # 如果返回的data为字典
            if isinstance(data, dict):
                # 响应信息中有detail和code这两个key，则获取响应信息中的detail和code，并且将原本data中的这两个key删除，放在自定义响应信息里
                # 响应信息中没有则将msg内容改为请求成功 code改为请求的状态码
                msg = data.pop('detail', '成功')

                # 判断msg如果为dict,将任意一个key,value对组装为 str
                if isinstance(msg, dict):
                    try:
                        field, errorDetail = msg.popitem()
                        errorDetail = str(errorDetail[0])
                        if errorDetail.startswith('该字段'):
                            msg = f"{field}{errorDetail.strip('该')}"
                        elif errorDetail.startswith('请确保这个字段'):
                            msg = f"{field}{errorDetail.strip('请确保这个')}"
                        else:
                            msg = errorDetail
                    except Exception:
                        logger.warning('处理msg异常', exc_info=True)
                        msg = '参数校验失败'

                code = renderer_context["response"].status_code
            # 如果不是字典则将msg内容改为请求成功 code改为请求的状态码
            else:
                msg = '成功'
                code = renderer_context["response"].status_code
            renderer_context["response"].status_code = 200
            # 自定义返回的格式
            ret = {
                'msg': msg,
                'code': code,
                'data': data,
            }
            # 返回JSON数据
            response_data = super(CustomJsonRenderer, self).render(ret, accepted_media_type, renderer_context)
        else:
            response_data = super(CustomJsonRenderer, self).render(data, accepted_media_type, renderer_context)

        # 添加统一请求日志
        response = renderer_context["response"]
        request = renderer_context["request"]
        try:
            logger_info = f'{request.method} {request.path} [params:{dict(request.query_params)}] [code:{code or response.status_code}] [account_id:{request.user.id}] [request_body:{dict(request.data)}] [file:{dict(request.FILES)}] [response_data:{dict(ret or data)}] [Authorization:{request.headers.get("Authorization")}] [header:{dict(request.headers)}]'[:5000]
        except Exception:
            logger.warning('请求信息打印失败', exc_info=True)
            logger_info = ''
        logger.info(logger_info)

        return response_data
