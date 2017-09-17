from django.shortcuts import render
from .forms import laedForm

def landing(request):
    form = laedForm(request.POST or None)
    return render(request, 'landing/landing.html', locals())

def index(request):
    form = laedForm(request.POST or None)
    if request.POST and form.is_valid():
        newForm =form.save()

    return render(request, 'landing/index.html', locals())
# Create your views here.
