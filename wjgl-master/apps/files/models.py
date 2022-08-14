from datetime import datetime

from django.db import models


# 文件model
class File(models.Model):
    fileno = models.CharField(max_length=18, verbose_name='文件编号')
    filename = models.CharField(max_length=200, verbose_name='文件名称')
    filepath = models.CharField(max_length=200, verbose_name='文件路径')
    owner = models.CharField(max_length=30, verbose_name='文件所属用户')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='上传时间')
    first_check = models.CharField(max_length=1, choices=(('0', '未付费'), ('1', '付费')), verbose_name='是否付费', default='0')
    second_check = models.CharField(max_length=1, choices=(('0', '删除'), ('1', '已删除')), verbose_name='删除', default='0')
    isapprove = models.CharField(max_length=1, choices=(('0', '未审批'), ('1', '已审批'), ('2', '已驳回')), verbose_name='终审', default='0')
    remark = models.CharField(max_length=256, null=True, blank=True, verbose_name='文件备注')

    class Meta:
        verbose_name = '文件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.filename
