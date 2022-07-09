

class Animal:
    def __init__(self,nombre,onomatopeya):
        self.nombre=nombre
        self.onomatopeya=onomatopeya
    def saludo(self):
        print("Hola soy un", self.tipo, "y mi sonido es el", self.onomatopeya)

class Gato(Animal):
    tipo= "gato"

class Perro(Animal):
    tipo="perro"

gato=Gato("fluffy", "Miau")
gato.saludo()

perro=Perro("guera", "Guau")
perro.saludo()