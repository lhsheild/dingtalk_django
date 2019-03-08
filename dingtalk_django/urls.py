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
from django.conf.urls import url
from django.contrib import admin
from main import views as main_views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^login/', main_views.login),
    url(r'^user_list/', main_views.user_list),
    url(r'^add_user/', main_views.add_user),
    url(r'^ding_login/', main_views.ding_login),
    url(r'^get_ding_shenpi/', main_views.get_ding_shenpi),
    url(r'^', main_views.index),
]
