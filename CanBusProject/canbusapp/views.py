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


def terminalPage(request, tmIndex):
    status = None
    if request.POST.get('operation') == 'startsending':
        status = 1
    if request.POST.get('operation') == 'stopsending':
        status = 0
    if status is not None:
        p0 = subprocess.Popen(["/home/www/code/sendcanframe", "1", f"{status}"])
        if status == 0:
            os.killpg(os.getpgid(p0.pid), signal.SIGTERM)
    context = {
        'tmIndex': tmIndex,
    }
    return render(request, 'terminal.html', context)


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def vcan(request, icIndex, tmIndex):
    dataFile = []
    idFrameList = []
    dlcFrameList = []
    dataFrameList = []
    status = None
    if request.POST.get('operation') == 'startsending':
        status = 1
    if request.POST.get('operation') == 'stopsending':
        status = 0
    print("TERMINAL" + str(tmIndex) + ": STATUS OF INTERFACE VCAN" + str(icIndex) + "" + str(status))
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
    context = {
        'icIndex': icIndex,
        'tmIndex': tmIndex,
        'interface': 'vcan0', #обязательно поменять
        'all_rows': all_rows
    }
    return render(request, "vcan0.html", context)
