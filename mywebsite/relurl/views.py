from django.shortcuts import render
from relurl.models import Device
# Create your views here.

def index (request):
    return  render(request, 'relurl/index.html')

def image (request):
    return render(request, 'relurl/image.html')

def relative (request):
    return render(request, 'relurl/relurl.html')

def templ (request):
    return render(request, 'relurl/tmplinh.html')

def devices (request):
    dlist = Device.objects.order_by('name')
    dev_list = {'device_list':dlist}
    return render(request, 'relurl/devices.html', context=dev_list)

