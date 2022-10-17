"""CanBusProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from canbusapp import views

urlpatterns = [
    path('', include('canbusapp.urls')),
    path('vcan0', views.vcan0, name="vcan0"),
    path('vcan1', views.vcan1, name="vcan1"),
    path('vcan2', views.vcan2, name="vcan2"),
    path('vcan3', views.vcan3, name="vcan3"),
    path('vcan4', views.vcan4, name="vcan4"),
    path('vcan5', views.vcan5, name="vcan5"),
    path('vcan6', views.vcan6, name="vcan6"),
    path('vcan7', views.vcan1, name="vcan7"),
    path('admin/', admin.site.urls),
]

