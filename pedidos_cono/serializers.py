from rest_framework import serializers
from pedidos_cono.models import PedidosCono
from pedidos_cono.factory import ConoFactory
from pedidos_cono.builder import ConoPersonalizadoBuilder, ConoDirector
from api_patrones.logger import Logger


class PedidosConoSerializer(serializers.ModelSerializer):
    precio_total = serializers.SerializerMethodField()
    toppings_finales = serializers.SerializerMethodField()

    class Meta:
        model = PedidosCono
        fields = [
            "id",
            "cliente",
            "variante",
            "toppings",
            "tamanio_cono",
            "fecha_pedido",
            "precio_total",
            "toppings_finales",
        ]

    def get_precio_total(self, obj):
        base = ConoFactory.obtener_base(obj.variante)
        builder = ConoPersonalizadoBuilder(base)
        director = ConoDirector(builder)
        director.construir(obj.toppings, obj.tamanio_cono)

        Logger().registrar(f"Cálculo de precio para el pedido {obj.id}")
        return builder.obtener_precio()

    def get_toppings_finales(self, obj):
        base = ConoFactory.obtener_base(obj.variante)
        builder = ConoPersonalizadoBuilder(base)
        director = ConoDirector(builder)
        director.construir(obj.toppings, obj.tamanio_cono)

        Logger().registrar(f"Obtención de toppings finales para el pedido {obj.id}")
        return builder.obtener_toppings_finales()
