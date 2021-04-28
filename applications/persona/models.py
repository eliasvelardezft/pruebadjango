from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades de los empleados'
    
    def __str__(self):
        return f'{str(self.id)} - {self.habilidad}'


class Empleado(models.Model):
    job_choices = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro')
    )
    first_name = models.CharField('Nombres', max_length=100)
    last_name = models.CharField('Apellidos', max_length=100)
    job = models.CharField('Trabajos', max_length=1, choices=job_choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    hoja_vida = RichTextField()

    class meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['id']
        unique_together = ('first_name', 'last_name')
        

    def __str__(self):
        return f'{str(self.id)} - {self.first_name} {self.last_name}'
