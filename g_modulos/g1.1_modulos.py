import g1_modulos #Al tomar esta clase, me di cuenta que el nombre de los archivos .py tambien es importante no iniciarlo con numero ni caracteres especiales
#si lo inicias con numeros, no vas a poder crear modulos con ellos, y llamarlos en los archivos
print(g1_modulos.mascotas) #Un modulo se puede importar desde otro archivo, para traerte a ese archivo todas las funciones creadas dentro de ese modulo
g1_modulos.saludo("Pepe")