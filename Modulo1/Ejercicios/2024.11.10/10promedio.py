#promedio de calificaciones de un alumno

nombre=input('Escribe tu nombre: ')
pc1=float(input('Escribe tu nota de práctica 1: '))
pc2=float(input('Escribe tu nota de práctica 2: '))
pc3=float(input('Escribe tu nota de práctica 3: '))
promediopc=round((pc1+pc2+pc3)/3,2)
print(nombre,', el promedio de tus notas de práctica es :',promediopc)
