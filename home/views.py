# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from home import models

# user_list = [
#     {"user": "韩海龙", "pwd": "123"},
#     {"user": "宋娜娜", "pwd": "123"}
# ]


def home(request):
    # return HttpResponse("Hello Django")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print "username is %s,password is %s" % (username, password)

        # 添加到数据库
        models.UserModel.objects.create(user=username, pwd=password)

    # 查询数据库
    user_list = models.UserModel.objects.all()

    return render(request, "home.html", {"data": user_list})
