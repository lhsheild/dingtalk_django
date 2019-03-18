from django.conf.urls import url
from booksmanager02 import views


urlpatterns = [
    url(r'', views.Main.as_view()),
]