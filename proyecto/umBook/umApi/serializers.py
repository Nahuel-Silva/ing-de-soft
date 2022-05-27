from umApi.models import Usuarios
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta():
        model = Usuarios
        fields = '__all__'



class UsuarioCreateSerializer(serializers.ModelSerializer):

    class Meta():
        model = Usuarios
        fields = ('nombre','apellido','usuario', 'email', 'contraseña',)



class UsuarioUpdateSerializer(serializers.ModelSerializer):

    class Meta():
        model = Usuarios
        fields = ('nombre','apellido', 'email', 'contraseña',)