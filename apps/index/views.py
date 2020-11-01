from django.shortcuts import render
from django.http import HttpResponse
from index.forms import MomentForm
import json
# Create your views here.


def welcome(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    print(ip)
    if not ip:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    return HttpResponse("hell world{}".format(ip))


def index(request):
    form = MomentForm()
    return render(request,'index.html',{'form':form})