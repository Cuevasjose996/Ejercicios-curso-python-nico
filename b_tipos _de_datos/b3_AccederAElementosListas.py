lista=["hola",",mundo","chanchito feliz"] #Los caracteres "[]" definen tipo de dato lista
lista2=[]
print(type(lista))

print(lista)

#Los siguientes son algunos metodos para los tipos de datos (lista)

lista2=lista.copy() #copia la lista en el estado actual
lista.append(55) #El metodo append agrega elementos a listas, al final

# print(lista,lista2)
# print(lista,lista2.count(1)) #El metodo count indica la cantidad de veces que se repide un valor en una lista

# #lista.clear() #Vacia o elimina todos los datos de una lista
# #print(lista)

# print(len(lista),len(lista2)) #len indica la cantidad de datos que contiene una lista

largoLista=len(lista)
largoLista2=len(lista2)

# print(largoLista,largoLista2)

print(lista[0]) #las "[]" indicaran la posicion del elemento que queremos imprimir o seleccionar

