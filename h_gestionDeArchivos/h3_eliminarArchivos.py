import os #se debe importar el modulo "os"

if os.path.exists("x.txt"):
    os.remove("x.txt") #os.remove elimina el archivo seleccionado
else:
    print("el archivo no existe")

os.rmdir() #esta indicacion eliminar las carpetas