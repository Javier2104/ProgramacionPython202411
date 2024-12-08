#guardar la data de cada país  de csv "winemag" en un excel distinto

import pandas as pd
df=pd.read_csv('./data/winemag-data-130k-v2.csv')
#print(df.country.unique())

for pais in df.country.unique():
    condicion=(df.country==pais)
    df_filter=df[condicion]
    df_filter.to_excel(f'./data/vinos/{pais}.xlsx',index=False)
    print(f'{pais}, {df_filter.shape}')
