#valor por defecto en una función

def area_circulo(radio,pi = 3.14):
    return pi*(radio**2)

aux=float(input('Ingrese el radio del círculo: '))

print('El área del círculo es_',area_circulo(aux,3.141529))
print('El área del círculo es_',area_circulo(aux))
