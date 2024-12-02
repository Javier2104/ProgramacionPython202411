#crear un CRUD

import os
import time
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pruebaperu"
)

mycursor=mydb.cursor()

while True:
    print('---MENU---\n'
          '1. Insertar un producto\n'
          '2. Eliminar un producto\n'
          '3. Buscar un producto\n'
          '4. Actualizar un producto\n'
          '5. Mostrar la lista de productos\n'
          '6. Salir del sistema'
          )
    opcion=int(input('Elige una opción del menú: '))
    if opcion==1:
        clave=int(input('Escribe la clave del producto: '))
        nombre=input('Escribe el nombre del producto: ')
        costo=float(input('Escribe el costo del producto: '))
        sql='insert into productos (clave,nombre,costo) values (%s,%s,%s)'
        val=(clave,nombre,costo)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount,'Registro insertado en la BD')
        time.sleep(3)
        os.system('cls')
    elif opcion==2:
        clave=int(input('Escriba la clave del producto a eliminar: '))
        sql='delete from productos where clave=%s'
        val=(clave,)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount,'Registro eliminado en la BD')
        time.sleep(3)
        os.system('cls')
    elif opcion==3:
        clave=int(input('Escriba la clave del producto a buscar: '))
        sql='select * from productos where clave=%s'
        val=(clave,)
        mycursor.execute(sql,val)
        myresult=mycursor.fetchone()
        if myresult:
            print('Sí tenemos ese producto')
        else:
            print('Lo sentimos, producto agotado')
        time.sleep(3)
        os.system('cls')
    elif opcion==4:
        clave=int(input('Escribe la clave del producto a modificar: '))
        nombre=input('Escribe el nuevo nombre del producto: ')
        costo=float(input('Escribe el nuevo costo del producto: '))
        sql='update productos set nombre=%s,costo=%s where clave=%s'
        val=(nombre,costo,clave)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount,'Registro actualizado en la BD')
        time.sleep(3)
        os.system('cls')
    elif opcion==5:
        mycursor.execute('select * from productos')
        myresult=mycursor.fetchall()
        print('La lista de productos es:')
        for x in myresult:
            print(x)
        time.sleep(7)
        os.system('cls')
    elif opcion==6:
        print('Saliendo del sistema...')
        time.sleep(2)
        os.system('cls')
        break
    else:
        print('Opción no válida, intenta de nuevo..')
        time.sleep(2)
        os.system('cls')
