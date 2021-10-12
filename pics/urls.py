from django.shortcuts import render
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^gallery/', views.gallery, name='gallery'),
    url(r'^search/', views.search, name='search'),
    url(r'^location/(?P<location>\w+)/', views.image_location, name='location'),
]
