# _*_ coding : utf-8 _*_
from django.shortcuts import render_to_response, redirect, render


def main(request):
    username = request.session.get('username')
    data = {}
    if username:
        data['username'] = username
        return render(request, 'admin/main.html', data)
    return redirect('/admin/login/')


def left(request):
    return render_to_response('admin/left.html')


def head(request):
    return render_to_response('admin/head.html')


def foot(request):
    return render_to_response('admin/footer.html')


def welcome(request):
    return render_to_response('admin/welcome.html')
