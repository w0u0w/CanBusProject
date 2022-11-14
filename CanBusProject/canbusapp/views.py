import os
import subprocess
import time
import signal
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from subprocess import call
import can
import random


def datatobyte(number):
    number = number * (65535 / 100)
    return number


def base(request):
    return render(request, 'base.html')


def terminalPage(request, tmIndex):
    dataFile = []
    idFrameList = []
    dlcFrameList = []
    dataFrameList = []

    status = None
    if request.method == 'POST':
        operation = request.POST.get('operation')
        if operation == 'startsending':
            status = 1
        if operation == 'stopsending':
            status = 0
        if operation == 'dataVcanPost':
            dataVcanList = request.POST.get('dataVcan')
            print(dataVcanList)
            vcan0 = datatobyte(dataVcanList[0])
            vcan1 = datatobyte(dataVcanList[1])
            vcan2 = datatobyte(dataVcanList[2])
            vcan3 = datatobyte(dataVcanList[3])
            vcan4 = datatobyte(dataVcanList[4])
            vcan5 = datatobyte(dataVcanList[5])
            vcan6 = datatobyte(dataVcanList[6])
            vcan7 = datatobyte(dataVcanList[7])
            print("TERMINAL" + str(tmIndex) + ": STATUS OF INTERFACE VCAN" + "" + str(status))
            if status is not None:
                p0 = subprocess.Popen(
                    [
                        "/home/www/code/testing",
                        str(tmIndex),
                        f"{status}",
                        vcan0, vcan1, vcan2, vcan3, vcan4, vcan5, vcan6, vcan7
                    ])
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
        'tmIndex': tmIndex,
        'all_rows': all_rows
    }
    return render(request, 'terminal.html', context)


def logs(request, icIndex, tmIndex):
    context = {
        'icIndex': icIndex,
        'tmIndex': tmIndex
    }
    return render(request, 'logs.html', context)


@csrf_exempt
def vcan(request, icIndex, tmIndex):

    context = {
        'icIndex': icIndex,
        'tmIndex': tmIndex,
        'interface': 'vcan0', #обязательно поменять
    }
    return render(request, "vcan0.html", context)
