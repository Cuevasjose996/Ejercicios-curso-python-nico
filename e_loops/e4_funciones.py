def miFuncion():
    print("mi primera funcion")

# miFuncion()
# miFuncion()
# miFuncion()
# miFuncion()
# miFuncion()
# miFuncion()

def imprimeDato(nombre, apellido): #cuando se definen las funciones, las variables que se declaran en la funcion se les llama argumentos
    print("mi nombre es: ",nombre ,"y mi apellido es: ",apellido)

imprimeDato("jose", "cruz") #cuando se mandan llamar funciones, las variables que se definen en la funcion se les llama parametros


def nombreCompleto(apellido, nombre): 
    print(nombre, apellido)

nombreCompleto(nombre="chanchito", apellido="feliz") # se pueden llamar a los argumentos escribiendo el nombre del argumento, seguido del parametro al llamar a a la funcion

def nombreCompleto2(**kwargs):
    print(kwargs["nombre"],["apellido"])

nombreCompleto2(nombre="chanchito", apellido="feliz")