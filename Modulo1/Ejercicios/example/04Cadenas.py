#buscar subcadena dentro de una cadena de texto y devolver la posición

mensaje='Bienvenidos alumnos al curso de Python'
buscar='Python'
posicion=mensaje.find(buscar)
#print('La palabra buscada está en la posición',posicion)
print(f'La palabra buscada "{buscar}" está en la posición {posicion}')
