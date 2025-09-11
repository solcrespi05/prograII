from builder import builder
from bebidas import Bebida, CafeNegro, CafeDeLaCasa, Espresso
from condimentos import Mocha, Crema, Soja, Caramelo, DobleMocha

def test_espresso():
    b = Espresso()
    b.set_size("mediano")
    assert abs(b.costo() - 2.50) < 1e-9
    assert b.obtener_descripcion() == "Espresso"

def test_cafe_negro_mocha_crema():
    b = CafeNegro()
    b.set_size("grande")
    b = Mocha(b)
    b = Mocha(b)
    b = Crema(b)
    assert abs(b.costo() - 3.30) < 1e-9
    assert b.obtener_descripcion() == "Cafe Negro, Mocha, Mocha, Crema"

def test_casa_soja_crema():
    b = CafeDeLaCasa()
    b.set_size("mediano")
    b = Soja(b)
    b = Crema(b)
    assert "Soja" in b.obtener_descripcion()
    assert "Crema" in b.obtener_descripcion()

def test_casa_doblemocha_caramelo():
    b = CafeDeLaCasa()
    b.set_size("grande")
    b = DobleMocha(b)
    b = Caramelo(b)
    assert "Doble Mocha" in b.obtener_descripcion()
    assert "Caramelo" in b.obtener_descripcion()

def test_builder():
    b = builder(CafeNegro, "grande", [Mocha, Mocha, Crema])
    desc = b.obtener_descripcion()
    assert desc == "Cafe Negro, Mocha, Mocha, Crema"

if __name__ == "__main__":
    test_espresso()
    test_cafe_negro_mocha_crema()
    test_casa_soja_crema()
    test_casa_doblemocha_caramelo()
    test_builder()
    print("Todos los tests pasaron ✅")