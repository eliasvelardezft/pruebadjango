from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=150)
    short_name = models.CharField('Nombre Corto', max_length=100)
    active = models.BooleanField('Activo', default=True)

    def __str__(self):
        return f'{self.name}'
