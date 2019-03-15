from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('用户名', max_length=20)
    password = models.CharField('密码', max_length=20)


class Goods(models.Model):
    id = models.AutoField(primary_key=True)
    goods_name = models.CharField(max_length=50, blank=True, null=True)
    goods_category = models.CharField(max_length=20, blank=True, null=True)
    goods_price = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    goods_summary = models.CharField(max_length=200, blank=True, null=True)
    goods_detail = models.TextField()
    create_name = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.TimeField(auto_now_add=True)
