#leer data de tipo de cambio en una api, e insertarlo en un txt

import requests

url="https://api.apis.net.pe/v1/tipo-cambio-sunat?month=11&year=2024"
data=requests.get(url)
datajson=data.json()
#print(datajson[0])

ruta_txt='./ejemploarchivo/prueba.txt'
with open(ruta_txt,mode='w') as file:
    for linea in datajson:
        aux=f'Compra: {linea['compra']}, Venta: {linea['venta']}, Fecha: {linea['fecha']}\n'
        file.write(aux)
file.close()

data=open('./ejemploarchivo/prueba.txt','r').read()
print(data)
