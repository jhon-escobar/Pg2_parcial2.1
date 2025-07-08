from django.db import models
from django.core.exceptions import ValidationError
from pedidos_cono.factory import ConoFactory
from pedidos_cono.builder import ConoPersonalizadoBuilder


class PedidosCono(models.Model):
    VARIANTES = [
        ("Carnívoro", "Carnívoro"),
        ("Vegetariano", "Vegetariano"),
        ("Saludable", "Saludable"),
    ]

    TAMANIOS = [
        ("Pequeño", "Pequeño"),
        ("Mediano", "Mediano"),
        ("Grande", "Grande"),
    ]

    cliente = models.CharField(max_length=100)
    variante = models.CharField(max_length=20, choices=VARIANTES)
    toppings = models.JSONField(default=list)
    tamanio_cono = models.CharField(max_length=10, choices=TAMANIOS)
    fecha_pedido = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Cono de {self.cliente} ({self.variante})"


# Create your models here.
