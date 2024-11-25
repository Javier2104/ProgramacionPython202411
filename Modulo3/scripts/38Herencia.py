#super clase o clase padre

class Animal:
    def __init__(self,nombre):
        self.nombre=nombre
    
    def comer(self):
        print(f'{self.nombre} está comiendo')

#subclase, clase derivada o hija

class Perro(Animal):
    def __init__(self, nombre,raza):
        super().__init__(nombre)
        self.raza=raza
    
    def ladrar(self):
        print(f'{self.nombre} es de raza {self.raza} y está ladrando')

miPerro=Perro('Simba','labrador')
miPerro.comer()
miPerro.ladrar()
