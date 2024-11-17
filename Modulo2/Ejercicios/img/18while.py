#el usuario debe adivinar el número secreto, tiene 3 intentos
numero_secreto=1
intento=0

while intento<3:
    numero_ingresado=int(input('Adivina el número, esta entre 0 y 4: '))
    if numero_ingresado==numero_secreto:
        print('Adivinaste el número, felicitaciones!')
        break
    else:
        intento+=1
        if intento==3:
            print('El juego ha terminado...')
        else:
            print('Intenta nuevamente, te queda ',3-intento,' intentos')
