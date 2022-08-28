from django.urls import path

from App_Proyecto_final.views import  (Buscar_combo, combo_unica, copetin_unica, 
disfraz_unica, editarcombo, editarcopetin, editardisfraz, editargolosinas,eliminar_combo,
Buscar_copetin, Buscar_disfraz, Buscar_golosinas, Busqueda_Nombre, Busqueda_Nombre_combo,
Busqueda_Nombre_copetin, Busqueda_Nombre_disfraz, agregar_avatar, combo_cotillon,
combo_cotillon_formulario, copetin, copetin_formulario, disfraz, disfraz_formulario,
editar_perfil, eliminar_copetin, eliminar_disfraz, eliminar_golosina, golosina_unica,
golosinas, golosinas_formulario, inicio, loginview, registrar)
from django.contrib.auth.views import LogoutView 
urlpatterns = [
    path('', inicio,name='Inicio'),
    path('golosinas/', golosinas,name='Golosinas'),
    path('golosinas-unica/<int:id>', golosina_unica,name='golosinas-unica'),
    path('copetin/', copetin, name='Copetin'),
    path('copetin-unica/<int:id>', copetin_unica,name='copetin-unica'),
    path('disfraz/',disfraz, name='Disfraz'),
    path('disfraz-unica/<int:id>', disfraz_unica,name='disfraz-unica'),
    path('combo-cotillon/', combo_cotillon, name='ComboCotillon'),
    path('combo-unica/<int:id>', combo_unica,name='combo-unica'),
    path('golosina-formulario/', golosinas_formulario, name='golosinas-formulario'),
    path('eliminar-golosina/<int:id>', eliminar_golosina, name='eliminar-golosina'),
    path('editargolosina/<int:id>', editargolosinas, name="editargolosina" ),
    path('copetin-formulario/', copetin_formulario, name='copetin-formulario'),
    path('eliminar-copetin/<int:id>', eliminar_copetin, name='eliminar-copetin'),
    path('editarcopetin/<int:id>', editarcopetin, name="editarcopetin" ),
    path('disfraz-formulario/', disfraz_formulario, name='disfraz-formulario'),
    path('eliminar-disfraz/<int:id>', eliminar_disfraz, name='eliminar-disfraz'),
    path('editardisfraz/<int:id>', editardisfraz, name="editardisfraz" ),
    path('combo-cotillon-formulario/', combo_cotillon_formulario, name='combo-cotillon-formulario'),
    path('eliminar-combo/<int:id>', eliminar_combo, name='eliminar-combo'),
    path('editarcombo/<int:id>', editarcombo, name="editarcombo" ),
    path('busquedaNombre/', Busqueda_Nombre, name='busqueda-nombre'),
    path('Buscar/', Buscar_golosinas, name='Buscar'),
    path('busquedaNombredisfraz/', Busqueda_Nombre_disfraz, name='busqueda-nombredisfraz'),
    path('Buscard/', Buscar_disfraz, name='Buscard'),
    path('Buscarc/', Buscar_copetin, name='Buscarc'),
    path('busquedaNombrecopetin/', Busqueda_Nombre_copetin, name='busqueda-nombrecopetin'),
    path('Buscarcom/', Buscar_combo, name='Buscarcom'),
    path('busquedaNombrecombo/', Busqueda_Nombre_combo, name='busqueda-nombrecombo'),
    path('login/', loginview, name='login'),
    path('registrar/', registrar, name='registrar'),
    path('logout/',LogoutView.as_view(template_name='logout.html') , name='logout'),
    path('editar-perfil/', editar_perfil, name='editar-perfil'),
    path('agregar-avatar/', agregar_avatar, name='agregar-avatar'),

    
    
    


    
]