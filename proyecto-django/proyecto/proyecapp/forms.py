from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms
 
from proyecapp.models import *

class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'siglas']
        labels = {
            'nombre': _('Ingrese el nombre'),
            'siglas': _('Ingrese la siglas'),
        }


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'cedula', 'correo']
        labels = {
            'nombre': _('Ingrese el nombre'),
            'apellido': _('Ingrese el apellido'),
            'cedula': _('Ingrese la cedula'),
            'correo': _('Ingrese el correo'),
        }


class LocalComidaForm(ModelForm):
    class Meta:
        model = LocalComida
        fields = ['propietario', 'direccion', 'barrio', 'comida', 'ventas']
        labels = {
            'propietario': _('Ingrese el nombre'),
            'direccion': _('Ingrese la direccion'),
            'barrio': _('Seleccione  el barrio'),
            'comida': _('Ingrese el tipo de comida'),
            'ventas': _('Ingrese el valor de ventas'),
        }


class LocalRepuestoForm(ModelForm):
    class Meta:
        model = LocalRepuesto
        fields = ['propietario', 'direccion', 'barrio', 'valor', 'comida', 'ventas']
        labels = {
            'propietario': _('Ingrese el nombre'),
            'direccion': _('Ingrese la direccion'),
            'barrio': _('Seleccione el Barrio'),
            'valor': _('Ingrese el valor'),
            'comida': _('Ingrese el tipo de comida'),
            'ventas': _('Ingrese el valor de ventas'),
        }        