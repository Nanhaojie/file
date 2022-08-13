from django.urls import path

from .views import FileUploadView, FileDownloadView, FileExportView,   RemarkView


urlpatterns = [
    # 文件上传
    path('upload/', FileUploadView.as_view(), name='upload'),
    # 文件下载
    path('download/<int:file_id>/', FileDownloadView.as_view(), name='download'),
    # 文件导出
    path('export/', FileExportView.as_view(), name='export'),
    # 文件备注
    path('remark/', RemarkView.as_view())
]
