# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.models import User
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    if request.POST:
        username = request.POST['userName']
        password = request.POST['password']
        if username is not None:
            user = User.objects.filter(name=username)
            if len(user) > 0:
                if user[0].password == password:
                    request.session['username'] = username
                    return HttpResponse('200')
        return HttpResponse('404')
    return render(request, 'admin/login.html')


def loginout(request):
    del request.session["username"]
    return redirect('/admin/login/')
