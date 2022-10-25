import os
import subprocess
import time

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from subprocess import call
import can
import random


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def vcan0(request):
    # p0 = subprocess.Popen(["/home/www/code/sendcanframe", "1", "1"])
    if request.POST.get('operation') == 'startsending':
        subprocess.call(["./home/www/code/sendcanframe", "1", "1"])
    if request.POST.get('operation') == 'stopsending':
        subprocess.call(["./home/www/code/sendcanframe", "1", "0"])
        # subprocess.Popen(["/home/www/code/sendcanframe", "1", "0"])
    return render(request, "vcan0.html", {'interface': 'vcan0', })


def vcan1(request):
    return render(request, "vcan1.html", {'interface': 'vcan1'})


def vcan2(request):
    return render(request, "vcan2.html", {'interface': 'vcan2'})


def vcan3(request):
    return render(request, "vcan3.html", {'interface': 'vcan3'})


def vcan4(request):
    return render(request, "vcan4.html", {'interface': 'vcan4'})


def vcan5(request):
    return render(request, "vcan5.html", {'interface': 'vcan5'})


def vcan6(request):
    return render(request, "vcan6.html", {'interface': 'vcan6'})


def vcan7(request):
    return render(request, "vcan7.html", {'interface': 'vcan7'})
