import pytest
import wordle as w

def test_encontrar_letra_palabra_existe():
    w_attrs = dir(w)
    assert 'encontrar_letra_palabra' in w_attrs
    
def test_comparar_palabras_existe():
    w_attrs = dir(w)
    assert 'comparar_palabras' in w_attrs
