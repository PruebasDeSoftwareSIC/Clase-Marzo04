# TODO: Escribe pruebas unitarias para es_palindromo.
# Sugerencias:
# - "radar" -> True, "anita lava la tina" -> True, "python" -> False, "" -> True, "Radar" -> True

from python_app.palindromo import es_palindromo

def test_radar_es_palindromo():
    assert es_palindromo("radar") == True

def test_radar_mayuscula_es_palindromo():
    assert es_palindromo("Radar") == True

def test_anita_lava_la_tina_es_palindromo():
    assert es_palindromo("anita lava la tina") == True

def test_python_no_es_palindromo():
    assert es_palindromo("python") == False

def test_cadena_vacia_es_palindromo():
    assert es_palindromo("") == True
