#insertar información en un txt

data_a_insertar=['Primera línea\n'
                 ,'Segunda línea\n'
                 ,"Tercera línea"
                 ]

with open('./ejemploarchivo/prueba.txt',mode='w') as f:
    f.writelines(data_a_insertar)

f.close()

data=open('./ejemploarchivo/prueba.txt',mode='r').read()
print(data)
f.close()
