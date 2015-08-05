__author__ = 'zelengzhuang'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^questions', views.questions, name='questions'),
    url(r'^res', views.res, name='res'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^satisfaction2', views.satisfaction2, name='satisfaction2'),
    url(r'^satisfaction3', views.satisfaction3, name='satisfaction3'),
    url(r'^satisfaction1', views.satisfaction1, name='satisfaction1'),
    url(r'^thankyou', views.thankyou, name='thankyou')
]
