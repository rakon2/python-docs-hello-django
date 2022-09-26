from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("**** Hello  ITC  Batch team, Good evening & welcome To D365 - It's a great Journey ****")
