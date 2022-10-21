from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
def vcan0(request):
    with can.Bus(interface="virtual") as bus:
        msg = can.Message(arbitration_id = 0x123, data = [1, 2, 3, 4, 5, 6], is_extended_id = False)
        if request.POST.get('operation') == 'startsending':
            task = bus.send_periodic(msg, 0.20)
            assert isinstance(task, can.CyclicSendTaskABC)
            time.sleep(2)
            task.stop()
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