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
    
    return render(self, 'inicio.html')
    return HttpResponse("vista de inicio")

def golosinas(self):
    
    return render(self,"golosinas.html")

def combo_cotillon(self):
    
    return render(self,"combocotillon.html")

def copetin(self):
    
    return render(self,"copetin.html")

def disfraz(self):
    
    return render(self,"disfraz.html")