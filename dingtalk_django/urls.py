"""dingtalk_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main import views as main_views
from dingding import views as ding_views
from booksmanager import views as books_views
from booksmanager02 import urls as books02_urls
from orm import views as orm_views


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^login/$', main_views.login),
    url(r'^user_list/$', main_views.user_list),
    url(r'^add_user/$', main_views.add_user),
    url(r'^publisher_list/$', main_views.publisher_list),
    url(r'^add_publisher/$', main_views.AddPublisher.as_view()),
    url(r'^delete_publisher/$', main_views.delete_publisher),
    url(r'^delete_publisher/(?P<del_id>[0-9]+)/$', main_views.DeletePublisher.as_view()),
    url(r'^edit_publisher/$', main_views.edit_publisher),
    url(r'^ding_login/$', main_views.ding_login),
    url(r'^get_ding_shenpi/$', ding_views.ding_shenpi),
    url(r'mi/$', main_views.mi),

    # dingding
    url(r'^dingding/', ding_views.ding_shenpi),

    # 回调失败测试
    url(r'^register_callback/$', ding_views.register_callback),
    url(r'^get_bms_callback/$', ding_views.get_bms_callback),

    # booksmanager
    url(r'^books_list/$', books_views.books_list),
    url(r'^add_book/$', books_views.add_book),
    url(r'^delete_book/$', books_views.delete_book),
    url(r'^edit_book/$', books_views.edit_book),
    url(r'^author_list/$', books_views.author_list),
    url(r'^add_author/$', books_views.add_author),
    url(r'^delete_author/$', books_views.delete_author),
    url(r'^edit_author/$', books_views.edit_author),
    url(r'^t_test/$', books_views.template_test),

    # django 进阶
    url(r'^upload_test/$', books_views.UploadFileTest.as_view()),
    url(r'^json_data/$', books_views.JSONTest.as_view()),

    url(r'^$', main_views.index),

    url(r'^booksmanager02/', include(books02_urls)),
    url(r'^books/$', orm_views.books),
]
