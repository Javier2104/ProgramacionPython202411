import pandas as pd

#combinar dataframes en base a columnas
df1=pd.read_csv('./data/air_quality_no2_long.csv')
df2=pd.read_csv('./data/air_quality_pm25_long.csv')
df3=pd.read_csv('./data/air_quality_stations.csv')

df_quality=pd.concat([df1,df2],axis=0).reset_index(drop=True)
#print(df_quality.location.unique())

df4=df3.drop_duplicates(subset=['location'])
#print(df4.shape)

df_vf=pd.merge(df_quality,df4,how="inner",on="location")
print(df_vf)


#exportar a excel
df_vf.to_excel('./data/df_vf.xlsx',index=False)
