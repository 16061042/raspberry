from django.conf.urls import url, include 

from . import views

urlpatterns = [
    url(r'index/', views.index, name = 'index'),
    url(r'sensor/', views.sensor, name = 'sensor'),
    url(r'accessory/', views.accessory, name = 'accessory'),
    url(r'alarm/', views.alarm, name = 'alarm'),
]
