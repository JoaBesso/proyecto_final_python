from django.db import models

# Create your models here.

class Golosinas(models.Model):

    nombre = models.CharField( max_length=50)
    marca = models.CharField( max_length=50)
    tipo_de_producto = models.CharField( max_length=50)
    unidades = models.IntegerField()


class Disfraz(models.Model):

    nombre = models.CharField( max_length=50)
    talle = models.CharField( max_length=50)

class ComboCotillon(models.Model):

    nombre = models.CharField( max_length=50)
    cantidad_personas = models.IntegerField()

class Copetin(models.Model):

    nombre = models.CharField( max_length=50)
    marca = models.CharField( max_length=50)
    tipo_de_producto = models.CharField( max_length=50)
    peso = models.IntegerField()
    
    