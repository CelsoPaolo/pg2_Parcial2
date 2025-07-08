from django.shortcuts import render
from rest_framework import viewsets
from apiconos.models import PedidoCono
from apiconos.serializers import PedidoConoSerializer

class PedidoConoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para el modelo PedidoCono, proporcionando operaciones CRUD
    a través de la API REST.
    """
    queryset = PedidoCono.objects.all().order_by("-fecha_pedido")
    serializer_class = PedidoConoSerializer