from django.shortcuts import render

# Create your views here.

# Python native imports
from datetime import timedelta

# External imports
from rest_framework import viewsets
from django.utils import timezone as tz

# Local imports
from pedidos_cono.serializers import *
from pedidos_cono.models import *
from django.conf import settings


class PedidosConoViewSet(viewsets.ModelViewSet):
    queryset = PedidosCono.objects.all()
    serializer_class = PedidosConoSerializer


# Create your views here.
