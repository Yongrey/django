from django.shortcuts import render, HttpResponse
from .models import Bottle
# Create your views here.

def contacts(request):
   return render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')


def makers_list(request):
    context = {}
    bottles_list = Bottle.objects.all()
    context["bottles_list"] = bottles_list
    return render(request, 'makers.html', context)