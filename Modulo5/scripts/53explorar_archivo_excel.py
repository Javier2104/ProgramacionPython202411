import pandas as pd
path="./data/cripto_currency.xlsx"

df=pd.read_excel(path,sheet_name='BTC-USD')
print(df)
