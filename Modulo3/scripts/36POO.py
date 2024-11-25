
class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def saludar(self):
        print(f'Hola mi nombre es {self.nombre} y mi edad es de {self.edad} años')

#crear dos objetos del tipo clase Persona
persona1=Persona('Liliana',28)
persona2=Persona('Diego',50)

print('El nombre de la persona1 es:',persona1.nombre)
print('La edad de la persona2 es:',persona2.edad)

persona1.saludar()
persona2.saludar()
