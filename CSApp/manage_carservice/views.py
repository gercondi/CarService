from django.shortcuts import render
from django.http import HttpResponse
from .models import ServicestoCars,Owners
from cars.models import Cars

# Create your views here.
def index(request):
    num_services = ServicestoCars.objects.all().count()
    num_cars = Cars.objects.all().count()
    num_owners = Owners.objects.all().count()
    services_car = ServicestoCars.objects.all().count()

    return render(request, 'index.html', context={'num_services':num_services, 'num_cars':num_cars,
                                                  'num_owners':num_owners, 'car_services':services_car})

def newservice(request):
    return HttpResponse("Estoy en Nuevo Servicio")

def login(request):
    return HttpResponse("Estoy en el Login")

