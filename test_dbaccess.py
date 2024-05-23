import pytest
import dbaccess as dba
from constantes import DB_TABLES

def test_crear_conexion_existe():
    dba_attrs = dir(dba)
    assert 'crear_conexion' in dba_attrs
    
def test_ejecutar_consulta_existe():
    dba_attrs = dir(dba)
    assert 'ejecutar_consulta' in dba_attrs
    
def test_cargar_usuario_existe():
    dba_attrs = dir(dba)
    assert 'cargar_usuario' in dba_attrs
    
def test_existe_jugador_existe():
    dba_attrs = dir(dba)
    assert 'existe_jugador' in dba_attrs
    
def test_cargar_jugada_existe():
    dba_attrs = dir(dba)
    assert 'cargar_jugada' in dba_attrs
    
def test_obtener_palabras_jugadas_existe():
    dba_attrs = dir(dba)
    assert 'obtener_palabras_jugadas' in dba_attrs
    
def test_obtener_palabra_azar_existe():
    dba_attrs = dir(dba)
    assert 'obtener_palabra_azar' in dba_attrs
