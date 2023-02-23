from django.db import models

# Create your models here.
class Owners(models.Model):
    documento = models.CharField(max_length=20, null=False, blank=False, primary_key=True)
    nombre = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, blank=False)
    telefono = models.CharField(max_length=15, null=False, blank=False)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Propietario'
        verbose_name_plural = 'Propietarios'

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