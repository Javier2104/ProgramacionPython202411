class Auto:
    def __init__(self,marca,modelo):
        self.__marca=marca
        self.modelo=modelo
    
    def get_marca(self):
        return self.__marca

miAuto=Auto('Renault','Duster')
print(miAuto.modelo)
print(miAuto.get_marca())
