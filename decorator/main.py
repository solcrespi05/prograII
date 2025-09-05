from bebidas import Bebida, Espresso, CafeNegro, CafeDeLaCasa
from condimentos import Mocha, Crema, Soja, Caramelo, DobleMocha

def builder(base, size="chico", condimentos=None):
    """
    podes hacer la bebida en una sola línea
    """
    bebida = base()
    bebida.set_size(size)

    if condimentos:
        for cond in condimentos:
            bebida = cond(bebida)

    return bebida


def mostrar_pedido(bebida: Bebida) -> None:
    print(f"{bebida.obtener_descripcion()} ({bebida.get_size()}) -> ${bebida.costo():.2f}")

if __name__ == "__main__":
    # Ejemplo 1: Espresso solo
    cafe1: Bebida = Espresso()
    mostrar_pedido(cafe1)

    # Ejemplo 2: Café Negro con 2 Mocha y Crema
    cafe2: Bebida = CafeNegro()   # la variable es de tipo Bebida, listo
    cafe2 = Mocha(cafe2)          # le pongo un Mocha
    cafe2 = Mocha(cafe2)          # otro Mocha más
    cafe2 = Crema(cafe2)          # y crema por arriba
    mostrar_pedido(cafe2)

    # Ejemplo 3: Café de la Casa con Soja y Crema
    cafe3: Bebida = CafeDeLaCasa()
    cafe3.set_size("")
    cafe3 = Soja(cafe3)
    cafe3 = Crema(cafe3)
    mostrar_pedido(cafe3)

    #Ejemplo 4: Cafe de al casa grande con Doble Mocha y Caramelo
    cafe4: Bebida = CafeDeLaCasa()
    cafe4.set_size("grande")
    cafe4 = DobleMocha(cafe4)
    cafe4 = Caramelo(cafe4)
    mostrar_pedido(cafe4) 

    #Ejemplo del builder
    cafe5: Bebida = builder(Espresso, "grande", [Mocha, Crema])
    mostrar_pedido(cafe5)
