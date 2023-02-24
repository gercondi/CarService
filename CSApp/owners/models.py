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
