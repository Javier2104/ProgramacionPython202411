#promedio de dos números, validando el input ingresado por el usuario
try:
    p1=int(input('Ingrese el valor del primer número: '))
    p2=int(input('Ingrese el valor del segundo número: '))
    promedio=(p1+p2)/2
    print('El promedio de los números ingresados es ',promedio)
except:
    print('Ingrese un valor válido')
else:
    print('El código se ejecutó correctamente')
finally:
    print('Usaste esta funcionalidad de promedio')
