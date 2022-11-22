import os
import subprocess
import signal
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def calcBytes(dataFromPage):
    res = float(dataFromPage) * 655.35
    return str(res)


def base(request):
    return render(request, 'base.html')


def terminalPage(request, tmIndex):
    tmfromlog = []
    dataFile = []
    idFrameList = []
    dlcFrameList = []
    dataFrameList = []

    status = None

    if request.method == 'POST':
        operation = request.POST.get('operation')
        if operation == 'startsending':
            status = 1
            p1 = subprocess.Popen(["/home/www/code/cleardata"])
            os.killpg(os.getpgid(p1.pid), signal.SIGTERM)
        if operation == 'stopsending':
            status = 0
        if operation == 'dataVcanPost':
            dataVcanList = request.POST.getlist('dataVcan[]')
            calcBytes(dataVcanList[0])
            module0 = calcBytes(dataVcanList[0])
            module1 = calcBytes(dataVcanList[1])
            module2 = calcBytes(dataVcanList[2])
            module3 = calcBytes(dataVcanList[3])
            module4 = calcBytes(dataVcanList[4])
            module5 = calcBytes(dataVcanList[5])
            module6 = calcBytes(dataVcanList[6])
            module7 = calcBytes(dataVcanList[7])
            p0 = subprocess.Popen(
                [
                    "/home/www/code/test2",
                    str(tmIndex),
                    "1",
                    "2",
                    module0, module1, module2, module3, module4, module5, module6, module7
                ])
            if status == 0:
                os.killpg(os.getpgid(p0.pid), signal.SIGTERM)
    with open("/home/www/code/data2.txt") as f:
        for line in f:
            dataFile.append(line.strip())
    for line in dataFile:
        s1 = line.strip().split("#")
        print(s1[0], tmIndex)
        if str(s1[0]) == str(tmIndex):
            idFrameList.append(s1[1])
            dlcFrameList.append(s1[2])
            dataFrameList.append(s1[3])
    queue = {
        'idList': idFrameList,
        'dlcList': dlcFrameList,
        'dataList': dataFrameList
    }
    all_rows = list(zip(*queue.values()))
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
