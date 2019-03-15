# _*_ coding : utf-8 _*_
from django.http import HttpResponse
from django.http import JsonResponse
from app.models import User
from django.shortcuts import render, render_to_response
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import json


def index(request):
    # user = User(name='test')
    # user.save()
    # return HttpResponse("<p>数据添加成功</p>")
    output = _("Welcome to my site.")
    list = User.objects.all().order_by("id")
    data = {}
    province = serializers.serialize("json", list)
    data["ctx"] = json.loads(province)
    return render(request, "admin/UserManage/index.html", data)


@csrf_exempt
def save(request):
    data = {}
    result = saveuser(request)
    return HttpResponse(result)


def saveuser(request):
    try:
        if request.POST:
            if request.POST['id'] != '':
                test = User.objects.get(id=request.POST['id'])
                test.password = request.POST['password']
                test.name = request.POST['username']
                test.save()
                return '200'
            old = User.objects.filter(name=request.POST['username'])
            if old:
                return '101'
            user = User(name=request.POST['username'], password=request.POST['password'])
            user.save()
            return '200'
        return '404'
    except Exception as e:
        return '500'


def delete(request):
    try:
        if request.GET:
            id = request.GET['id']
            user = User.objects.get(id=id)
            user.delete()
            return HttpResponse('200')
        return HttpResponse('404')
    except Exception:
        return HttpResponse('500')


def detail(request):
    data = {}
    id = ''
    if request.GET:
        id = request.GET['id']
        user = User.objects.get(id=id)
        data['username'] = user.name
        data['password'] = user.password
    data['id'] = id
    return render(request, 'admin/UserManage/detail.html', data)


@csrf_exempt
def selectdata(request):
    count = 0
    if request.GET:
        page = request.GET.get('page', 0)
        limit = request.GET.get("limit", 10)
        user_list = User.objects.all().values()
        count = user_list.count()
        paginator = Paginator(user_list, limit)
        try:
            userlist = paginator.page(page).object_list
        except PageNotAnInteger:
            userlist = paginator.page(10).object_list
        except EmptyPage:
            userlist = paginator.page(paginator.num_pages).object_list
    else:
        userlist = User.objects.all().values()
        count = userlist.count()
    data = {}
    # province = serializers.serialize("json", userlist)
    # data["ctx"] = json.loads(province)
    data["code"] = 0
    data["msg"] = ''
    data["count"] = count
    data["data"] = list(userlist)

    return JsonResponse(data, safe=False)


def userDetail():
    result = ""
    # 相当于select* from table
    lists = User.objects.all()
    # 过滤条件查询
    response = User.objects.filter(id=1)
    # 查询单条记录
    response1 = User.objects.get(id=1)
    # 限制返回条数
    User.objects.order_by("name")[0:2]
    # 数据排序
    User.objects.order_by("id")
    # 多条连续使用
    User.objects.filter(name='test').order_by('id')
    # 输出所有数据
    for var in lists:
        result += var.name + ','

    # 修改数据
    test = User.objects.get(id=1)
    test.name = 'ceshi1'
    test.save()
    # 删除数据
    test1 = User.objects.get(id=1)
    test1.delete()
    return HttpResponse("<p>数据添加成功" + result + "</p>")
