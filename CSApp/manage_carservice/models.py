from django.db import models
from cars.models import Cars
from services.models import Services

# Create your models here.


class ServicestoCars (models.Model):

    class PorFacturar(models.TextChoices):
        S = 'S' #, 'Facturado'
        N = 'N' #, 'No Facturado'

    placa = models.ForeignKey(Cars, on_delete=models.CASCADE)
    servicio = models.ManyToManyField(Services)
    date = models.DateTimeField(verbose_name='fechaservicio',auto_now=True)
    porfacturar = models.CharField(max_length=1, choices=PorFacturar.choices, default=PorFacturar.N)

    def __str__(self):
        return "Servicio creado exitosamente"

    class Meta:
        verbose_name = 'Servicio a Carro'
        verbose_name_plural = 'Servicios a Carros'

