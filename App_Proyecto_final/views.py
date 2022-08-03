from django.http import HttpResponse
from django.shortcuts import render
from App_Proyecto_final.forms import ComboCotillonFormulario, CopetinFormulario, DisfrazFormulario, GolosinasFormulario
from django.urls import is_valid_path
from App_Proyecto_final.models import ComboCotillon, Copetin, Disfraz, Golosinas

# Create your views here.
def agregar_golosinas(self,nombre,marca,tipo_de_producto,unidades):
    golosinas = Golosinas(nombre=nombre,marca=marca,tipo_de_producto=tipo_de_producto, unidades=unidades)
    golosinas.save()
    return HttpResponse(f"""
    <p>Golosinas:{golosinas.nombre} - marca:{golosinas.marca} - tipo_de_producto:{golosinas.tipo_de_producto}- unidades:{golosinas.unidades}
    """)


def inicio(self):
    
    return render(self, 'inicio.html')
    

def golosinas(self):
    
    return render(self,"golosinas.html")

def combo_cotillon(self):
    
    return render(self,"combocotillon.html")

def copetin(self):
    
    return render(self,"copetin.html")

def disfraz(self):
    
    return render(self,"disfraz.html")




def golosinas_formulario(request):

    if request.method == 'POST':

        g_form = GolosinasFormulario(request.POST)

        if g_form.is_valid():

            data = g_form.cleaned_data
        golosina = Golosinas(nombre=data['nombre'], marca=data['marca'], tipo_de_producto=data['tipo_de_producto'], unidades=data['unidades'])
        golosina.save()

        return render(request,'inicio.html')
    else:

        g_form = GolosinasFormulario() 
    
    return render(request,"golosinasFormulario.html", {"g_form":g_form})


def copetin_formulario(request):

    if request.method == 'POST':

        cop_form = CopetinFormulario(request.POST)

        if cop_form.is_valid():

            data = cop_form.cleaned_data
        copet = Copetin(nombre=data['nombre'], marca=data['marca'], tipo_de_producto=data['tipo_de_producto'], peso=data['peso'])
        copet.save()

        return render(request,'inicio.html')
    else:

        cop_form = CopetinFormulario() 
    
    return render(request,"copetinFormulario.html", {"cop_form":cop_form})

def disfraz_formulario(request):

    if request.method == 'POST':

        dis_form = DisfrazFormulario(request.POST)

        if dis_form.is_valid():

            data = dis_form.cleaned_data
        disfra = Disfraz(nombre=data['nombre'], talle=data['talle'])
        disfra.save()

        return render(request,'inicio.html')
    else:

        dis_form = DisfrazFormulario
    
    return render(request,"disfrazFormulario.html", {"dis_form":dis_form})

def combo_cotillon_formulario(request):

    if request.method == 'POST':

        comb_form = ComboCotillonFormulario(request.POST)

        if comb_form.is_valid():

            data = comb_form.cleaned_data
        combo = ComboCotillon(nombre=data['nombre'], cantidad_personas=data['cantidad_personas'])
        combo.save()

        return render(request,'inicio.html')
    else:

        comb_form = ComboCotillonFormulario
    
    return render(request,"combocotillonFormulario.html", {"comb_form":comb_form})


def Busqueda_Nombre(request):

    return render(request,'busquedaNombre.html')

def Buscar(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        productos = Golosinas.objects.filter(nombre__icontains =nombre)
        return render(request,"ResultadoBusqueda.html",{"productos":productos})
    else:
        respuesta = "no enviaste datos" 
    return HttpResponse(respuesta)

#[]