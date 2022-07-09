# class Usuario: #las clases EN TODOS LOS LENGUAJES inician con una letra mayuscula, esto es una convension entre programadores
#     nombre="Felipe" #los metodos, son las caracteristicas que va a tener una clase por asi decirlo
#     apellido= "Feliz"

# usuario=Usuario() #asi se crea un objeto perteneciente a una clase, usuario es un objeto de la clase Usuario()
# usuario2=Usuario()

# print(usuario.nombre, usuario.apellido, usuario.nombre, usuario2.apellido) #se puede imprimir los metodo de una clase de esta manera

class Usuario: #el metodo __init__ nos dice que self, va a ser lo primero que se va a realizar antes que todo en la funcion
    def __init__(self, nombre, apellido): #el self, indica que la clase va a tener propiedades, pero los valores de estas propiedades van a ser definidos una vez llamado creado el objeto
        self.nombre=nombre #el self en la propiedad, indica que se va a pedir un valor para dicha propiedad, cada vez que se cree un objeto
        self.apellido=apellido

usuario=Usuario("felipe","feliz") #asi se crea un objeto perteneciente a una clase, usuario es un objeto de la clase Usuario()
usuario2=Usuario("chanchito","feliz")

print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido) #se puede imprimir las propiedades de una clase de esta manera

