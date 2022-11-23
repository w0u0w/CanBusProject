from django.urls import path
from django.urls import include, path, register_converter
from . import views


class TerminalChecker:
    regex = '[1-10]'

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
    path('terminal/<int:tmIndex>/', views.terminalPage, name='terminalNumber'),
    ]
