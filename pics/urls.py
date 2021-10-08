from django.shortcuts import render
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url('^gallery/', views.gallery, name='gallery'),
    url('^search/', views.search, name='search'),
    url('^location/(?P<locale>\w+)/', views.location, name='location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
