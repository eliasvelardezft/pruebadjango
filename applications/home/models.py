from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField()
    dni = models.CharField('DNI', max_length=50)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
