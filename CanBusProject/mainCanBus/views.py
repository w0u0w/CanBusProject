from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("<h1>CAN BUS MAIN PAGE</h1>")