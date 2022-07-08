#los for loops se usan por lo general para iterar(recorrer)listas, tuplas o diccionarios

usuarios= ["chanchito feliz","Felipe","Roberto", "Nicolas"]

for usuario in usuarios: # se puede acceder a cada uno de los elementos de una lista haciendo uso de un for loop
    print(usuario)

nombre="chanchito feliz" #se puede recorrer tambien cada uno de los caracteres de un string

for c in nombre:
    print(c)

usuarios2= ["chanchito triste","Raul","Rigoberto", "Nico"]

for usuarie in usuarios2: # se pueden usar breaks para cortar iteraciones
    if usuarie=="Rigoberto":
        break
    print(usuarie)

usuarios3= ["chanchito triste","Raul","Rigoberto", "Nico"]

for usuaria in usuarios3: # se pueden usar continue para saltar un dato de el rango
    if usuaria=="Rigoberto":
        continue
    print(usuaria)