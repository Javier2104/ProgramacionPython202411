#promedio de calificaciones de un alumno, considerando examen parcial, final y notas de práctica

nombre=input('Escribe tu nombre: ')
pc1=float(input('Escribe tu nota de práctica 1: '))
pc2=float(input('Escribe tu nota de práctica 2: '))
pc3=float(input('Escribe tu nota de práctica 3: '))
promediopc=round((pc1+pc2+pc3)/3,2)
exparcial=float(input('Escribe tu nota de examen parcial: '))
exfinal=float(input('Escribe tu nota de examen final: '))
promediofinal=round((0.2*promediopc+0.3*exparcial+0.5*exfinal),2)
print(f'{nombre}, el promedio final es: {promediofinal}')
