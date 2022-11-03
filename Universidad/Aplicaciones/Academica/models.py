from email.policy import default
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from .choices import sexos

# Create your models here.

#Crea una clase con los datos del docente

class Docente(models.Model):
    apellidos = models.CharField(max_length = 20, verbose_name= 'Apellidos')
    email = models.CharField(max_length = 20, verbose_name= 'email')
    nombre = models.CharField(max_length = 20, verbose_name= 'Nombres')
    fechaNacimiento = models.DateField(verbose_name= 'Fecha de Nacimiento')
    contraseña = models.CharField(max_length = 20, verbose_name = 'email')
    sexo= models.CharField(max_length= 1, choices= sexos, default='F')

#Creo un atributo para devolver el nombre del Docente con el siguiente formato
    def nombreCompleto(self):
        return "{}, {}".format( self.nombre, self.apellidos)

#Aplico el str con ese formato
    def __str__(self):
        return self.nombreCompleto()

#Creo metadatos para dar formato en la tabla

class Meta:
    verbose_name= 'Docente'
    verbose_name_plural=  'Docentes'
    db_table= 'docentes'
    ordering= ['apellidos', '-nombre']


class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.ForeignKey(Docente, null= True, blank= True, on_delete= models.CASCADE)

    def __str__(self):
        return self.nombre