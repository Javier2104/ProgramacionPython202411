#factorial de un número con función recursiva

def funcion_recursiva(numero):
    if numero==1:
        return numero
    else:
        return numero*funcion_recursiva(numero-1)

numero_factorial=int(input('Ingrese el número de factorial: '))

resultado=funcion_recursiva(numero_factorial)

print(resultado)
