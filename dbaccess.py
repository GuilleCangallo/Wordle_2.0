from typing import List
import mysql.connector as db
from constantes import DB_HOSTNAME,DB_DATABASE,DB_PASSWORD,DB_USERNAME
import random

def crear_conexion() -> db.pooling.PooledMySQLConnection | db.MySQLConnection:
    return db.connect(
        host=DB_HOSTNAME,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        database=DB_DATABASE
    )
    
def ejecutar_consulta(conn : db.MySQLConnection, consulta : str, parametros=(), fetch=False):   
    cursor = conn.cursor()
    cursor.execute(consulta, parametros)
    if fetch:
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultado
    else:
        conn.commit()
        cursor.close()
        conn.close()

def cargar_usuario(dbconn, nombre):
    ejecutar_consulta(dbconn, "INSERT INTO jugadores (nombre) VALUES (%s)", (nombre,))
    
def existe_jugador(dbconn, nombre):
    resultado = ejecutar_consulta(dbconn, "SELECT id FROM jugadores WHERE nombre = %s", (nombre,), fetch=True)
    return len(resultado) > 0

def cargar_jugada(dbconn, nombre_jugador, palabra_id, intentos):
    if not existe_jugador(dbconn, nombre_jugador) or intentos > 6:
        return False
    jugador_id = ejecutar_consulta(dbconn, "SELECT id FROM jugadores WHERE nombre = %s", (nombre_jugador,), fetch=True)
    ejecutar_consulta(dbconn, "INSERT INTO jugadas (palabra, jugador, intentos) VALUES (%s, %s, %s)", (palabra_id, jugador_id, intentos))

def obtener_palabras_jugadas(dbconn, nombre_jugador):
    jugador_id = ejecutar_consulta(dbconn, "SELECT id FROM jugadores WHERE nombre = %s", (nombre_jugador,), fetch=True)
    return [palabra[0] for palabra in ejecutar_consulta("SELECT id FROM jugadas WHERE jugador = %s", (jugador_id,), fetch=True)]
    
def obtener_palabra_azar(dbconn, ids_excluidos):
    consulta = "SELECT id FROM jugadores WHERE id NOT IN (%s)" & ',' .join(['%s'] * len(ids_excluidos))
    palabras_disponibles = [palabra[0] for palabra in ejecutar_consulta(dbconn, consulta, ids_excluidos, fetch=True)]
    return random.choice(palabras_disponibles) if palabras_disponibles else None
