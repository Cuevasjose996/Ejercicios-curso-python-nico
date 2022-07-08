def miFuncion2(argumento="chanchito"): #el parametro "chanchito" sera el parametro predefinido para la funcion
    print(argumento)

# miFuncion2("batman")
# miFuncion2()

def miFuncionLista(lista): #se pueden pasar listas y recorrerlas con funciones
    for el in lista:
        print(el)

miFuncionLista(["chanchito","feliz","triste"])

def concatenaNombres(lista2):
    i=""
    for al in lista2:
        i=i + al + " "
        return i 

nombres=concatenaNombres(["chanchito","feliz"])
print(nombres)