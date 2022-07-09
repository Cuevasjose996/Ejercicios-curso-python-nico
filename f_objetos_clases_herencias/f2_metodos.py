class Usuario:
    def __init__(self,nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
    def saludo(self): #los metodos, no es mas que una funcion dentro de una clase, la cual indica que acciones que pueden realizar los parametros definidos al crear un objeto.
        print("Hola, mi nombre es", self.nombre, self.apellido)
usuario=Usuario("felipe","feliz") 
usuario2=Usuario("chanchito","feliz")

usuario.saludo()
usuario2.saludo()

