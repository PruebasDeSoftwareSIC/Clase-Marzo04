# TODO: Escribe pruebas unitarias para suma.
# Sugerencias:
# - suma(2,3) -> 5; suma(0,5) -> 5; suma(-2,3) -> 1

from python_app.utils import suma


def test_suma_2_mas_3_es_5():
    assert suma(2, 3) == 5

def test_suma_0_mas_5_es_5():
    assert suma(0, 5) == 5

def test_suma_menos_2_mas_3_es_1():
    assert suma(-2, 3) == 1
