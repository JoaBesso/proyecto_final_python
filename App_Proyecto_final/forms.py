from dataclasses import fields
import email
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from App_Proyecto_final.models import Avatar

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


class UserEditForm(UserChangeForm):
    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label=" Repetir Contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    email = forms.CharField(label="Mail")
    class Meta:
        model = User
        fields =['email','first_name','last_name']
    
    def clean_password2(self):
        password2 = self.cleaned_data["password2"]
        if (password2 != self.cleaned_data["password1"]):
            raise forms.ValidationError("las contraseñas no coinciden.")

        return password2

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model =Avatar
        fields=('imagen',)
