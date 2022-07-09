class Usuario:
    def __init__(self,nombre, apellido): #self es una convension que se usa entre programadores para hacer referencia a la instancia de la clase
        self.nombre=nombre
        self.apellido=apellido
    def saludo(self): 
        print("Hola, mi nombre es", self.nombre, self.apellido)

usuario=Usuario("felipe","feliz") 

usuario.saludo()
usuario.nombre="chanchito" #se pueden cambiar las instancias de una clase 
usuario.saludo() 

del usuario.nombre #se pueden eliminar propiedades de un objeto
del usuario #se puede eliminar la definicion de un objeto

