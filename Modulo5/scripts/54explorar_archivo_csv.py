import pandas as pd
df=pd.read_csv('./data/titanic.csv',sep=',')

#print(df) #muestra la data del dataframe
#print(df.shape) #muestra la cantidad de filas y columnas del dataframe
#print(df.head(2)) #muestra las primeras n filas
#print(df.tail(3)) #muestra las últimas n filas
#print(df.dtypes) #muestra los tipos de valor de cada columna del dataframe
#print(df.columns) #muestra el nombre de las columnas del dataframe
#print(df.describe) #muestra la data del dataframe
#print(df.describe()) #muestra valores estadísticos de las columnas numéricas
#print(df.info) #similar a describe
#print(df.isnull()) #validación de si el valor de cada celda es nulo o no
print(df.isnull().mean()) #resumen de la cantidad de valores nulos por cada columna
