from django.shortcuts import render, redirect, HttpResponse
from main.models import UserInfo
from dingtalk.client.api import Bpms

import time


# Create your views here.
def index(request):
    return render(request, 'main.html')


def login(request):
    error_msg = None
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        if request.POST.get('email', ) == 'root@163.com' and request.POST.get('pwd') == '123':
            return redirect("http://192.168.0.147:8001")
        else:
            error_msg = '邮箱或密码错误'
            return render(request, 'login.html', {'error': error_msg})


def user_list(request):
    ret = UserInfo.objects.all()
    # print(ret[0].id, ret[0].name)
    return render(request, 'ORM_user_list.html', {'user_list': ret})


def add_user(request):
    if request.method == 'GET':
        return render(request, 'ORM_add_user.html')
    else:
        username = request.POST.get('username')
        UserInfo.objects.create(name=username)
        return redirect('/user_list/')


def ding_login(request):
    return render(request, 'ding_login.html')


def get_ding_shenpi(request):
    process_code = 'PROC-ELYJ1A4W-7WJ39FFR3417CDU1EEOZ2-D8YFWXSJ-2'
    user_id = '250426260736250483'
    dt = '2019-03-08 00:00:00'
    ts = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    time_stamp = time.mktime(ts)
    process_instance_id = '201903081609000566214'
    print(time_stamp)
    sp_client = Bpms()
    # sp_list = sp_client.processinstance_list(process_code, dt, userid_list=[user_id])
    # print(sp_list)
    res = sp_client.processinstance_get(process_instance_id='201903081609000566214')
    print(res)
    return HttpResponse("测试获取审批实例")
