
#  Creamos la clase perro
class Perro:
    # método constructor
    # nos permite inicializar los atributos de la clase
    # self es una referencia a la instancia de la clase
    def __init__(self, nombre, color, raza) -> None:
        self.nombre = nombre
        self.color = color
        self.raza = raza
        

    # métodos de la clase, son funciones que pertenecen a la clase
    def ladrar(self):
        print("Guau Guau")
        

    def oler(self):
        print("Sniff Sniff")
        

    def dormir(self):
        print("Zzzzzzz")
        

    def imprimir(self):
        print(f"Perro {self.nombre} de raza {self.raza} y color {self.color}")
        
perro1=Perro('Firulais','negro','pastor alemán')

#print(perro1)
perro1.ladrar()
perro1.oler()
perro1.dormir()
perro1.imprimir()
