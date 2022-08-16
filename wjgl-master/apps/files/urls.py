from django.urls import path

from .views import FileUploadView, FileDownloadView, FileExportView, RemarkView, FilePayView, FileDeleteView, \
    WordPresslistView, FileNeedPayView, FileWordPressDownloadView, FileWordPressPayView

urlpatterns = [
    # 文件上传
    path('upload/', FileUploadView.as_view(), name='upload'),
    # 管理文件下载
    path('download/<int:file_id>/', FileDownloadView.as_view(), name='download'),
    # 文件导出
    path('export/', FileExportView.as_view(), name='export'),
    # 文件备注
    path('remark/', RemarkView.as_view()),
    # 付费
    path('pay/<int:file_id>/', FilePayView.as_view(), name='pay'),
    # 是否需要付费
    path('needpay/<int:file_id>/', FileNeedPayView.as_view(), name='needpay'),
    # 删除
    path('delete/<int:file_id>/', FileDeleteView.as_view(), name='delete'),

    # 分享站
    path('wordpresslist/', WordPresslistView.as_view(), name='wordpresslist'),
    # 发布站文件下载
    path('wordpressdownload/<int:file_id>/', FileWordPressDownloadView.as_view(), name='wordpressdownload'),
    # 付费
    path('wordpresspay/<int:file_id>/', FileWordPressPayView.as_view(), name='wordpresspay'),
]
