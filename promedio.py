## promedio
sum=0
i=0
a=0
print("este programa calculará la suma y promedio de los numeros ingresados. Recuerde que solo puede ingresar 10 numeros")
num=int(input("por favor ingrese ingrese un numero" ))
for b in range (1,11):
	sum=sum+num
	i=i+1
	num=int(input("por favor ingrese ingrese un numero"))
t_sum=sum
prom=sum/i
print("la suma de los numeros ingresados es de: ", t_sum)
print("el prommedio de los numeros ingresados es de:", prom)
