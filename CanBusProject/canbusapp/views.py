import os
import subprocess
import time
import signal
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from subprocess import call
import can
import random


def base(request):
    return render(request, 'base.html')


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def vcan0(request):
    dataFile = []
    idFrameList = []
    dlcFrameList = []
    dataFrameList = []
    status = None
    if request.POST.get('operation') == 'startsending':
        status = 1
    if request.POST.get('operation') == 'stopsending':
        status = 0
    print("STATUS OF INTERFACE VCAN0 " + str(status))
    if status is not None:
        p0 = subprocess.Popen(["/home/www/code/sendcanframe", "1", f"{status}"])
        if status == 0:
            os.killpg(os.getpgid(p0.pid), signal.SIGTERM)
    with open("/home/www/code/data.txt") as f:
        for line in f:
            dataFile.append(line.strip())
    for line in dataFile:
        s1 = line.strip().split("#")
        print(s1)
        print(s1[1])
        idFrameList.append(s1[0])
        dlcFrameList.append(s1[1])
        dataFrameList.append(s1[2])
    print(dataFile)
    queue = {
        'idList': idFrameList,
        'dlcList': dlcFrameList,
        'dataList': dataFrameList
    }
    all_rows = list(zip(*queue.values()))
    print(all_rows)
    return render(request, "vcan0.html", {'interface': 'vcan0', 'all_rows': all_rows})


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
