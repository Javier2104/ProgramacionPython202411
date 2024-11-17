#contador que valide hasta llegar a cero, y se detiene cuando el valor sea 2
import time

contador=int(input('Ingrese el número de conteo regresivo...'))
while contador>0:
    if contador==2:
        break
    print(contador)
    time.sleep(1)
    contador-=1
    