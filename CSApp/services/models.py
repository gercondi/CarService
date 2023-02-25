from django.db import models

# Create your models here.
class Services (models.Model):
    description = models.CharField(max_length=255, null=False, blank=False)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

