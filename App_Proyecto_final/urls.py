from django.urls import path

from App_Proyecto_final.views import Buscar, Busqueda_Nombre, agregar_avatar, combo_cotillon, combo_cotillon_formulario, copetin, copetin_formulario, disfraz, disfraz_formulario, editar_perfil, golosinas, golosinas_formulario, inicio, agregar_golosinas, loginview, registrar
from django.contrib.auth.views import LogoutView 
urlpatterns = [
    path('agrega-golosina/<nombre>/<marca>/<tipo_de_producto>/<unidades>/', agregar_golosinas),
    path('', inicio,name='Inicio'),
    path('golosinas/', golosinas,name='Golosinas'),
    path('copetin/', copetin, name='Copetin'),
    path('disfraz/',disfraz, name='Disfraz'),
    path('combo-cotillon/', combo_cotillon, name='ComboCotillon'),
    path('golosina-formulario/', golosinas_formulario, name='golosinas-formulario'),
    path('copetin-formulario/', copetin_formulario, name='copetin-formulario'),
    path('disfraz-formulario/', disfraz_formulario, name='disfraz-formulario'),
    path('combo-cotillon-formulario/', combo_cotillon_formulario, name='combo-cotillon-formulario'),
    path('busquedaNombre/', Busqueda_Nombre, name='busqueda-nombre'),
    path('Buscar/', Buscar, name='Buscar'),
    path('login/', loginview, name='login'),
    path('registrar/', registrar, name='registrar'),
    path('logout/',LogoutView.as_view(template_name='logout.html') , name='logout'),
    path('editar-perfil/', editar_perfil, name='editar-perfil'),
    path('agregar-avatar/', agregar_avatar, name='agregar-avatar'),


    
]