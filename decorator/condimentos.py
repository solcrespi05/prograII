from abc import ABC, abstractmethod
from bebidas import Bebida

# Decorador base: cualquier condimento envuelve una bebida
class CondimentoDecorador(Bebida, ABC):
    def __init__(self, bebida):
        self.bebida = bebida

    def set_size(self, size):
        """Delegar el cambio de tamaño a la bebida envuelta"""
        self.bebida.set_size(size)
    
    def get_size(self):
        """Delegar la obtención del tamaño a la bebida envuelta"""
        return self.bebida.get_size()

    @abstractmethod
    def obtener_descripcion(self):
        pass


# --- Condimentos concretos ---
class Mocha(CondimentoDecorador):  # chocolate
    def obtener_descripcion(self):
        return f"{self.bebida.obtener_descripcion()}, Mocha"

    def costo(self):
        return self.bebida.costo() + 0.30


class Crema(CondimentoDecorador):  # crema batida
    def obtener_descripcion(self):
        return f"{self.bebida.obtener_descripcion()}, Crema"

    def costo(self):
        return self.bebida.costo() + 0.20


class Soja(CondimentoDecorador):  # leche de soja
    def obtener_descripcion(self):
        return f"{self.bebida.obtener_descripcion()}, Soja"

    def costo(self):
        return self.bebida.costo() + 0.25

class Caramelo(CondimentoDecorador):
    def obtener_descripcion(self):
        return f"{self.bebida.obtener_descripcion()}, Caramelo"
    
    def costo(self):
        return self.bebida.costo() + 0.20

class DobleMocha(CondimentoDecorador):
    def obtener_descripcion(self):
        return f"{self.bebida.obtener_descripcion()}, Doble Mocha"
    
    def costo(self):
        return self.bebida.costo() + 0.60
    