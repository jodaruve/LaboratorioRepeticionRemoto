## pares
t_pares=0
a=int(input("por favor ingrese un  numero para saber si es par o impar "))
while a%2==0:
    print("el numero es par")
    a=int(input("por favor ingrese un  numero para saber si es par o impar "))
    t_pares=t_pares+1

print("el total de pares fue de:", t_pares)