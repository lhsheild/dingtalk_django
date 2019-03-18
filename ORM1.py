import os


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dingtalk_django.settings')
    import django
    django.setup()

    from queryfunc import models

    ret = models.Person.objects.all().order_by('birthday')
    for i in ret:
        print(i.name)
