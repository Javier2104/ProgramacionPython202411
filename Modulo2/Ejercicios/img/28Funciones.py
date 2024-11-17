#cálculo del área de un rectángulo

def area(base,altura):
    return base*altura

aux1=float(input('Ingrese la base del rectángulo: '))
aux2=float(input('Ingrese la altura del rectángulo: '))

print('El área del rectángulo es: ',area(aux1,aux2))
