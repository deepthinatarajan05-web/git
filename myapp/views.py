from django.shortcuts import render
from django.http import HttpResponse
def myview(request):
    return render(request,"myapp/index.html")
def mysuccess(request):
    return render(request,"myapp/scnd.html")
# Create your views here.
