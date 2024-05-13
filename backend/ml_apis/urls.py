from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.getData),
    path('checkConnection/', views.newData),
    path('getTemperature/', views.getTemperature),
    path('getHumidity/', views.getHumidity),
]
