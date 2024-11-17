#el usuario debe adivinar el número secreto aleatorio, tiene 3 intentos
import random
valor_inicial=1
valor_final=6
vidas=5

numero_secreto=random.randint(valor_inicial,valor_final)
intento=0

while intento<vidas:
    numero_ingresado=int(input(f'Adivina el número, está entre {valor_inicial} y {valor_final}: '))
    if numero_ingresado==numero_secreto:
        print('Adivinaste el número, felicitaciones!')
        break
    else:
        intento+=1
        if intento==vidas:
            print('El juego ha terminado...')
        else:
            print('Intenta nuevamente, te queda ',vidas-intento,' intentos')
