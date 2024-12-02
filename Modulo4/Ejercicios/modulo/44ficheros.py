#leer información de txt en una ruta relativa

ruta_archivo='./ejemploarchivo/terminar.txt'
with open(ruta_archivo,mode='r') as file:
    data=file.read()
    pass

print(data)
