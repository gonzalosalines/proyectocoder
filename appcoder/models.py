from mailbox import NoSuchMailboxError
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

    #estas funciones sirven para q desde el admin panel se vea mejor la data de la BD
    def __str__(self):
        return f"{self.nombre}--> Camada {self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido.upper()}, {self.nombre.capitalize()}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.apellido.upper()}, {self.nombre.capitalize()} [{self.profesion.title()}]"

class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} -> {self.fecha_de_entrega}"



