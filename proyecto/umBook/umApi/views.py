from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from umApi.models import Usuarios
from .serializers import *

# Create your views here.
class UsuarioViewSet(viewsets.ViewSet):
    def list(self, request): # GET ALL
        queryset = Usuarios.objects.all()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):  # GET ONE
        queryset = Usuarios.objects.all()
        usuario = get_object_or_404(queryset, pk=pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def create(self, request):  # POST
        post_data = request.data
        serializer = UsuarioCreateSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):  # UPDATE
        post_data = request.data
        usuario = Usuarios.objects.get(pk=pk)
        serializer = UsuarioUpdateSerializer(
            usuario, data=post_data, partial=True
        )  # partial te deja modificar un solo campo
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)