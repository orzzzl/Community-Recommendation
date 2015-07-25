__author__ = 'zelengzhuang'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^questions', views.questions, name='questions'),
    url(r'^res', views.res, name='res')
]
