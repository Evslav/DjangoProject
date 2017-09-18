from django.http import HttpResponse
from django.shortcuts import render
from .forms import laedForm
from .forms import uinfo
import datetime

def landing(request):
    print(request.META['REMOTE_ADDR'])

    print("end")
    return render(request, 'landing/landing.html', locals())

def index(request):
    form = laedForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
    return render(request, 'landing/index.html', locals())

def uInfo(request):
    ua = request.META['HTTP_USER_AGENT']
    ip = request.META['REMOTE_ADDR']
    now = datetime.datetime.now()
    data = now.strftime("%d-%m-%Y %H:%M")
    return render(request, 'landing/uinfo.html', locals())

