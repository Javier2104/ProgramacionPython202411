import Lib42

class UsuarioPremium(Lib42.Usuario):
    def __init__(self, id, nombre, apellido, alias,puntos,sorteos):
        super().__init__(id, nombre, apellido, alias)
        self.puntos=puntos
        self.sorteos=sorteos
    
    def muestra_info(self):
        super().muestra_info()
        print(f'Tienes {self.puntos} puntos para canjear en premios')
        print(f'Tienes derecho a participar en {self.sorteos} sorteos')

id=input('Ingresa el id del usuario: ')
nombre=input('Ingresa el nombre del usuario: ')
apellido=input('Ingresa el apellido del usuario: ')
alias=input('Ingresa el alias del usuario: ')
sorteos=25
puntos=500

userPremium=UsuarioPremium(id,nombre,apellido,alias,sorteos,puntos)
userPremium.muestra_info()
