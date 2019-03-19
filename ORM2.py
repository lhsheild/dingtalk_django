import os


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dingtalk_django.settings')
    import django
    django.setup()

    from django.db import transaction
    from django.db.models import *
    from orm import models

    print(models.Book.objects.all())

    '''聚合分组'''
    ret0 = models.Book.objects.all().annotate(author_num=Count('author'))
    print(ret0.values('title','author_num'))

