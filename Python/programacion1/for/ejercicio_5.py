acum=0
cont=0
for i in range (10):
    num=int(input("ingrese su numero: "))
    if num ==0:
        break
    acum+=num
    cont+=1
print("la suma de los numeros es: " +str(acum))
print("el promedio de los numeros es: "+str(acum/cont))


