from django.shortcuts import render
from django.shortcuts import redirect
import hashlib
from django.template import loader
from django.http import HttpResponse
from django.core import serializers
import json
from . import models
from django import forms
from django.http import JsonResponse

def index(request):
    return HttpResponse("hello\r\n")

def switch_on(request):
    if(models.Switch.objects.all() == None):
        obj = models.Switch(switch=True)
        obj.save()
    else:
        obj = models.Switch.objects.get(id = 0)
        obj.switch = True
        obj.save()
    print(models.Switch.objects.all())
def switch_off(request):
    if (models.Switch.objects.all() == None):
        obj = models.Switch(switch=False)
        obj.save()
    else:
        obj = models.Switch.objects.get(id=0)
        obj.switch = False
        obj.save()
    print(models.Switch.objects.all())

def sensor(request):
    if request.method == 'POST':
        content = json.loads(request.body.decode())
    return HttpResponse("26.5")

def accessory(request):
    return HttpResponse("accessory response\r\n")

def alarm(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.body)
        print(request.body.decode())
    return HttpResponse("success")
