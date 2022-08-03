from django.urls import path

from App_Proyecto_final.views import Buscar, Busqueda_Nombre, combo_cotillon, combo_cotillon_formulario, copetin, copetin_formulario, disfraz, disfraz_formulario, golosinas, golosinas_formulario, inicio, agregar_golosinas

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
    
]