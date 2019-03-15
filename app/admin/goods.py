# coding:utf-8
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render_to_response, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from app.models import Goods


@csrf_exempt
def index(request):
    data = {}
    if request.GET:
        page = request.GET.get('page', 1)
        pagesize = request.GET.get('size', 10)
        good_list = Goods.objects.all().values()
        paginator = Paginator(good_list, pagesize)
        try:
            goodlist = paginator.page(page).object_list
        except PageNotAnInteger:
            goodlist = paginator.page(10).object_list
        except EmptyPage:
            goodlist = paginator.page(paginator.num_pages).object_list
        data['data'] = list(goodlist)
        return JsonResponse(data)
    return render_to_response('admin/Goods/index.html')
