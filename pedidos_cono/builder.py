class ConoPersonalizadoBuilder:
    def __init__(self, base_cono):
        self.base = base_cono
        self.precio = base_cono.precio_base()
        self.ingredientes = list(base_cono.obtener_toppings_base())

    def agregar_topping(self, topping):
        precios = {
            "queso_extra": 2,
            "papas_al_hilo": 1,
            "salchicha_extra": 2.5,
            "guacamole": 1.5,
            "jalapeños": 1,
        }
        if topping not in precios:
            raise ValueError(f"Topping '{topping}' no válido.")
        self.ingredientes.append(topping)
        self.precio += precios[topping]

    def ajustar_tamanio(self, tamanio):
        if tamanio == "Mediano":
            self.precio *= 1.25
        elif tamanio == "Grande":
            self.precio *= 1.5

    def obtener_precio(self):
        return round(self.precio, 2)

    def obtener_toppings_finales(self):
        return self.ingredientes


class ConoDirector:
    def __init__(self, builder):
        self.builder = builder

    def construir(self, toppings, tamanio):
        for t in toppings:
            self.builder.agregar_topping(t)
        self.builder.ajustar_tamanio(tamanio)
