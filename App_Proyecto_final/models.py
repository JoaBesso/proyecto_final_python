from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Golosinas(models.Model):

    nombre = models.CharField( max_length=50)
    marca = models.CharField( max_length=50)
    tipo_de_producto = models.CharField( max_length=50)
    unidades = models.IntegerField()
    marca = models.CharField( max_length=50)


    def __str__(self) -> str:
        return f'{self.nombre}-{self.marca}-{self.tipo_de_producto}-{self.unidades}'


class Disfraz(models.Model):

    nombre = models.CharField( max_length=50)
    talle = models.CharField( max_length=50)
    def __str__(self) -> str:
        return f'{self.nombre}-{self.talle}'

class ComboCotillon(models.Model):

    nombre = models.CharField( max_length=50)
    cantidad_personas = models.IntegerField()
    def __str__(self) -> str:
        return f'{self.nombre}-{self.cantidad_personas}'

class Copetin(models.Model):

    nombre = models.CharField( max_length=50)
    marca = models.CharField( max_length=50)
    tipo_de_producto = models.CharField( max_length=50)
    peso = models.IntegerField()
    def __str__(self) -> str:
        return f'{self.nombre}-{self.marca}-{self.tipo_de_producto}-{self.peso}'
    
    
class Avatar(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares',blank=True, null=True)
