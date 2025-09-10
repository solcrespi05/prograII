from abc import ABC, abstractmethod

# Clase base: cualquier bebida
class Bebida(ABC):
    def __init__(self, descripcion="Bebida desconocida", tamanio="chico"):
        self._descripcion = descripcion
        self._tamanio = tamanio

    def obtener_descripcion(self):
        return self._descripcion
    
    def set_size(self, size):
        self._tamanio = size

    def get_size(self):
        return self._tamanio

    @abstractmethod
    def costo(self):
        pass


# Bebidas 
class Espresso(Bebida):
    def __init__(self):
        super().__init__("Espresso", "chico")

    def costo(self):
        if self.get_size() == "chico":
                    return 2.00
        elif self.get_size() == "mediano":
                    return 2.50
        elif self.get_size() == "grande":
            return 3.00
        else:
            return 2.00
    


class CafeNegro(Bebida):
    def __init__(self):
        super().__init__("Cafe Negro", "chico")

    def costo(self):
        if self.get_size() == "chico":
                    return 1.50
        elif self.get_size() == "mediano":
                    return 2.00
        elif self.get_size() == "grande":
            return 2.50
        else:
            return 1.50


class CafeDeLaCasa(Bebida):
    def __init__(self):
        super().__init__("Cafe de la Casa", "chico")

    def costo(self):
        if self.get_size() == "chico":
                    return 1.20
        elif self.get_size() == "mediano":
                    return 1.70
        elif self.get_size() == "grande":
            return 2.20
        else:
            return 1.20


