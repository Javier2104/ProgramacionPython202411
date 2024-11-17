#función con parámetros

def Funcion(texto):
    return texto[::-1]

frase=input('Ingresa la frase a invertir: ')
frase_a_invertir=Funcion(frase)
print(frase_a_invertir)
