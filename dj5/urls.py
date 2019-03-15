"""webdig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import app.admin.users as use
import app.admin.goods as goods
import app.admin.login as login
import app.layout as lay
import app.tests as test
import app.views.index as index

urlpatterns = [
    # path('admin/', admin.site.urls),

    path('admin/login/', login.login),
    path('admin/loginout/', login.loginout),
    path('admin/tests/', test.test),
    path('admin/index/', lay.main),
    path('admin/main/', lay.welcome),
    path('admin/left/', lay.left),
    path('admin/user/', use.index),
    path('admin/save/', use.save),
    path('admin/select/', use.selectdata),
    path('admin/detail/', use.detail),
    path('admin/delete/', use.delete),
    path('admin/goods_list/', goods.index),

    path('index/', index.index),

]
