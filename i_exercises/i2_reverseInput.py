#Ingresa nombre y apellido e imprimirlo al reves

nombre=input("Ingresa tu nombre: ")
apellido=input("Ingresa tu apellido: ")

lnombre=len(nombre)
cortenombre=nombre[lnombre::-1]
lapellido=len(apellido)
corteapellido=apellido[lapellido::-1]

print(cortenombre,"",corteapellido)

#metodo dos

concatenar=nombre+' '+apellido
print(concatenar[::-1])

