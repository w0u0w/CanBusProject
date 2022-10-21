from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import subprocess
import sys

# Create your views here.
from django.http import HttpResponse
import can
import random
import time


def startSending(bus, request):
        msg = can.Message(arbitration_id=0x01, data=[1, 2], is_extended_id=False)
        task = bus.send_periodic(msg, 2)
        assert isinstance(task, can.CyclicSendTaskABC)
        return render(request, "vcan0.html", {'interface': 'vcan0', })


def index(request):
    return render(request, 'index.html')

global flag
@csrf_exempt
def vcan0(request):
    with can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=25000) as bus:
        if request.POST.get('operation') == 'startsending':
            startSending(bus, request)
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