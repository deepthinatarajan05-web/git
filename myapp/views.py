from django.shortcuts import render
from django.http import HttpResponse
def myview(request):
    return HttpResponse("welcome<br>django")
def mysuccess(request):
    return HttpResponse("successfull django")
# Create your views here.
