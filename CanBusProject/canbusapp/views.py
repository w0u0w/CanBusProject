from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from can.interface import Bus
import subprocess
import sys
from threading import Thread
# Create your views here.
from django.http import HttpResponse
import can
import random
import time


def index(request):
    return render(request, 'index.html')


def createTask(bus, msg):
    task = bus.send_periodic(msg, 2)
    assert isinstance(task, can.RestartableCyclicTaskABC)
    task.stop()
    return task


def genNewMsg():
    msg = can.Message(arbitration_id=random.randint(1, 100), data=[1, 1, 1, 1])
    return msg


@csrf_exempt
def vcan0(request):
    bus = can.interface.Bus(interface='socketcan', channel='vcan0')
    # msg = can.Message(arbitration_id=random.randint(1, 100), data=[1, 1, 1, 1])
    myTask = createTask(bus, genNewMsg())
    if request.POST.get('operation') == 'startsending':
        myTask.start()
    if request.POST.get('operation') == 'stopsending':
        # bus.stop_all_periodic_tasks()
        myTask.stop()
        # bus.shutdown()

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