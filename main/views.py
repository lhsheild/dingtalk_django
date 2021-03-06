from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from main.models import UserInfo
from booksmanager.models import Publisher


# Create your views here.
def index(request):
    return render(request, 'home.html')


def mi(request):
    return render(request, 'MISHOP_TEST.html')


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


def publisher_list(request):
    object = Publisher.objects.all()
    return render(request, 'publisher_list2.html', {'publisher_list': object})


def add_publisher(request):
    if request.method == 'GET':
        return render(request, 'add_publisher2.html')
    else:
        publisher_name = request.POST.get('publisher')
        if publisher_name:
            Publisher.objects.create(name=publisher_name)
            return redirect('/publisher_list/')
        else:
            error_msg = '出版社不能为空!'
        return render(request, 'add_publisher2.html', {'error': error_msg})


# CBV添加出版社
class AddPublisher(View):
    def get(self, request):
        return render(request, 'add_publisher2.html')

    def post(self, request):
        publisher_name = request.POST.get('publisher')
        if publisher_name:
            Publisher.objects.create(name=publisher_name)
            return redirect('/publisher_list/')
        else:
            error_msg = '出版社不能为空!'
        return render(request, 'add_publisher2.html', {'error': error_msg})


def delete_publisher(request):
    if request.method == 'GET':
        delete_id = request.GET.get('id')
        if delete_id:
            del_obj = Publisher.objects.get(id=delete_id)
            del_obj.delete()
            return redirect('/publisher_list/')
        else:
            return HttpResponse('找不到该数据')

def delete_publisher2(request, del_id):
    if del_id:
        del_obj = Publisher.objects.get(id=del_id)
        del_obj.delete()
        return redirect('/publisher_list/')
    else:
        return HttpResponse('找不到该数据')

class DeletePublisher(View):
    def get(self,request,del_id):
        if del_id:
            del_obj = Publisher.objects.get(id=del_id)
            del_obj.delete()
            return redirect('/publisher_list/')
        else:
            return HttpResponse('找不到该数据')

def edit_publisher(request):
    if request.method == 'GET':
        edit_id = request.GET.get('id')
        if edit_id:
            edit_obj = Publisher.objects.get(id=edit_id)
            return render(request, 'ORM_edit_publisher.html', {'publisher': edit_obj})
    else:
        new_publisher_name = request.POST.get('publisher_name')
        edit_obj = Publisher.objects.get(id=request.POST.get('id'))
        edit_obj.name = new_publisher_name
        edit_obj.save()
        return redirect('/publisher_list/')


def ding_login(request):
    return render(request, 'ding_login.html')
