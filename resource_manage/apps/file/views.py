import hashlib
import os

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.
from resource_manage.settings import FILE_PATH, FS_SERVER
from rest_framework.response import Response
from rest_framework import status


class FileUpload(APIView):
    # permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        # 接口描述，支持markdown语法
        operation_description="""文件上传""",
        # manual_parameters=[
        #     openapi.Parameter(name="Authorization", in_=openapi.IN_HEADER, description="token",
        #                       type=openapi.TYPE_STRING)
        # ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'file': openapi.Schema(type=openapi.TYPE_FILE, description='文件')
            }
        ),
        # 接口标题
        operation_summary='文件上传',
        # 接口所属分组，会单独将接口拆出来放到 用户管理 分组中
        tags=['文件管理']
    )
    def post(self, request, *args, **kwargs):
        file = request.data['file']
        file_data = file.read()
        sha1 = hashlib.sha1()
        sha1.update(file_data)
        file_name = sha1.hexdigest()
        file_storage_abs_path = FILE_PATH + file_name
        # 如果路径不存在
        if not os.path.exists(FILE_PATH):
            os.makedirs(FILE_PATH)
        # 查询文件是否存在
        if not os.path.exists(file_storage_abs_path):
            # 不存在，保存后返回链接
            with open(file_storage_abs_path, 'wb') as f:
                f.write(file_data)
        return Response(data={'data': FS_SERVER + file_name}, status=status.HTTP_200_OK)
