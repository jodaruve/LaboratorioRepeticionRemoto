## promedio
sum=0
i=0
a=0
print("este programa calculará la suma y promedio de los numeros ingresados. Recuerde que cuando no desee igresar mas numeros debe escribir -1")
num=int(input("por favor ingrese ingrese un numero"))
while num!=-1:
	sum=sum+num
	i=i+1
	num=int(input("por favor ingrese ingrese un numero"))
t_sum=sum
prom=sum/i
print("la suma de los numeros ingresados es de: ", t_sum)
print("el prommedio de los numeros ingresados es de:", prom)