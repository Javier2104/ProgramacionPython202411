#clase Triángulo con una función para calcular su área

class Triangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    
    def area(self):
        return self.base*self.altura/2

    #Tipo de triángulo: agudo, recto u obtuso
    
    def set_tipo(self,tipo):
        self.tipo=tipo
    
    def __str__(self) ->str:
        if hasattr(self,"tipo"):
            return f"Triángulo de base {self.base} de tipo {self.tipo}"
        else:
            return f"No tiene tipo definido de triángulo"

valor1=float(input('Ingrese la base del triángulo: '))
valor2=float(input('Ingrese la altura del triángulo: '))

triangulo1=Triangulo(valor1,valor2)
print('El área del triángulo es:',triangulo1.area())

triangulo1.set_tipo('Agudo')
print(triangulo1)
