from django.db import models

# Create your models here.
import uuid
from django.utils.translation import gettext_lazy as _
from utils.models import SpareFieldModel


class FileModel(SpareFieldModel):
    id = models.CharField(max_length=36, primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    file_url = models.TextField(null=True, blank=True, verbose_name="文件路径")
    user = models.ForeignKey('user.AccountModel', null=True, blank=True, on_delete=models.PROTECT,
                             related_name='user_participle', db_constraint=False, verbose_name='上传文件用户')
    create_time = models.DateTimeField(_('date joined'), auto_now_add=True)
    update_time = models.DateTimeField(_('date update'), auto_now=True)

    class Meta:
        verbose_name = '文件表'
        verbose_name_plural = verbose_name
        db_table = 't_file'
        ordering = ('-create_time',)
