#el usuario ingresará números, y el programa se detendrá cuando el usuario ingrese cero

suma=0
numero=1

while numero!=0:
    numero=int(input('Ingrese un número: '
                     'Ingrese 0 para salir'))
    suma+=numero

print(f'La suma de los números introducidos es: {suma}')
