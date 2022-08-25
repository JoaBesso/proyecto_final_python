from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from App_Proyecto_final.forms import AvatarFormulario, ComboCotillonFormulario, CopetinFormulario, DisfrazFormulario, GolosinasFormulario, UserEditForm
from django.urls import is_valid_path
from App_Proyecto_final.models import Avatar, ComboCotillon, Copetin, Disfraz, Golosinas
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def inicio(request):

    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, 'inicio.html',{"url": avatar.imagen.url})
    except:
        return render(request, 'inicio.html')
    

def golosinas(request):
    golosinas= Golosinas.objects.all()
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, 'golosinas.html',{"golosinas": golosinas,"url": avatar.imagen.url})
    except:
        return render(request, 'golosinas.html',{"golosinas": golosinas})
    
    

def combo_cotillon(request):
    combos = ComboCotillon.objects.all()
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, 'combocotillon.html',{"combos":combos, "url": avatar.imagen.url})
    except:
        return render(request, 'combocotillon.html',{"combos":combos})
    
    

def copetin(request):
    copets= Copetin.objects.all()
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, 'copetin.html',{"copets": copets,"url": avatar.imagen.url})
    except:
        return render(request, 'copetin.html',{"copets": copets})
    
    

def disfraz(request):
    disfraces= Disfraz.objects.all()
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, 'disfraz.html',{"disfraces":disfraces, "url": avatar.imagen.url})
    except:
        return render(request, 'disfraz.html',{"disfraces": disfraces})
    





def golosinas_formulario(request):

    if request.method == 'POST':

        g_form = GolosinasFormulario(request.POST)

        if g_form.is_valid():

            data = g_form.cleaned_data
            golosina = Golosinas(nombre=data['nombre'], marca=data['marca'], tipo_de_producto=data['tipo_de_producto'], unidades=data['unidades'])
            golosina.save()
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'golosinas.html', {"url":avatar.imagen.url})
        except:
        
            return render(request, "golosinas.html",)
        
    else:

        g_form = GolosinasFormulario() 
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'golosinasFormulario.html',{"g_form": g_form, "url":avatar.imagen.url})
        except:
            return render(request,"golosinasFormulario.html", {"g_form":g_form})

def eliminar_golosina(request, id):

    if request.method == 'POST':
        golo = Golosinas.objects.get(id=id)
        golo.delete()
        golos = Golosinas.objects.all()
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'golosinas.html', {"golos":golos,"url":avatar.imagen.url})
        except:
        
            return render(request, "golosinas.html",{"golos":golos})






def editargolosinas(request,id):
    golosina = Golosinas.objects.get(id=id)
    if request.method == 'POST':
        miFormulario = GolosinasFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            golosina.nombre = data['nombre']
            golosina.marca = data['marca']
            golosina.tipo_de_producto = data['tipo_de_producto']
            golosina.unidades = data['unidades']
            golosina.save()
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'golosinas.html', {"url":avatar.imagen.url})
        except:
        
            return render(request, "golosinas.html",)
            
    else:
        miFormulario= GolosinasFormulario(initial={
            "nombre":golosina.nombre,
            "marca":golosina.marca,
            "tipo_de_producto":golosina.tipo_de_producto,
            "unidades":golosina.unidades,

        })
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'editargolosinas.html',{"miFormulario": miFormulario, "url":avatar.imagen.url})
        except:
            return render(request,"editargolosinas.html", {"miFormulario":miFormulario, "id":golosina.id})

def copetin_formulario(request):

    if request.method == 'POST':

        cop_form = CopetinFormulario(request.POST)

        if cop_form.is_valid():

            data = cop_form.cleaned_data
            copet = Copetin(nombre=data['nombre'], marca=data['marca'], tipo_de_producto=data['tipo_de_producto'], peso=data['peso'])
            copet.save()
            try:
                avatar = Avatar.objects.get(user=request.user.id)
                return render(request, 'inicio.html', {"url":avatar.imagen.url})
            except:
        
                return render(request, "inicio.html",)

        
    else:

        cop_form = CopetinFormulario() 
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'copetinFormulario.html',{"cop_form": cop_form, "url":avatar.imagen.url})
        except:
            return render(request,"copetinFormulario.html", {"cop_form":cop_form})

def eliminar_copetin(request, id):

    if request.method == 'POST':
        copet = Copetin.objects.get(id=id)
        copet.delete()
        copets = Copetin.objects.all()
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'copetin.html', {"copets":copets,"url":avatar.imagen.url})
        except:
        
            return render(request, "golosinas.html",{"copets":copets}) 

def editarcopetin(request,id):
    copetin = Copetin.objects.get(id=id)
    if request.method == 'POST':
        miFormulario = CopetinFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            copetin.nombre = data['nombre']
            copetin.marca = data['marca']
            copetin.tipo_de_producto = data['tipo_de_producto']
            copetin.peso = data['peso']
            copetin.save()
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'copetin.html', {"url":avatar.imagen.url})
        except:
        
            return render(request, "copetin.html",)
            
    else:
        miFormulario= CopetinFormulario(initial={
            "nombre":copetin.nombre,
            "marca":copetin.marca,
            "tipo_de_producto":copetin.tipo_de_producto,
            "peso":copetin.peso,

        })
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'editarcopetin.html',{"miFormulario": miFormulario, "url":avatar.imagen.url})
        except:
            return render(request,"editarcopetin.html", {"miFormulario":miFormulario, "id":copetin.id})    

def disfraz_formulario(request):

    if request.method == 'POST':

        dis_form = DisfrazFormulario(request.POST)

        if dis_form.is_valid():

            data = dis_form.cleaned_data
            disfra = Disfraz(nombre=data['nombre'], talle=data['talle'])
            disfra.save()
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'inicio.html', {"url":avatar.imagen.url})
        except:
        
            return render(request, "inicio.html",)
        
    else:

        dis_form = DisfrazFormulario() 
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'disfrazFormulario.html',{"dis_form": dis_form, "url":avatar.imagen.url})
        except:
            return render(request,"disfrazFormulario.html", {"dis_form":dis_form})

def eliminar_disfraz(request, id):

    if request.method == 'POST':
        disfraz = Disfraz.objects.get(id=id)
        disfraz.delete()
        disfra = Disfraz.objects.all()
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'disfraz.html', {"disfra":disfra,"url":avatar.imagen.url})
        except:
        
            return render(request, "disfraz.html",{"disfra":disfra})

def editardisfraz(request,id):
    disfraz = Disfraz.objects.get(id=id)
    if request.method == 'POST':
        miFormulario = DisfrazFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            disfraz.nombre = data['nombre']
            disfraz.talle = data['talle']
            disfraz.save()
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'disfraz.html', {"url":avatar.imagen.url})
        except:
        
            return render(request, "disfraz.html",)
            
    else:
        miFormulario= DisfrazFormulario(initial={
            "nombre":disfraz.nombre,
            "talle":disfraz.talle,
            

        })
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'editardisfraz.html',{"miFormulario": miFormulario, "url":avatar.imagen.url})
        except:
            return render(request,"editardisfraz.html", {"miFormulario":miFormulario, "id":disfraz.id})

def combo_cotillon_formulario(request):

    if request.method == 'POST':

        comb_form = ComboCotillonFormulario(request.POST)

        if comb_form.is_valid():

            data = comb_form.cleaned_data
            combo = ComboCotillon(nombre=data['nombre'], cantidad_personas=data['cantidad_personas'])
            combo.save()
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'inicio.html', {"url":avatar.imagen.url})
        except:
        
            return render(request, "inicio.html",)
        
    else:

        comb_form = ComboCotillonFormulario() 
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'combocotillonFormulario.html',{"comb_form": comb_form, "url":avatar.imagen.url})
        except:
            return render(request,"copetinFormulario.html", {"comb_form":comb_form})


def eliminar_combo(request, id):

    if request.method == 'POST':
        combo = ComboCotillon.objects.get(id=id)
        combo.delete()
        combos = ComboCotillon.objects.all()
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'combocotillon.html', {"combos":combos,"url":avatar.imagen.url})
        except:
        
            return render(request, "combocotillon.html",{"combos":combos})

def editarcombo(request,id):
    combo = ComboCotillon.objects.get(id=id)
    if request.method == 'POST':
        miFormulario = ComboCotillonFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            combo.nombre = data['nombre']
            combo.cantidad_personas = data['cantidad_personas']
            combo.save()
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'combocotillon.html', {"url":avatar.imagen.url})
        except:
        
            return render(request, "combocotillon.html",)
            
    else:
        miFormulario= ComboCotillonFormulario(initial={
            "nombre":combo.nombre,
            "cantidad_personas":combo.cantidad_personas,
            

        })
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'editarcombo.html',{"miFormulario": miFormulario, "url":avatar.imagen.url})
        except:
            return render(request,"editarcombo.html", {"miFormulario":miFormulario, "id":combo.id})



def Busqueda_Nombre(request):
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, 'busquedaNombre.html',{"url":avatar.imagen.url})
    except:
        return render(request,"busquedaNombre.html")
    

def Buscar_golosinas(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        productos = Golosinas.objects.filter(nombre__icontains =nombre)
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'ResultadoBusquedagolosina.html',{"productos": productos, "url":avatar.imagen.url})
        except:
            return render(request,"ResultadoBusquedagolosina.html",{"productos":productos})
        
    else:
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'ResultadoBusquedagolosina.html',{ "url":avatar.imagen.url})
        except:
            return render(request,"ResultadoBusquedagolosina.html")

def Busqueda_Nombre_disfraz(request):
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, 'busquedaNombredisfraz.html',{"url":avatar.imagen.url})
    except:
        return render(request,"busquedaNombredisfraz.html")

def Buscar_disfraz(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        productos = Disfraz.objects.filter(nombre__icontains =nombre)
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'ResultadoBusquedadisfraz.html',{"productos": productos, "url":avatar.imagen.url})
        except:
            return render(request,"ResultadoBusquedadisfraz.html",{"productos":productos})
        
    else:
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'ResultadoBusquedadisfraz.html',{ "url":avatar.imagen.url})
        except:
            return render(request,"ResultadoBusquedadisfraz.html")


def Busqueda_Nombre_copetin(request):
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, 'busquedaNombre_copetin.html',{"url":avatar.imagen.url})
    except:
        return render(request,"busquedaNombre_copetin.html")

def Buscar_copetin(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        productos = Copetin.objects.filter(nombre__icontains =nombre)
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'ResultadoBusquedacopetin.html',{"productos": productos, "url":avatar.imagen.url})
        except:
            return render(request,"ResultadoBusquedacopetin.html",{"productos":productos})
        
    else:
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'ResultadoBusquedacopetin.html',{ "url":avatar.imagen.url})
        except:
            return render(request,"ResultadoBusquedacopetin.html")

def Busqueda_Nombre_combo(request):
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, 'busquedaNombrecombo.html',{"url":avatar.imagen.url})
    except:
        return render(request,"busquedaNombrecombo.html")

def Buscar_combo(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        productos = ComboCotillon.objects.filter(nombre__icontains =nombre)
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'ResultadoBusquedacombo.html',{"productos": productos, "url":avatar.imagen.url})
        except:
            return render(request,"ResultadoBusquedacombo.html",{"productos":productos})
        
    else:
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'ResultadoBusquedacombo.html',{ "url":avatar.imagen.url})
        except:
            return render(request,"ResultadoBusquedacombo.html")







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

        form = UserEditForm(request.POST,request.FILES,instance=request.user)

        if form.is_valid():

            data = form.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]

            usuario.save()


        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'inicio.html',{"mensaje": "Sus datos han sido actualizados correctamente!", "url":avatar.imagen.url})
        except:
        
            return render(request, "inicio.html",{"mensaje": "Sus datos han sido actualizados correctamente!"})
    else:
        form = UserEditForm(instance=request.user)
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'EditarPerfil.html',{"form":form ,"url":avatar.imagen.url})
        except:
        

            return render(request, "EditarPerfil.html",{"form": form})

def agregar_avatar(request):

    if request.method == 'POST':

        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():

            data = form.cleaned_data
            avatar = Avatar(user=request.user, imagen=data['imagen'])
            avatar.save()
        try:
            avatar = Avatar.objects.get(user=request.user.id)
            return render(request, 'inicio.html', {"url":avatar.imagen.url})
        except:
        
            return render(request, "inicio.html",)
        
    else:

        form = AvatarFormulario() 
        try:
            avatar = Avatar.objects.get(user=request.user)
            return render(request, 'agregarAvatar.html',{"form": form, "url":avatar.imagen.url})
        except:
            return render(request,"agregarAvatar.html", {"form":form})




#[]