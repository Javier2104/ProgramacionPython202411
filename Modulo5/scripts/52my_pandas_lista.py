#creación de un dataframe a partir de una lista
import pandas as pd

lista= [
    ["Jack","Gómez",40],
    ["Felipe","Gutiérrez",50]
]

columnas=["Nombre","Apellido","Edad"]

df=pd.DataFrame(lista,columns=columnas)
print(df)
