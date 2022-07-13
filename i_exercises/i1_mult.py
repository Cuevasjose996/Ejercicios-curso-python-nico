#multiplicar dos numeros sin usar el simbolo de multiplicacion

a=int(input("Ingresa un numero: "))
b=int(input("Ingresa un segundo numero: "))
resultado=0

if a==0 or b==0:
    print(0)
elif b==1:
    print(a)
elif a==1:
    print(b)
else:
    for x in range(a):
        resultado+=b
    print(resultado)