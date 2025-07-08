from pedidos_cono.base import Carnivoro, Vegetariano, Saludable


class ConoFactory:
    @staticmethod
    def obtener_base(variante):
        if variante == "Carnívoro":
            cono = Carnivoro()
        elif variante == "Vegetariano":
            cono = Vegetariano()
        elif variante == "Saludable":
            cono = Saludable()
        else:
            raise ValueError("Variante de cono no válida")

        cono.inicializar()
        return cono
