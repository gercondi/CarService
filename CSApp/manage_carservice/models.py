from django.db import models
from owners.models import Owners
from services.models import Services

# Create your models here.


class ServicestoCars (models.Model):

    class PorFacturar(models.TextChoices):
        SI = 'S', 'Facturado'
        NO = 'N', 'No Facturado'

    placa = models.ForeignKey(Owners, on_delete=models.CASCADE)
    servicio = models.ManyToManyField(Services)
    date = models.DateTimeField
    porfacturar = models.CharField(max_length=1, choices=PorFacturar.choices, default='N')

    def __str__(self):
        return self.placa

