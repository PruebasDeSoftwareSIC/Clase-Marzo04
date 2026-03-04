# TODO: Escribe pruebas unitarias para es_palindromo.
# Sugerencias:
# - "radar" -> True, "anita lava la tina" -> True, "python" -> False, "" -> True, "Radar" -> True

from python_app.palindromo import es_palindromo


def test_radar_es_palindromo():
    assert es_palindromo("radar")

def test_radar_mayuscula_es_palindromo():
    assert es_palindromo("Radar")

def test_anita_lava_la_tina_es_palindromo():
    assert es_palindromo("anita lava la tina")

def test_python_no_es_palindromo():
    assert not es_palindromo("python")

def test_cadena_vacia_es_palindromo():
    assert es_palindromo("")
