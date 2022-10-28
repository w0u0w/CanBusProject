from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('/terminal/', views.terminalPage, name='terminal'),
]
