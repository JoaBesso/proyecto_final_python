from django import forms


class GolosinasFormulario(forms.Form):

    nombre = forms.CharField( max_length=50)
    marca = forms.CharField( max_length=50)
    tipo_de_producto = forms.CharField( max_length=50)
    unidades = forms.IntegerField()

class CopetinFormulario(forms.Form):

    nombre = forms.CharField( max_length=50)
    marca = forms.CharField( max_length=50)
    tipo_de_producto = forms.CharField( max_length=50)
    peso = forms.IntegerField()

class DisfrazFormulario(forms.Form):
    nombre = forms.CharField( max_length=50)
    talle = forms.IntegerField()

class ComboCotillonFormulario(forms.Form):

    nombre = forms.CharField( max_length=50)
    cantidad_personas = forms.IntegerField()