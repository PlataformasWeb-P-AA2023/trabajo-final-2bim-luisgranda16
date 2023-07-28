from django.contrib.auth.models import User, Group
from proyecapp.models import *

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class BarrioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Barrio
        fields = '__all__'


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class LocalComidaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocalComida
        fields = '__all__'

class LocalRepuestoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocalRepuesto
        fields = '__all__'