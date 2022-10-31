from django.urls import path
from django.urls import include, path, register_converter
from . import views


class TerminalChecker:
    regex = '[1-2]'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


register_converter(TerminalChecker, 'tm')


class InterfaceChecker:
    regex = '[0-7]'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


register_converter(TerminalChecker, 'ic')

urlpatterns = [
    path('', views.base, name='base'),
    path('terminal/<tm:tmIndex>/', views.terminalPage, name='terminalNumber'),
    path('terminal/<tm:tmIndex>/vcan/<int:icIndex>/', views.vcan, name='vcanInterface'),

]
