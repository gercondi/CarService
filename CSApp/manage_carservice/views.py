from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def newservice(request):
    return HttpResponse("Estoy en Nuevo Servicio")

def login(request):
    return HttpResponse("Estoy en el Login")

