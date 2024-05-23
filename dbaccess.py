from typing import List
import mysql.connector as db
from constantes import DB_HOSTNAME,DB_DATABASE,DB_PASSWORD,DB_USERNAME

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
