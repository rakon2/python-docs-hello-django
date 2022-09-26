from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("**** Hello  ITC  Batch team, we learnt D365 & its very nice  ****")
