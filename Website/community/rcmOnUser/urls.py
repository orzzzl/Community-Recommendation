__author__ = 'zelengzhuang'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^preference', views.preference, name='preference'),
    url(r'^res', views.ans, name='ans')
]
