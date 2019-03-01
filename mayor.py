## mayor de dos
t_positivos=0
t_ceros=0
t_negativos=0
i=0
for i in range (1,11): 
    a=int(input("ingrese un numero "))
    if a==0:
        print("el numero es cero")
        t_ceros=t_ceros + 1
    elif a>0:
        print("el numero es positivo")
        t_positivos=t_positivos+1
    else:
        print("el numero es negativo")
        t_negativos=t_negativos+1
print("el total de numeros positives es de:", t_positivos)
print("el total de numeros negativos es de:", t_negativos)
print("el total de ceros es de:", t_ceros)