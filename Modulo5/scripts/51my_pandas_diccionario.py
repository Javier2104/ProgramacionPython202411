import pandas as pd
#print(pd.__version__)

#crear un dataframe a partir de un diccionario

dicx= {
    "Nombre": ["Ana","María","Isabel","Juliana"],
    "Edad": [21,30,40,None],
    "Género": ["Femenino","Femenino",None,None]
}

df=pd.DataFrame(dicx)
print(df)
