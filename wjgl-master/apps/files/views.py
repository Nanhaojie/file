import csv
import os
import datetime

from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.http import FileResponse
from django.utils.http import urlquote
from django.db.models import Q
from pure_pagination import Paginator, PageNotAnInteger
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import File
from wjgl.settings import per_page, root_path
from utils.mixin_utils import LoginRequiredMixin


# 首页(文件列表)
class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get('search')
        if search:
            search = search.strip()
            if request.user.role == '3' or request.user.is_superuser == 1:
                files = File.objects.filter(Q(fileno__icontains=search) | Q(filename__icontains=search)
                                            | Q(owner__icontains=search)).order_by('-add_time')
            else:
                files = File.objects.filter(Q(fileno__icontains=search) | Q(filename__icontains=search),
                                            owner=request.user.username).order_by( '-add_time')
        else:
            if request.user.role == '3' or request.user.is_superuser == 1:
                files = File.objects.all().order_by('-add_time')
            else:
                files = File.objects.filter(owner=request.user.username).order_by('-add_time')

        # 分页功能实现
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(files, per_page=per_page, request=request)
        p_contents = p.page(page)
        start = (int(page)-1) * per_page  # 避免分页后每行数据序号从1开始

        return render(request, 'files/index.html', {'p_contents': p_contents, 'start': start, 'search': search})


# 文件上传
class FileUploadView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'files/file_upload.html', {})

    def post(self, request):
        my_file = request.FILES.get('myfile', None)
        if not my_file:
            return render(request, 'files/file_upload.html', {'msg': '没有选择文件'})
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().month)
        day = str(datetime.datetime.now().day)
        username = request.user.username.upper()
        upload_path = os.path.join(root_path, username, year, month, day)
        if os.path.isfile(os.path.join(upload_path, my_file.name)):
            return render(request, 'files/file_upload.html', {'msg': my_file.name + '已存在'})
        if not os.path.exists(upload_path):
            os.makedirs(upload_path)
        with open(os.path.join(upload_path, my_file.name), 'wb+') as f:
            for chunk in my_file.chunks():
                f.write(chunk)

        # 将上传记录插入到文件表中
        records = File()
        records.fileno = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'))[:17]  # 时间精确到0.001s，用作文件的编号
        records.filename = my_file.name
        records.filepath = upload_path
        records.owner = username
        records.save()
        return HttpResponseRedirect((reverse('index')))


# 文件下载
class FileDownloadView(LoginRequiredMixin, View):
    def get(self, request, file_id):
        file = File.objects.get(id=file_id)
        if (request.user.username.upper() != file.owner.upper() and request.user.role != '3' and request.user.is_superuser != 1):
            return HttpResponse(status=404)
        filename = file.filename
        filepath = file.filepath
        if not os.path.isfile(os.path.join(filepath, filename)):
            return render(request, 'files/file_download_error.html', {'msg': '文件可能已经被删除，请联系管理员~'})
        # 文件管理下载不需要收费
        # file_pay = file.first_check
        # if file_pay == '0' or file_pay == 0:
        #     return render(request, 'files/file_download_error.html', {'msg': '文件未付费，请先付费~'})
        download_file = open(os.path.join(filepath, filename), 'rb')
        response = FileResponse(download_file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename=' + urlquote(filename)
        return response


# 文件列表导出
class FileExportView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.role != '3' and request.user.is_superuser != 1:
            return HttpResponse(status=404)
        search = request.GET.get('search')
        if search:
            search = request.GET.get('search').strip()
            files = File.objects.filter(Q(fileno__icontains=search) | Q(filename__icontains=search)
                                        | Q(owner__icontains=search)).order_by('-add_time')
        else:
            files = File.objects.all().order_by('-add_time')

        files = files.values('fileno', 'filename', 'filepath', 'owner', 'add_time')
        colnames = ['文件编号', '文件名', '文件路径', '上传用户', '上传时间']
        response = create_excel(colnames, files, 'wjgl')
        return response


def create_excel(columns, content, filename):
    """创建导出csv的函数"""
    filename = filename + '.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + filename
    response.charset = 'gbk'
    writer = csv.writer(response)
    writer.writerow(columns)
    for i in content:
        writer.writerow([i['fileno'], i['filename'], i['filepath'], i['owner'], i['add_time'].strftime( '%Y/%m/%d %H:%M:%S')])
    return response


# 修改备注
class RemarkView(APIView):
    def post(self, request):
        remark = request.POST.get('content')
        id = request.POST.get('id')
        data = {'code': 200, 'content': remark}
        file_obj = File.objects.filter(id=id)
        if file_obj:
            file_obj.update(remark=remark)
        return Response(data)


# 是否付费
class FilePayView(LoginRequiredMixin, View):
    def get(self, request, file_id):
        file = File.objects.get(id=file_id)
        if file.isapprove == '0':
            if file.first_check == '0':
                file.first_check = '1'
        else:
            file.first_check = '2'
        file.save()
        return HttpResponseRedirect((reverse('files:wordpresslist')))


# 是否需要付费付费
class FileNeedPayView(LoginRequiredMixin, View):
    def get(self, request, file_id):
        file = File.objects.get(id=file_id)
        if file.isapprove == '0':
            file.isapprove = '1'
            file.first_check = '2'
        else:
            file.isapprove = '0'
            file.first_check = '0'

        file.save()
        return HttpResponseRedirect((reverse('index')))


# 删除
class FileDeleteView(LoginRequiredMixin, View):
    def get(self, request, file_id):
        file = File.objects.get(id=file_id)
        file.delete()
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().month)
        day = str(datetime.datetime.now().day)
        username = request.user.username.upper()
        upload_path = os.path.join(root_path, username, year, month, day)
        path = os.path.join(upload_path, file.filename)
        os.remove(path)
        return HttpResponseRedirect((reverse('index')))


# 发布站
class WordPresslistView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get('search')
        if search:
            search = search.strip()
            if request.user.role == '3' or request.user.is_superuser == 1:
                files = File.objects.filter(Q(fileno__icontains=search) | Q(filename__icontains=search)
                                            | Q(owner__icontains=search)).order_by('-add_time')
            else:
                files = File.objects.filter(Q(fileno__icontains=search) | Q(filename__icontains=search),
                                            owner=request.user.username).order_by('-add_time')
        else:
            files = File.objects.all().order_by('-add_time')

        # 分页功能实现
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(files, per_page=per_page, request=request)
        p_contents = p.page(page)
        start = (int(page) - 1) * per_page  # 避免分页后每行数据序号从1开始

        return render(request, 'files/wordpress.html', {'p_contents': p_contents, 'start': start, 'search': search})


# 文件下载
class FileWordPressDownloadView(LoginRequiredMixin, View):
    def get(self, request, file_id):
        file = File.objects.get(id=file_id)
        filename = file.filename
        filepath = file.filepath
        if not os.path.isfile(os.path.join(filepath, filename)):
            return render(request, 'files/word_press_file_download_error.html', {'msg': '文件可能已经被删除，请联系管理员~'})
        file_pay = file.first_check
        if file_pay == '0' or file_pay == 0:
            return render(request, 'files/word_press_file_download_error.html', {'msg': '文件未付费，请先付费~'})
        download_file = open(os.path.join(filepath, filename), 'rb')
        response = FileResponse(download_file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename=' + urlquote(filename)
        return response
