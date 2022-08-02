from django.http import HttpResponse
from django.shortcuts import render

from App_Proyecto_final.models import Golosinas

# Create your views here.
def agregar_golosinas(self,nombre,marca,tipo_de_producto,unidades):
    golosinas = Golosinas(nombre=nombre,marca=marca,tipo_de_producto=tipo_de_producto, unidades=unidades)
    golosinas.save()
    return HttpResponse(f"""
    <p>Golosinas:{golosinas.nombre} - marca:{golosinas.marca} - tipo_de_producto:{golosinas.tipo_de_producto}- unidades:{golosinas.unidades}
    """)


def inicio(self):
    
    return HttpResponse("vista de inicio")

def golosinas(self):
    
    return HttpResponse("vista de golosinas")

def combo_cotillon(self):
    
    return HttpResponse("vista de combo cotillon")

def copetin(self):
    
    return HttpResponse("vista de copetin")

def disfraz(self):
    
    return HttpResponse("vista de disfraz")