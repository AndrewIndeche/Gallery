from django.shortcuts import render
from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
]
