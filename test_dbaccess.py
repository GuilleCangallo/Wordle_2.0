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

@pytest.fixture
def conn_fixture():
    pytest.dbconn = dba.crear_conexion()
    
@pytest.mark.usefixtures("conn_fixture")
def test_crear_conexion():
    conn = pytest.dbconn
    assert conn
    
@pytest.mark.usefixtures("conn_fixture")
@pytest.mark.parametrize('tabla', DB_TABLES)
def test_chequear_tabla(tabla):
    resultado = dba.ejecutar_consulta(pytest.dbconn, "SHOW TABLES LIKE %s", (tabla,), fetch=True)
    assert len(resultado) == 1

#Se crea anteriormente un registro en la tabla jugadores que tenga como nombre "Pedro",
# y luego se ejecuta el siguiente test:    
@pytest.mark.usefixtures("conn_fixture") 
def test_cargar_usuario_fallido():
    resultado = dba.cargar_usuario(pytest.dbconn, "Pedro")
    assert resultado == False
    
@pytest.mark.usefixtures("conn_fixture")
def test_cargar_usuario_exitoso():
    dba.cargar_usuario(pytest.dbconn, "Juan")

@pytest.mark.usefixtures("conn_fixture")
def test_cargar_jugada_fallida_intentos():
    resultado = dba.cargar_jugada(pytest.dbconn, "Pedro", 2, 7)
    assert resultado == False
    
@pytest.mark.usefixtures("conn_fixture")
def test_cargar_jugada_fallida_jugador_inexistente():
    resultado = dba.cargar_jugada(pytest.dbconn, "", 5, 6)
    assert resultado == False
    
@pytest.mark.usefixtures("conn_fixture")
def test_cargar_jugada():
    resultado = dba.cargar_jugada(pytest.dbconn, "Pedro", 4, 4)
    assert resultado == True
