import pandas as pd
df=pd.read_csv('./data/winemag-data-130k-v2.csv')
#print(df.head(5))
#print(df['country'].head(5))

#seleccionar columnas
columns_selected=['country','province']
df_subset=df[columns_selected]
#print(df_subset)

#renombrar nombres de columnas
df_renamed=df.rename(columns={'Unnamed: 0':'Index'})
#print(df_renamed)

#borrar columnas
df_drop=df.drop(['Unnamed: 0'],axis=1)
#print(df_drop)

#filtrar filas
condicion=(df['country']=='Peru')
df_filter=df[condicion]
#print(df_filter)

condicion2=(df.country=='Italy') & (df.points>=90)
#print(df[condicion2].head(5))

#obtener combinaciones únicas de columnas
df_resumen=df_filter[['country','winery','variety']].drop_duplicates(subset=['country','winery','variety'])
#print(df_resumen)

#nuevas columnas
df['new_price']=df.price*1.2
#print(df.head())

def etiqueta_precio(precio:float):
    if precio<100:
        return 'Precio accesible'
    elif precio<500 and precio>=100:
        return 'Precio moderadamente alto'
    elif precio>=500:
        return 'Precio alto'
    else:
        return None
    
df['etiqueta_precio']=df.price.apply(etiqueta_precio)
#print(df.head())

def incremento_por_pais(row):
    if row.country=='Italy':
        return row.price*1.5
    else:
        return row.price

df['increase_by_country']=df.apply(incremento_por_pais,axis='columns')
#print(df.head())

#agrupar valores
condicion3=(df.country=='Portugal')
df_group=df[condicion3].groupby(['country','province']).agg(
    {
        'points': ['mean','min','max'],
        'price': ['mean','min','max']
    }
).sort_values(by=[('points','mean'),('price','max')],ascending=[False,False])

#print(df_group.head())


#combinar dataframes
#df1=df_filter #registros de Perú
#df2=df[condicion3] #registros de Portugal

condicion4=(df.country=='Peru')
df1=df[condicion4]
condicion5=(df.country=='Portugal')
df2=df[condicion5]
df3=pd.concat([df1,df2],axis=0)
df4=df3[['country','province']].drop_duplicates(subset=['country','province'])
df5=df4.reset_index(drop=True)
print(df5.head)

