#leer información de csv e insertarlo en un archivo txt

ruta_archivo='./ejemploarchivo/data.csv'
with open(ruta_archivo) as file:
    lineas=file.readlines()
    pass
print(lineas)

diccionario={}
for linea in lineas:
    producto,cantidad,precio_unitario=linea.strip().split(',')
    cantidad=int(cantidad)
    precio_unitario=float(precio_unitario)

    if not producto in diccionario.keys():
        diccionario[producto]={'cantidad':cantidad,'precio_unitario':precio_unitario}

    pass

for producto,data in diccionario.items():
    diccionario[producto]['precio_total']=data['cantidad']*data['precio_unitario']

#print(diccionario)

ruta_txt='./ejemploarchivo/prueba.txt'
with open(ruta_txt,mode='w') as file:
    for producto, data in diccionario.items():
        linea = f'Producto: {producto},  Precio Total: {data["precio_total"]}\n'
        file.write(linea)
file.close()

data=open('./ejemploarchivo/prueba.txt',mode='r').read()
print(data)

