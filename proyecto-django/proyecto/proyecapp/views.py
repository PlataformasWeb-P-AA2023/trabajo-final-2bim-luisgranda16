from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# ejemplo de uso django-rest_framework
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from proyecapp.serializers import UserSerializer, GroupSerializer, \
BarrioSerializer, PersonaSerializer, LocalComidaSerializer, LocalRepuestoSerializer

# importar las clases de models.py
from proyecapp.models import *

# importar los formularios de forms.py
from proyecapp.forms import *

# Create your views here.
def indexCo(request):
    localComida = LocalComida.objects.all()
    diccionario = {'LocalComida': localComida, 'numero_localComida': len(localComida)}
    return render(request, 'indexCo.html', diccionario)

def indexRe(request):
    localRepuesto = LocalRepuesto.objects.all()
    diccionario = {'LocalRepuesto': localRepuesto, 'numero_localRepuesto': len(localRepuesto)}
    return render(request, 'indexRe.html', diccionario)

#
#
#

def crear_persona(request):
    if request.method=='POST':
        formulario = PersonaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(indexCo)
    else:
        formulario = PersonaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearPersona.html', diccionario)

def editar_persona(request, id):
    persona = Persona.objects.get(pk=id)
    if request.method=='POST':
        formulario = PersonaForm(request.POST, instance=persona)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(indexCo)
    else:
        formulario = PersonaForm(instance=persona)
    diccionario = {'formulario': formulario}

    return render(request, 'editarPersona.html', diccionario)

def eliminar_persona(request, id):
    persona = Persona.objects.get(pk=id)
    persona.delete()
    return redirect(indexCo)

#
#
#

def crear_barrio(request):
    if request.method=='POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(indexCo)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearBarrio.html', diccionario)

def editar_barrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(indexCo)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarBarrio.html', diccionario)

def eliminar_barrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    barrio.delete()
    return redirect(indexCo)

#
#
#

def crear_local_comida(request):
    if request.method=='POST':
        formulario = LocalComidaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(indexCo)
    else:
        formulario = LocalComidaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearLocalCo.html', diccionario)

def editar_local_comida(request, id):
    localCo = LocalComida.objects.get(pk=id)
    if request.method=='POST':
        formulario = LocalComidaForm(request.POST, instance=localCo)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(indexCo)
    else:
        formulario = LocalRepuestoForm(instance=localCo)
    diccionario = {'formulario': formulario}

    return render(request, 'editarLocalCo.html', diccionario)

def eliminar_local_comida(request, id):
    localCo = LocalComida.objects.get(pk=id)
    localCo.delete()
    return redirect(indexCo)

#
#
#

def crear_local_repuesto(request):
    if request.method=='POST':
        formulario = LocalRepuestoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(indexRe)
    else:
        formulario = LocalRepuestoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearLocalRe.html', diccionario)

def editar_local_repuesto(request, id):
    localRe = LocalRepuesto.objects.get(pk=id)
    if request.method=='POST':
        formulario = LocalRepuestoForm(request.POST, instance=localRe)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(indexRe)
    else:
        formulario = LocalRepuestoForm(instance=localRe)
    diccionario = {'formulario': formulario}

    return render(request, 'editarLocalRe.html', diccionario)

def eliminar_local_repuesto(request, id):
    localRe = LocalRepuesto.objects.get(pk=id)
    localRe.delete()
    return redirect(indexRe)

#
#
#

def ingreso(request):

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.data.get("username")
            raw_password = form.data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect(indexCo)
    else:
        form = AuthenticationForm()

    informacion_template = {'form': form}
    return render(request, 'registration/login.html', informacion_template)

def logout_view(request):
    logout(request)
    messages.info(request, "Has salido del sistema")
    return redirect(indexCo)

# crear vistas a través de viewsets
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PersonsaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [permissions.IsAuthenticated]


class BarrioViewSet(viewsets.ModelViewSet):
# class NumeroTelefonicoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocalComidaViewSet(viewsets.ModelViewSet):
# class NumeroTelefonicoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LocalComida.objects.all()
    serializer_class = LocalComidaSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocalRepuestoViewSet(viewsets.ModelViewSet):
# class NumeroTelefonicoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LocalRepuesto.objects.all()
    serializer_class = LocalRepuestoSerializer
    permission_classes = [permissions.IsAuthenticated]