
class Animal():
    def comunicarse(self):
        raise NotImplementedError('La subclase debe implementar el cuerpo de este método')

class Perro(Animal):
    def comunicarse(self):
        return 'Soy un perro'

class Gato(Animal):
    def comunicarse(self):
        return 'Soy un gato'
    
class Oso(Animal):
    def comunicarse(self):
        return 'Soy un oso'

animales=[Perro(),Gato(),Oso()]
for animal in animales:
    print(animal.comunicarse())
