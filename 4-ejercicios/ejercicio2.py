primero= input("ingrese primer numero: ")
try:
    primero=int(primero)
except:
    primero= "chanchito feliz"

if primero=="chanchito feliz":
    print("el valor ingresado no es entero")
    exit()

segundo= input("ingrese segundo numero: ")

try:
    segundo=int(segundo)
except:
    segundo= "chanchito feliz"

if segundo=="chanchito feliz":
    print("el valor ingresado no es entero")
    exit()

simbolo= input("ingrese operacion: ")

if simbolo== "+":
    print(primero+segundo)
elif simbolo=="-":
    print(primero-segundo)
elif simbolo=="*":
    print(primero*segundo)
elif simbolo=="/":
    print(primero/segundo)
else:
    print("el simbolo ingresado no es valido")