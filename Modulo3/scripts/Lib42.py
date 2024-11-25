
class Usuario:
    def __init__(self,id,nombre,apellido,alias):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.alias=alias
    
    def muestra_info(self):
        print('El id del usuario es:',self.id)
        print('El nombre del usuario es:',self.nombre)
        print('El apellido del usuario es:',self.apellido)
        print('El alias del usuario es:',self.alias)

