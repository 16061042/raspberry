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
    

def switch_off(request):


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
        #content = json.loads(request.body.decode())
        #print(content)
    return HttpResponse("success")
