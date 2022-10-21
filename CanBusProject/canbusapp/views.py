from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse
import can
import random
import time

flag = False


def index(request):
    with can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=25000) as bus:
        msg = can.Message(arbitration_id=0x01, data=[1, 2], is_extended_id=False)
        if request.POST.get('operation') == 'startsending':
            bus.send(msg)
        if request.POST.get('operation') == 'stopsending':
            pass
    return render(request, 'index.html')


@csrf_exempt
def vcan0(request):
    # global flag
    # with can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=25000) as bus:
    #     msg = can.Message(arbitration_id=0x01, data=[1, 2], is_extended_id=False)
    #     # task = bus.send_periodic(msg, 2)
    #     if request.POST.get('operation') == 'startsending':
    #         flag = True
    #
    #     if request.POST.get('operation') == 'stopsending':
    #         flag = False
    #         # bus.shutdown()
    #
    #     while flag:
    #         bus.send(msg)
    #         time.sleep(2)
    return render(request, "vcan0.html", {'interface': 'vcan0'})
  
  
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