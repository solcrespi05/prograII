from abc import ABC, abstractmethod

# Clase base: cualquier bebida
class Bebida(ABC):
    def __init__(self, descripcion="Bebida desconocida"):
        self._descripcion = descripcion

    def obtener_descripcion(self):
        return self._descripcion

    @abstractmethod
    def costo(self):
        pass


# --- Bebidas concretas ---
class Espresso(Bebida):
    def __init__(self):
        super().__init__("Espresso")

    def costo(self):
        return 2.00


class CafeNegro(Bebida):
    def __init__(self):
        super().__init__("Cafe Negro")

    def costo(self):
        return 1.50


class CafeDeLaCasa(Bebida):
    def __init__(self):
        super().__init__("Cafe de la Casa")

    def costo(self):
        return 1.20
