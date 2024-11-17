#factorial usando for y range

def factorial(numero):
    aux=1
    for i in range(2,numero+1):
        aux*=i
        print(i)
    return aux

numero_factorial=int(input('Ingrese el número de factorial: '))

resultado=factorial(numero_factorial)

print(resultado)
