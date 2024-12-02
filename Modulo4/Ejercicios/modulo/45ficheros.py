#leer información de un archivo txt desde una ruta absoluta

ruta_archivo='C:/Users/Javier/OneDrive - Levo Learning Center/Negocios - asesorías/2024.11 Python, con Datux/Sesiones/Sesion4/ejemploarchivo/terminar.txt'
with open(ruta_archivo,mode='r') as file:
    data=file.read()
    pass

print(data)
