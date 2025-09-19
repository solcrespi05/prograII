
from factory.abstract_factory.store import NYPizzaStore, ChicagoPizzaStore

# 1. NYPizzaStore crea una pizza de tipo NY Style Cheese Pizza
def test_ny_store_creates_ny_style_pizza():
    store = NYPizzaStore()
    pizza = store.order_pizza("cheese")
    assert "NY Style" in pizza.name

# 2. ChicagoPizzaStore crea una pizza de tipo Chicago Style Cheese Pizza
def test_chicago_store_creates_chicago_style_pizza():
    store = ChicagoPizzaStore()
    pizza = store.order_pizza("cheese")
    assert "Chicago Style" in pizza.name

# 3. CheesePizza de NY tiene Thin Crust Dough
def test_ny_cheese_pizza_has_correct_dough():
    store = NYPizzaStore()
    pizza = store.order_pizza("cheese")
    assert pizza.dough.name == "Thin Crust Dough"

# 4. ClamPizza de Chicago tiene Frozen Clams
def test_chicago_clam_pizza_has_frozen_clams():
    store = ChicagoPizzaStore()
    pizza = store.order_pizza("clam")
    assert pizza.clam.name == "Frozen Clams"

# 5. CheesePizza de Chicago tiene Thick Crust Dough
def test_chicago_cheese_pizza_has_correct_dough():
    store = ChicagoPizzaStore()
    pizza = store.order_pizza("cheese")
    assert pizza.dough.name == "Thick Crust Dough"
