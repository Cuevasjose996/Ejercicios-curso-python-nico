class Usuario:
    def __init__(self,nombre, apellido): #self es una convension que se usa entre programadores para hacer referencia a la instancia de la clase
        self.nombre=nombre
        self.apellido=apellido
    def saludo(self): 
        print("Hola, mi nombre es", self.nombre, self.apellido)

class Admin(Usuario): #La herencia se utiliza cuando se quiere crear una clase, que contenga todos los atributos de otra clase
    def superSaludo(self):
        print("Hola, me llamo ",self.nombre, "y soy administrador")



usuario=Usuario("felipe","feliz") 

usuario.saludo()
usuario.nombre="chanchito" #se pueden cambiar las instancias de una clase 
usuario.saludo() 

admin=Admin("super","feliz")

admin.saludo()
admin.superSaludo()

usuario.superSaludo() #no se pueden acceder a los metodos de las clases que heredan otras
