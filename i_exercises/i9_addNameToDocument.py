#escribir una funcion que reciba nombre y apellido y los vaya agregando a un archivo

def agregarNombreArchivo(nombre,apellido):
    c=open("nombrecompleto.txt","a")
    c.write(nombre+" "+apellido+"\n")
    c.close()

agregarNombreArchivo("Jose", "Cuevas")