from django.db import models

# Create your models here.
class Cursos(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
class Tecnologias(models.Model):
    nombre = models.CharField(max_length=40)
    dificultad = models.CharField(max_length=40)
    
class Proyectos(models.Model):
    nombre = models.CharField(max_length=40)
    empresa = models.CharField(max_length=40)
    email = models.EmailField()