class ConoBase:
    def __init__(self):
        self.ingredientes = []
        self.precio = 0

    def inicializar(self):
        raise NotImplementedError()

    def obtener_toppings_base(self):
        return self.ingredientes

    def precio_base(self):
        return self.precio


class Carnivoro(ConoBase):
    def inicializar(self):
        self.ingredientes = ["pollo", "queso"]
        self.precio = 20


class Vegetariano(ConoBase):
    def inicializar(self):
        self.ingredientes = ["vegetales", "tofu"]
        self.precio = 18


class Saludable(ConoBase):
    def inicializar(self):
        self.ingredientes = ["ensalada", "frijoles"]
        self.precio = 15
