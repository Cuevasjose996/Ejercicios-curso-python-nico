#escribir una aplicacion que reciba una cantidad infinita de numeros
#hasta decir basta, luego que devuelva la suma de los numeros ingresados

lista=[]
print("Ingrese numeros y para salir escriba 'basta'")

while True:
    valor=input("Ingrese un valor: ")
    if valor== "basta":
        break
    else:
        try:
            valor=int(valor)
            lista.append(valor)
        except:
            print("Dato invalido")
            exit()

resultado=0
for x in lista:
    resultado+=x

print(resultado)