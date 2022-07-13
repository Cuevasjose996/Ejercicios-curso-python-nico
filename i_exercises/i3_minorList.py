# Escribir una funcion que encuentre el menor de una lista

numeros = []


print("Este programa selecciona el valor mas alto de tres numeros.")

numero1 = input("Ingrese primer numero: ")

try:
    int(numero1)
except ValueError:
    try:
        float(numero1)
    except ValueError:
        print("Error! Ingrese un numero.")
        exit()

numero1 = float(numero1)
numeros.append(numero1)

numero2 = input("Ingrese el segundo numero: ")

try:
    int(numero2)
except ValueError:
    try:
        float(numero2)
    except ValueError:
        print("Error! Ingrese un numero.")
        exit()

numero2 = float(numero2)
numeros.append(numero2)

numero3 = input("Ingrese el tercer numero: ")

try:
    int(numero3)
except ValueError:
    try:
        float(numero3)
    except ValueError:
        print("Error! Ingrese un numero.")
        exit()

numero3 = float(numero3)
numeros.append(numero3)

numero4 = input("Ingrese el cuarto numero: ")

try:
    int(numero4)
except ValueError:
    try:
        float(numero4)
    except ValueError:
        print("Error! Ingrese un numero.")
        exit()

numero4= float(numero4)
numeros.append(numero4)

numero5 = input("Ingrese el cuarto numero: ")

try:
    int(numero5)
except ValueError:
    try:
        float(numero5)
    except ValueError:
        print("Error! Ingrese un numero.")
        exit()

numero5= float(numero5)
numeros.append(numero5)

menor = numeros[0]

for numero in numeros:
    if menor > numero:
        menor = numero

print("El mayor es el:", menor)
