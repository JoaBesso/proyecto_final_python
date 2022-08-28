from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Golosinas(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    nombre = models.CharField( max_length=50)
    marca = models.CharField( max_length=50)
    tipo_de_producto = models.CharField( max_length=50)
    unidades = models.IntegerField()
    imagen = models.ImageField(upload_to='golosinass',blank=True, null=True)
    precio =  models.CharField( max_length=50)
    descripcion = models.CharField( max_length=50)
    def __str__(self) -> str:
        return f'{self.nombre}-{self.marca}-{self.tipo_de_producto}-{self.unidades}-{self.imagen}-{self.precio}-{self.descripcion}'

def golosina_path(golosina,filename):

    return f'user_{golosina.user.id}/golosina_{golosina.id}/{filename}'

class Disfraz(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    nombre = models.CharField( max_length=50)
    talle = models.CharField( max_length=50)
    imagen = models.ImageField(upload_to='golosinass',blank=True, null=True)
    precio =  models.CharField( max_length=50)
    descripcion = models.CharField( max_length=50)
    def __str__(self) -> str:
        return f'{self.nombre}-{self.talle}-{self.imagen}-{self.precio}-{self.descripcion}'

class ComboCotillon(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    nombre = models.CharField( max_length=50)
    cantidad_personas = models.IntegerField()
    imagen = models.ImageField(upload_to='golosinass',blank=True, null=True)
    precio =  models.CharField( max_length=50)
    descripcion = models.CharField( max_length=50)
    def __str__(self) -> str:
        return f'{self.nombre}-{self.cantidad_personas}-{self.imagen}-{self.precio}-{self.descripcion}'

class Copetin(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    nombre = models.CharField( max_length=50)
    marca = models.CharField( max_length=50)
    tipo_de_producto = models.CharField( max_length=50)
    peso = models.IntegerField()
    imagen = models.ImageField(upload_to='golosinass',blank=True, null=True)
    precio =  models.CharField( max_length=50)
    descripcion = models.CharField( max_length=50)
    def __str__(self) -> str:
        return f'{self.nombre}-{self.marca}-{self.tipo_de_producto}-{self.peso}-{self.imagen}-{self.precio}-{self.descripcion}'
    
    
class Avatar(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares',blank=True, null=True)


    