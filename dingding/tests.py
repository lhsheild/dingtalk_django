# Create your tests here.
import datetime
import json
import os

import requests


def save_img(in_args):
    print(in_args)
    img_url = in_args[0]
    file_name = in_args[1]
    upload_time = in_args[2]
    file_path = in_args[3]  # my_setting.img_folder_path
    year_s, mon_s, day_s = upload_time.split(' ')[0].split('-')
    save_path = '{}{}{}{}{}{}{}'.format(file_path, os.sep, year_s, os.sep, mon_s, os.sep, day_s)
    print('save_path:', save_path)
    try:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
            print(save_path)
        file_suffix = os.path.splitext(img_url)[1]
        filename = '{}{}{}{}'.format(save_path, os.sep, file_name, file_suffix)
        print('filename:', filename)

        r = requests.get(img_url, stream=True)
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
        r.close()
        return filename
        print("downloading picture succedd!， {}".format(filename))
    except IOError as e:
        print(e)
    except Exception as e:
        print(e)


def func_container_nogeo(data_dic):
    all_data = data_dic.get('process_instance').get('form_component_values')
    name = all_data[0].get('value')  # 监测点
    # print(name)
    # geophysical_point = all_data[1].get('value')  # 物探点号
    # print(geophysical_point)
    work_function = 0
    upload_time = json.loads(all_data[1].get('value'))[0]  # 审批提交时间
    year_s, mon_s, day_s = upload_time.split(' ')[0].split('-')  # 年月日
    date = datetime.datetime(int(year_s), int(mon_s), int(day_s)).date()  # 检测日期/采样日期
    # print(date)
    img_folder = r'D:\Project\PythonProjects\Sewage\media\img'

    exterior_photo_link_lst = json.loads(all_data[2].get('value'))  # 钉钉回调的外景照链接
    exterior_photo_lst = []
    if exterior_photo_link_lst is not None:
        for counter, exterior_photo_link in enumerate(exterior_photo_link_lst):
            img_name = '{}_{}_{}'.format(name, 'exterior', counter)
            img_path = save_img(
                (exterior_photo_link, img_name, upload_time, img_folder))
            exterior_photo_lst.append(img_path)
    # print(exterior_photo_lst)

    water_photo_link_lst = json.loads(all_data[3].get('value'))  # 钉钉回调的水流照链接
    water_photo_lst = []
    if water_photo_link_lst is not None:
        for counter, water_photo_link in enumerate(water_photo_link_lst):
            img_name = '{}_{}_{}'.format(name, 'flow', counter)
            img_path = save_img((water_photo_link, img_name, upload_time, img_folder))
            water_photo_lst.append(img_path)
    # print(water_photo_lst)

    work_photo_link_lst = json.loads(all_data[4].get('value'))  # 钉钉回调的工作照链接
    work_photo_lst = []
    if work_photo_link_lst is not None:
        for counter, work_photo_link in enumerate(work_photo_link_lst):
            img_name = '{}_{}_{}'.format(name, 'work', counter)
            img_path = save_img((work_photo_link, img_name, upload_time, img_folder))
            work_photo_lst.append(img_path)
    # print(work_photo_lst)

    people = data_dic.get('process_instance').get('title').split('提交')[0]  # 监测者/采样者
    # print(people)

    monitor_time_str = all_data[5].get('value')
    hour_s, min_s = monitor_time_str.split(':')
    monitor_time = datetime.datetime(int(year_s), int(mon_s), int(day_s), int(hour_s), int(min_s)).time()  # 检测/采样时间段
    # print(monitor_time)

    # 容器法测流量
    time1 = all_data[6].get('value')
    # print(time1)
    volume1 = all_data[7].get('value')
    # print(volume1)
    time2 = all_data[8].get('value')
    # print(time2)
    volume2 = all_data[9].get('value')
    # print(volume2)
    time3 = all_data[10].get('value')
    # print(time3)
    volume3 = all_data[11].get('value')
    # print(volume3)

    # 样品编号
    sample_number = all_data[12].get('value')
    # print(sample_number)

    # 监测指标
    indicator = all_data[13].get('value')

    # 样品数量
    # sample_count = all_data[15].get('value')

    sample_photo_link_lst = json.loads(all_data[14].get('value'))  # 钉钉回调的样品照链接
    sample_photo_lst = []
    if sample_photo_link_lst is not None:
        for counter, sample_photo_link in enumerate(sample_photo_link_lst):
            img_name = '{}_{}_{}_{}'.format(name, sample_number, 'sample', counter)
            img_path = save_img((sample_photo_link, img_name, upload_time, img_folder))
            sample_photo_lst.append(img_path)
    # print(sample_photo_lst)

    # 样品颜色
    sample_color = all_data[15].get('value')
    # print(sample_color)
    # 样品气味
    sample_odor = all_data[16].get('value')
    # print(sample_odor)
    # 样品浊度
    sample_turbidity = all_data[17].get('value')
    # print(sample_turbidity)

    try:
        from django.db import transaction
        with transaction.atomic():
            if models.DingCallbackMonitorpoint.objects.all().filter(name=name):
                monitor_obj = models.DingCallbackMonitorpoint.objects.all().filter(
                    name=name).first()
                if exterior_photo_lst:
                    if monitor_obj.exterior_photo and json.dumps(json.loads(monitor_obj.exterior_photo)) is not 'null':
                        monitor_obj.exterior_photo = json.dumps(
                            json.loads(monitor_obj.exterior_photo) + exterior_photo_lst)
                    else:
                        monitor_obj.exterior_photo = json.dumps(exterior_photo_lst)
                if water_photo_lst:
                    if monitor_obj.water_flow_photo and json.dumps(
                            json.loads(monitor_obj.water_flow_photo)) is not 'null':
                        monitor_obj.water_flow_photo = json.dumps(
                            json.loads(monitor_obj.water_flow_photo) + water_photo_lst)
                    else:
                        monitor_obj.water_flow_photo = json.dumps(water_photo_lst)
                if work_photo_lst:
                    if monitor_obj.work_photo and json.dumps(json.loads(monitor_obj.work_photo)) is not 'null':
                        monitor_obj.work_photo = json.dumps(json.loads(monitor_obj.work_photo) + work_photo_lst)
                    else:
                        monitor_obj.work_photo = json.dumps(work_photo_lst)
                monitor_obj.save()
            else:
                monitor_obj = models.DingCallbackMonitorpoint.objects.create(
                    name=name,
                    geophysical_point=name,
                    is_monitor=1,
                    people=people,
                    work_function=work_function,
                    exterior_photo=json.dumps(exterior_photo_lst),
                    water_flow_photo=json.dumps(water_photo_lst),
                    work_photo=json.dumps(work_photo_lst),
                    start_time=date
                )
            print('MonitorPoint created!!')

            sample_dic = {
                'monitor_point': monitor_obj,
                'people': people,
                'sample_date': date,
                'sample_time': monitor_time,
                'sample_photo': json.dumps(sample_photo_lst),
                'sample_number': sample_number,
                'sample_color': sample_color,
                'sample_odor': sample_odor,
                'sample_turbidity': sample_turbidity,
                'monitor_task': indicator,
                'sample_count': 2
            }
            models.DingCallbackSampleinfo.objects.create(**sample_dic)
            print('SampleInfo created!!')

            models.DingCallbackFlowinfo.objects.create(
                monitor_point=monitor_obj,
                people=people,
                flow_date=date,
                flow_time=monitor_time,
                time1=time1,
                volume1=volume1,
                time2=time2,
                volume2=volume2,
                time3=time3,
                volume3=volume3
            )
            print('FlowInfo created!!')
    except Exception as e:
        print(e)


def func_container(data_dic):
    all_data = data_dic.get('process_instance').get('form_component_values')
    name = all_data[0].get('value')  # 监测点
    # print(name)
    geophysical_point = all_data[1].get('value')  # 物探点号
    # print(geophysical_point)
    work_function = 0
    upload_time = json.loads(all_data[2].get('value'))[0]  # 审批提交时间
    year_s, mon_s, day_s = upload_time.split(' ')[0].split('-')  # 年月日
    date = datetime.datetime(int(year_s), int(mon_s), int(day_s)).date()  # 检测日期/采样日期
    # print(date)
    img_folder = r'D:\Project\PythonProjects\Sewage\media\img'

    exterior_photo_link_lst = json.loads(all_data[3].get('value'))  # 钉钉回调的外景照链接
    exterior_photo_lst = []
    if exterior_photo_link_lst is not None:
        for counter, exterior_photo_link in enumerate(exterior_photo_link_lst):
            img_name = '{}_{}_{}'.format(geophysical_point, 'exterior', counter)
            img_path = save_img(
                (exterior_photo_link, img_name, upload_time, img_folder))
            exterior_photo_lst.append(img_path)
    # print(exterior_photo_lst)

    water_photo_link_lst = json.loads(all_data[4].get('value'))  # 钉钉回调的水流照链接
    water_photo_lst = []
    if water_photo_link_lst is not None:
        for counter, water_photo_link in enumerate(water_photo_link_lst):
            img_name = '{}_{}_{}'.format(geophysical_point, 'flow', counter)
            img_path = save_img((water_photo_link, img_name, upload_time, img_folder))
            water_photo_lst.append(img_path)
    # print(water_photo_lst)

    work_photo_link_lst = json.loads(all_data[5].get('value'))  # 钉钉回调的工作照链接
    work_photo_lst = []
    if work_photo_link_lst is not None:
        for counter, work_photo_link in enumerate(work_photo_link_lst):
            img_name = '{}_{}_{}'.format(geophysical_point, 'work', counter)
            img_path = save_img((work_photo_link, img_name, upload_time, img_folder))
            work_photo_lst.append(img_path)
    # print(work_photo_lst)

    people = data_dic.get('process_instance').get('title').split('提交')[0]  # 监测者/采样者
    # print(people)

    monitor_time_str = all_data[6].get('value')
    hour_s, min_s = monitor_time_str.split(':')
    monitor_time = datetime.datetime(int(year_s), int(mon_s), int(day_s), int(hour_s), int(min_s)).time()  # 检测/采样时间段
    # print(monitor_time)

    # 容器法测流量
    time1 = all_data[7].get('value')
    # print(time1)
    volume1 = all_data[8].get('value')
    # print(volume1)
    time2 = all_data[9].get('value')
    # print(time2)
    volume2 = all_data[10].get('value')
    # print(volume2)
    time3 = all_data[11].get('value')
    # print(time3)
    volume3 = all_data[12].get('value')
    # print(volume3)

    # 样品编号
    sample_number = all_data[13].get('value')
    # print(sample_number)

    # 监测指标
    indicator = all_data[14].get('value')

    # 样品数量
    # sample_count = all_data[15].get('value')

    sample_photo_link_lst = json.loads(all_data[15].get('value'))  # 钉钉回调的样品照链接
    sample_photo_lst = []
    if sample_photo_link_lst is not None:
        for counter, sample_photo_link in enumerate(sample_photo_link_lst):
            img_name = '{}_{}_{}_{}'.format(geophysical_point, sample_number, 'sample', counter)
            img_path = save_img((sample_photo_link, img_name, upload_time, img_folder))
            sample_photo_lst.append(img_path)
    # print(sample_photo_lst)

    # 样品颜色
    sample_color = all_data[16].get('value')
    # print(sample_color)
    # 样品气味
    sample_odor = all_data[17].get('value')
    # print(sample_odor)
    # 样品浊度
    sample_turbidity = all_data[18].get('value')
    # print(sample_turbidity)

    try:
        from django.db import transaction
        with transaction.atomic():
            if models.DingCallbackMonitorpoint.objects.all().filter(geophysical_point=geophysical_point):
                monitor_obj = models.DingCallbackMonitorpoint.objects.all().filter(
                    geophysical_point=geophysical_point).first()
                if exterior_photo_lst:
                    if monitor_obj.exterior_photo and json.dumps(json.loads(monitor_obj.exterior_photo)) is not 'null':
                        monitor_obj.exterior_photo = json.dumps(
                            json.loads(monitor_obj.exterior_photo) + exterior_photo_lst)
                    else:
                        monitor_obj.exterior_photo = json.dumps(exterior_photo_lst)
                if water_photo_lst:
                    if monitor_obj.water_flow_photo and json.dumps(
                            json.loads(monitor_obj.water_flow_photo)) is not 'null':
                        monitor_obj.water_flow_photo = json.dumps(
                            json.loads(monitor_obj.water_flow_photo) + water_photo_lst)
                    else:
                        monitor_obj.water_flow_photo = json.dumps(water_photo_lst)
                if work_photo_lst:
                    if monitor_obj.work_photo and json.dumps(json.loads(monitor_obj.work_photo)) is not 'null':
                        monitor_obj.work_photo = json.dumps(json.loads(monitor_obj.work_photo) + work_photo_lst)
                    else:
                        monitor_obj.work_photo = json.dumps(work_photo_lst)
                monitor_obj.save()
            else:
                monitor_obj = models.DingCallbackMonitorpoint.objects.create(
                    name=name,
                    geophysical_point=geophysical_point,
                    is_monitor=1,
                    people=people,
                    work_function=work_function,
                    exterior_photo=json.dumps(exterior_photo_lst),
                    water_flow_photo=json.dumps(water_photo_lst),
                    work_photo=json.dumps(work_photo_lst),
                    start_time=date
                )
            print('MonitorPoint created!!')

            sample_dic = {
                'monitor_point': monitor_obj,
                'people': people,
                'sample_date': date,
                'sample_time': monitor_time,
                'sample_photo': json.dumps(sample_photo_lst),
                'sample_number': sample_number,
                'sample_color': sample_color,
                'sample_odor': sample_odor,
                'sample_turbidity': sample_turbidity,
                'monitor_task': indicator,
                'sample_count': 2
            }
            models.DingCallbackSampleinfo.objects.create(**sample_dic)
            print('SampleInfo created!!')

            models.DingCallbackFlowinfo.objects.create(
                monitor_point=monitor_obj,
                people=people,
                flow_date=date,
                flow_time=monitor_time,
                time1=time1,
                volume1=volume1,
                time2=time2,
                volume2=volume2,
                time3=time3,
                volume3=volume3
            )
            print('FlowInfo created!!')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dingtalk_django.settings")
    import django

    django.setup()

    from dingding import models

    data_dic = {'errcode': 0, 'process_instance': {'attached_process_instance_ids': [], 'biz_action': 'NONE',
                                                   'business_id': '201904130838000200615',
                                                   'create_time': '2019-04-13 08:38:20',
                                                   'finish_time': '2019-04-13 08:46:05',
                                                   'form_component_values': [{'name': '监测点', 'value': 'FHJ2-3'},
                                                                             {'name': '监测点物探号', 'value': '42NQYS27'}, {
                                                                                 'ext_value': '当前时间:2019-04-13 08:34:57\n当前地点:广西壮族自治区南宁市江南区江南街道宏德路150-19号南宁市自行车总厂生活区',
                                                                                 'name': '["当前时间","当前地点"]',
                                                                                 'value': '["2019-04-13 08:34:57",108.2763232421875,22.802205946180557,"广西壮族自治区南宁市江南区江南街道宏德路150-19号南宁市自行车总厂生活区",65]'},
                                                                             {'name': '监测点外景照',
                                                                              'value': '["https://static.dingtalk.com/media/lADPBE1XX-MZirDNBQDNAtA_720_1280.jpg"]'},
                                                                             {'name': '监测点水流照',
                                                                              'value': '["https://static.dingtalk.com/media/lADPBE1XX-Ma4WnNBQDNAtA_720_1280.jpg"]'},
                                                                             {'name': '无法监测原因', 'value': '无水流'},
                                                                             {'name': '是否合格', 'value': '是'}],
                                                   'operation_records': [
                                                       {'date': '2019-04-13 08:38:20', 'operation_result': 'NONE',
                                                        'operation_type': 'START_PROCESS_INSTANCE',
                                                        'userid': '166869521621373591'},
                                                       {'date': '2019-04-13 08:46:04', 'operation_result': 'REFUSE',
                                                        'operation_type': 'EXECUTE_TASK_NORMAL', 'remark': '管口没有拍到',
                                                        'userid': '215312413421401344'}],
                                                   'originator_dept_id': '104846032', 'originator_dept_name': '实习生',
                                                   'originator_userid': '166869521621373591', 'result': 'refuse',
                                                   'status': 'COMPLETED', 'tasks': [
            {'create_time': '2019-04-13 08:38:20', 'finish_time': '2019-04-13 08:46:05', 'task_result': 'REFUSE',
             'task_status': 'COMPLETED', 'taskid': '61112265635', 'userid': '215312413421401344'}],
                                                   'title': '向剑雷提交的流量水质监测（无法监测）'}, 'request_id': 'nfek8j519bnj'}

    all_data = data_dic.get('process_instance').get('form_component_values')
    print(all_data)
    if all_data[1].get('name') == '监测点物探号':
        func_container(data_dic)
    else:
        func_container_nogeo(data_dic)
    # print(all_data[16].get('name'))
