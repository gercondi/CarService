from django.db import models
from owners.models import Owners
# Create your models here.

class Cars(models.Model):
    placa = models.CharField(max_length=8, null=False, blank=False, unique=True, primary_key=True)
    modelo = models.CharField(max_length=5, null=False, blank=False)
    marca = models.CharField(max_length=255, null=False, blank=False)
    owner = models.ForeignKey(Owners, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.placa

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'