from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from App_Proyecto_final.forms import AvatarFormulario, ComboCotillonFormulario, CopetinFormulario, DisfrazFormulario, GolosinasFormulario, UserEditForm
from django.urls import is_valid_path
from App_Proyecto_final.models import Avatar, ComboCotillon, Copetin, Disfraz, Golosinas
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def agregar_golosinas(self,nombre,marca,tipo_de_producto,unidades):
    golosinas = Golosinas(nombre=nombre,marca=marca,tipo_de_producto=tipo_de_producto, unidades=unidades)
    golosinas.save()
    return HttpResponse(f"""
    <p>Golosinas:{golosinas.nombre} - marca:{golosinas.marca} - tipo_de_producto:{golosinas.tipo_de_producto}- unidades:{golosinas.unidades}
    """)


def inicio(request):
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, 'inicio.html',{"url": avatar.imagen.url})
    except:
        return render(request, 'inicio.html')
    

def golosinas(request):
    
    return render(request,"golosinas.html")

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


def loginview(request):
    if request.method == 'POST':

        form = AuthenticationForm(request,data=request.POST)

        if form.is_valid():

            data = form.cleaned_data

            usuario = data["username"]
            clave = data["password"]

            user = authenticate(username=usuario, password=clave)

            if user:

                login(request,user)
                return render(request,"inicio.html", {"mensaje": f'Bienvenido {usuario}'})
            else:
                return render(request,"inicio.html",{"mensaje": "error, datos incorrectos"})
        return render(request,"inicio.html",{"mensaje":"error, formulario invalido"})
    else:
        form = AuthenticationForm()
    return render(request, "login.html",{"form": form})

def registrar(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            username = data["username"]

            form.save()

            return render(request, "inicio.html",{"mensaje": f'usuario {username} creado'})
    else:
        form = UserCreationForm()

    return render(request, "registro.html",{"form": form})


def editar_perfil(request):
    usuario= request.user
    if request.method == 'POST':

        form = UserEditForm(request.POST,instance=request.user)

        if form.is_valid():

            data = form.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            

            usuario.save()

            return render(request, "inicio.html",{"mensaje": "Sus datos han sido actualizados correctamente!"})
    else:
        form = UserEditForm(instance=request.user)

    return render(request, "EditarPerfil.html",{"form": form})

def agregar_avatar(request):

    if request.method == 'POST':

        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():

            data = form.cleaned_data
            avatar = Avatar(user=request.user, imagen=data['imagen'])
            avatar.save()

            return render(request,'inicio.html',{"mensaje": "Avatar cargado..."})
    else:

        form = AvatarFormulario() 
    
    return render(request,"agregarAvatar.html", {"form":form})
#[]