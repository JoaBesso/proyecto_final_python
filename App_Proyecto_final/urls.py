from django.urls import path

from App_Proyecto_final.views import combo_cotillon, copetin, disfraz, golosinas, inicio, agregar_golosinas

urlpatterns = [
    path('agrega-golosina/<nombre>/<marca>/<tipo_de_producto>/<unidades>/', agregar_golosinas),
    path('', inicio),
    path('golosinas/', golosinas),
    path('copetin/', copetin),
    path('disfraz/',disfraz),
    path('combo-cotillon/', combo_cotillon),
]