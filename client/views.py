from django.shortcuts import render
from .models import Client
# Create your views here.

def client_list(request):
    context = {}
    clients_list = Client.objects.all()
    context["clients_list"] = clients_list
    return render(request, 'clients.html', context)