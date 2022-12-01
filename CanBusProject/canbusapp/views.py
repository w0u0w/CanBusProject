import asyncio
import os
import subprocess
import signal
import time

from django.shortcuts import render
import threading
from django.views.decorators.csrf import csrf_exempt
from asgiref.sync import sync_to_async


def calcBytes(dataFromPage):
    res = float(dataFromPage) * 655.35
    return str(res)


@sync_to_async
def asyncTest(status, tmIndex, dataModuleList):
    module0 = calcBytes(dataModuleList[0])
    module1 = calcBytes(dataModuleList[1])
    module2 = calcBytes(dataModuleList[2])
    module3 = calcBytes(dataModuleList[3])
    module4 = calcBytes(dataModuleList[4])
    module5 = calcBytes(dataModuleList[5])
    module6 = calcBytes(dataModuleList[6])
    module7 = calcBytes(dataModuleList[7])
    p0 = subprocess.Popen(
        [
            "/home/www/code/test2",
            str(tmIndex),
            "1",
            "2",
            module0, module1, module2, module3, module4, module5, module6, module7
        ])
    if status == 0:
        pass
        os.killpg(os.getpgid(p0.pid), signal.SIGTERM)


def base(request):
    return render(request, 'base.html')


async def terminalPage(request, tmIndex):
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
        if operation == 'stopsending':
            status = 0
        if operation == 'dataVcanPost':
            dataModuleList = request.POST.getlist('dataVcan[]')
            task = asyncio.ensure_future(asyncTest(status, dataModuleList, tmIndex))
            await asyncio.wait(task)
            if status == 0:
                pass
                # os.killpg(os.getpgid(p0.pid), signal.SIGTERM)
    with open("/home/www/code/data2.txt") as f:
        for line in f:
            dataFile.append(line.strip())
    for line in dataFile:
        s1 = line.strip().split("#")
        # print(s1[0], tmIndex)
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
