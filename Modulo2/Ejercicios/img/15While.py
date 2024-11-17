#contador que valide hasta llegar a cero, y se detiene en dicho número
import time

contador=int(input('Ingrese el número de conteo regresivo...'))
while contador>0:
    print(contador)
    time.sleep(1)
    contador-=1
    