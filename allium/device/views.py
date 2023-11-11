from django.shortcuts import render
from .models import Device


def index(request):
    device = Device.objects.latest('eventTime')
    return render(request, 'device.html', {'device': device})


