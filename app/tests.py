# coding:utf-8
from app.ClassLib.urldata import reqdata
from django.http import HttpResponse
from app.models import Goods
import urllib.request
import os
import json
import datetime


def test(request):
    res = dd()
    return HttpResponse(str(res))


def test1():
    req = reqdata()
    url = "http://q.stock.sohu.com/hisHq?code=zs_399300&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp&0.27326577514529204"
    res = req.requrl(url)
    res = res.replace('historySearchHandler(', '')
    res = res.replace(')', '')
    return res


def test2():
    req = reqdata()
    url = "http://q.stock.sohu.com/zs/399300/lshq.shtml"
    res = req.selsm(url)
    return res


def test3():
    req = reqdata()
    url = "http://news.baidu.com/"
    try:
        res = req.beasoaplist(url)
        for imgsrc in res:
            if req.reg(imgsrc) is None:
                continue
            with open('download/imgurl.txt', 'w', encoding='utf-8') as file:
                file.write(imgsrc)
            result = urllib.request.Request(imgsrc)
            with urllib.request.urlopen(result) as response:
                data = response.read()
                # if len(data) < 1024 * 100:
                #   continue
                if not os.path.exists('download'):
                    os.mkdir('download')
                filename = req.getname(imgsrc)
                filename = 'download/' + filename
                with open(filename, 'wb') as f:
                    f.write(data)
        return '下载成功'
    except Exception as e:
        return str(e)


def dd():
    req = reqdata()
    url = "http://e.dangdang.com/media/api.go?action=mediaCategoryLeaf&promotionType=1&deviceSerialNo=html5&macAddr=html5&channelType=html5&permanentId=20190311144828373429030242631487465&returnType=json&channelId=70000&clientVersionNo=5.8.4&platformSource=DDDS-P&fromPlatform=106&deviceType=pconline&token=&start=21&end=41&category=ZTXYTL&dimension=dd_sale&order=0"
    try:
        res = req.requrl(url)
        jsonstr = json.loads(res)
        dic_json = jsonstr['data']['saleList']
        product_list_to_insert = list()
        for each_json in dic_json:
            goods = Goods()
            jsons=each_json['mediaList'][0]
            goods.goods_name = jsons['title']
            goods.goods_category = jsons['categorys']
            goods.goods_summary = jsons['coverPic']
            goods.goods_price = jsons['lowestPrice']
            goods.goods_detail = jsons['descs']
            goods.create_name = jsons['authorPenname']
            product_list_to_insert.append(goods)
        Goods.objects.bulk_create(product_list_to_insert)
        return '下载成功'
    except Exception as e:
        return str(e)
