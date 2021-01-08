#actividad 3

from Tema_4.db_class import create, conexion, insert, select, _del_

archivo = input("Dime el nombre del archivo y la extension ")

con = conexion(archivo)
cur = con.cursor()

c = True

while c: 
    sentencia = input("Escribe la sentencia de creacion de tablas a ejecutar ")

    create(con, sentencia)
    respuesta = input("Si desea crear otra tabla escriba si " )
    
    if respuesta != "si":
        c = False

c = True

while c: 
    insertar = input("Escribe la sentencia de insert ")

    insert(con, insertar)
    respuesta = input("Si desea realizar otro insert escriba si " )
    
    if respuesta != "si":
        c = False


c = True

while c: 
    selecccion = input("Escribe la sentencia de select ")

    select(con, selecccion)
    respuesta = input("Si desea realizar otro select escriba si " )
    
    if respuesta != "si":
        c = False


_del_(con)



