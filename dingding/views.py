import asyncio
import requests
import time
from threading import Thread
from django.shortcuts import render, redirect, HttpResponse


# Create your views here.
def ding_shenpi(request):
    # 获取access_token
    appkey = 'dingmdy8p4txyehahwqv'
    appsecret = 'msKp0WTSjbgcaLmhmBUJhYhqkpWua-Gu8HTvSxhTf1tgIwuf4U50a_CXqoQVzYQg'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1', }
    ret = requests.get('https://oapi.dingtalk.com/gettoken?appkey={}&appsecret={}'.format(appkey, appsecret),
                       headers=header)
    # print(ret.json())
    # print(type(ret.json()))
    access_token = ret.json()['access_token']
    # print(access_token)

    # 批量获取审批实例ID
    r = requests.post('https://oapi.dingtalk.com/topapi/processinstance/listids?access_token={}'.format(access_token),
                      data={'process_code': 'PROC-ELYJ1A4W-SXJ37TP95QVKM4F1BV143-L84IYXSJ-4',
                            'start_time': '1544406815'})
    result = r.json()
    result = result['result']
    # print(type(result), result)
    shenpi_list = result['list']

    # 通过审批实例ID获取审批详细数据(多线程)
    shenpi_shili_url = 'https://oapi.dingtalk.com/topapi/processinstance/get?access_token={}'.format(access_token)
    t_list = []

    for i in shenpi_list:
        # 单线程
        # shenpi_shili = requests.post(shenpi_shili_url, data={'process_instance_id': i})
        # shenpi_shili_json = shenpi_shili.json()
        # print(shenpi_shili_json)

        # 多线程
        t = Thread(target=get_shenpi_data, args=(shenpi_shili_url, i))
        t.start()
        t_list.append(t)
        [t.join() for t in t_list]

    return HttpResponse('成功了 ')


def get_shenpi_data(url, id):
    shenpi_shili = requests.post(url, data={'process_instance_id': id})
    shenpi_shili_json = shenpi_shili.json()
    print(shenpi_shili_json)
