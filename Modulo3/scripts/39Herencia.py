
class Figura():
    def __init__(self,color):
        self.color=color
    
    def dibujar(self):
        print('Estamos dibujando una figura de color',self.color)

class Rectangulo(Figura):
    def __init__(self, color,ancho,alto):
        super().__init__(color)
        self.ancho=ancho
        self.alto=alto
    
    def calcular_area(self):
        return self.ancho*self.alto

class Circulo(Figura):
    def __init__(self, color,radio):
        super().__init__(color)
        self.radio=radio
    
    def calcular_area(self):
        return 3.14*(self.radio**2)

miRectangulo=Rectangulo('Azul',8,6)
miCirculo=Circulo('Blanco',10)

miRectangulo.dibujar()
print('El color del rectángulo es',miRectangulo.color)
print('El área del rectángulo es',miRectangulo.calcular_area())

miCirculo.dibujar()
print('El color del círculo es',miCirculo.color)
print('El área del círculo es',miCirculo.calcular_area())
