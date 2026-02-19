from django.shortcuts import render
from django.http import HttpResponse
def myview(request):
    return render(request,"myapp/index.html")

# Create your views here.
