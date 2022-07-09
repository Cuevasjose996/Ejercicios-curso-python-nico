diccionario= {
    "nombre":"chanchito feliz",
    "raza":"persa",
    "edad": 5
} #las llaves "{}" define un diccionario

# print(diccionario)
# print(diccionario["nombre"]) #accede al nombre o al dato ingresado en el valor del diccionario

# print(diccionario.get("nombre")) #se puede acceder al nombre mediante el metodo .get

diccionario["nombre"]= "wiskas" #de esta manera se modifican valores de un diccionario
# print(diccionario)

print(len(diccionario)) #imprime la cantidad de datos en un diccionario (clave:valor)

diccionario["peso"]= 2 #agrega datos al diccionario

print(diccionario)

# diccionario.pop("peso") #elimina un dato del diccionario
#diccionario.popitem() #elimina el ultimo dato anadido al diccionario
# del diccionario["peso"] #elimina el dato seleccionado

copiaGatos=diccionario.copy()

print(copiaGatos,diccionario)

diccionario.clear() #elimina todos los datos de un diccionario

