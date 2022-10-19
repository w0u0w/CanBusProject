from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import can
import random
import time

def index(request):
    #bus0 = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
    #anw0 = "EMPTY"
    #anwRes = ""
    #cnt = 1
    #try:
    #  while cnt < 4:
    #    datalist = []
    #    for i in range(1,random.randint(2,8)):
    #      n = random.randint(1,8)
    #      datalist.append(n)
    #    msg0 = can.Message(arbitration_id=cnt, data=datalist, is_extended_id=False)
    #    bus0.send(msg0)
    #    decodeData0 = (" ".join(hex(b) for b in msg0.data))
    #    anw0 = "<br>Canbusapp message sent on {0} <br> <br>DATA: {0} id: {1} dlc: {2} data: {3} <br>".format(str(bus0.channel), 
    #                                                                str(msg0.arbitration_id), str(len(msg0.data)), str(decodeData0))
    #    anwRes += anw0
    #    cnt += 1
    #  return HttpResponse(f"{anwRes}")
    #except:
    #  anw0 = "message NOT sent"
    #  return HttpResponse(f"Canbus app {anw0}")
    return render(request, 'index.html')

def generateBus(interface):
    bus = can.interface.Bus(bustype='socketcan', channel=interface, bitrate=250000)
    return bus


def generateMsg(interface, flag):
    firstbyte = 11
    if flag:
        firstbyte = 1
    identification = {
        'vcan0': 0x01
    }
    msg = can.Message(arbitration_id=identification[interface], data=[firstbyte, 2, 3, 4, 5, 6, 7, 8])
    return msg


def startSending(bus, msg):
    task = bus.send_periodic(msg, 1)
    assert isinstance(task, can.CyclicSendTaskABC)
    return task


def vcan0(request):
    flag = False
    bus = generateBus('vcan0')
    if request.method == 'POST' and 'vcan0start' in request.POST:
        flag = True
        # startSending(bus, msg)
    if request.method == 'POST' and 'vcan0stop' in request.POST:
        flag = False

    while flag:
        msg = generateMsg('vcan0', flag)
        bus.send(msg)
        time.sleep(2)
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