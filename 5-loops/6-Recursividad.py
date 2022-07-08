from re import I


def recursion(i):
    if (i < 1):
        return i 
    print(i)
    recursion(i-1)

recursion(6)

#se puede usar la recursividad cuando se quiere trabajar sobre una coleccion de datos o se quieren hacer intentos para llamar a un servidor o una base de datos
