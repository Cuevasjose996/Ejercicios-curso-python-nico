tupla=("hola","mundo","somos","tuplas") #las tuplas se definen con "()"

#metodos de tuplas

print(tupla.count("hola")) #cuenta las veces que se repite un elemento
print(tupla.index("hola")) #indica la posicion de un elemento

#como convertir tupla a lista

listaDeTupla= list(tupla) #list convierte un tipo de elemento a lista

listaDeTupla.append("chanchin")
print(listaDeTupla)