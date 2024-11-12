#promedio de calificaciones de un alumno, con validaciones de tipo de dato y rango de 0 a 20 para cada nota

try:
    pc1=float(input('Escribe tu nota de práctica 1: '))
    if pc1>=0 and pc1<=20:
        pc2=float(input('Escribe tu nota de práctica 2: '))
        if pc2>=0 and pc2<=20:
            pc3=float(input('Escribe tu nota de práctica 3: '))
            if pc3>=0 and pc3<=20:
                promediopc=round((pc1+pc2+pc3)/3,2)
                print('El promedio de tus notas de práctica es :',promediopc)
            else:
                print(f'Ingresa un valor válido de pc3')
        else:
            print(f'Ingresa un valor válido de pc2')
    else:
        print(f'Ingresa un valor válido de pc1')
except:
    print(f'Ingresa un valor válido')
