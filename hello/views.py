from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("**** Hello  ITC  Batch team, we learnt AZ900 & its very nice  ****")
