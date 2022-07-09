c=open("chanchito.txt","r") #"open" permite abrir archivos en una programa de python, seguido de esto,
#se le puede agregar un segundo 
#valor para indicar los permisos que le queremos dar a la instruccion
#r="read", a="append", w="write", x="create"
for x in c:
    print(x)

c.close #close cierra los archivos abiertos



