#mostrar los valores de una lista, cada cierto tiempo
import time
for i in [1,2,3,4]:
    print(f'Habrá un retardo de {i} segundos')
    time.sleep(i)
