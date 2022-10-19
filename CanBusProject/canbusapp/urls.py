from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("generatedata_vcan0", views.generatedata_vcan0),
]