#actividad 3

import sqlite3
from sqlite3 import Error

def conexion(filename = ":memory:"):
    try:
        con = sqlite3.connect(filename)
        print("Conexion realizada a ", filename)
    except Error:
        print(Error)
        con = None 
    finally:
        return con
  

def create(con, sentencia):
    try:
        cur = con.cursor()
        
        cur.execute(sentencia)
        
        con.commit()
        
        print("Tabla creada")
    
    except sqlite3.OperationalError:
        print("La tabla ya existia")
        
    
def insert(con, insertar):
    try:
        
        cur = con.cursor()
        
        cur.execute(insertar)
        con.commit()    
        
        print("Registro actualizado")
        
    except sqlite3.IntegrityError:
        print("Ya existe ese registro")


def select(con, select):
    try:
        
        cur = con.cursor()
        
        cur.execute(select)
        row = cur.fetchall()
    
        print(row)
    
    except sqlite3.OperationalError:
        print("Algo salio mal")


def _del_(con):
    con.close()
