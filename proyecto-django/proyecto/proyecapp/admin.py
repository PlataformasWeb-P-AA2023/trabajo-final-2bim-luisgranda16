from django.contrib import admin

# Register your models here.
from proyecapp.models import *

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas')
    search_fields = ('nombre', 'siglas')

admin.site.register(Barrio, BarrioAdmin)


class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cedula', 'correo')
    search_fields = ('nombre', 'apellido', 'cedula', 'correo')

admin.site.register(Persona, PersonaAdmin)


class LocalComidaAdmin(admin.ModelAdmin):
    list_display = ('propietario', 'direccion', 'barrio', 'comida', 'ventas', 'permiso')
    search_fields = ('propietario', 'direccion', 'barrio', 'comida', 'ventas', 'permiso')

admin.site.register(LocalComida, LocalComidaAdmin)

class LocalRepuestoAdmin(admin.ModelAdmin):
    list_display = ('propietario', 'direccion', 'barrio', 'valor', 'comida', 'ventas', 'permiso')
    search_fields = ('propietario', 'direccion', 'barrio', 'valor', 'comida', 'ventas', 'permiso')

admin.site.register(LocalRepuesto, LocalRepuestoAdmin)