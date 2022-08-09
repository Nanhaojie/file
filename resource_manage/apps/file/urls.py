from django.urls import path

from file.views import FileUpload

urlpatterns = [
    # 文件上传
    path('file_upload', FileUpload.as_view()),

]
