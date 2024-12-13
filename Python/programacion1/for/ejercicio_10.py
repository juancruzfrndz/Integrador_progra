num=int(input("ingrese el numero: "))
contador=0
for i in range (1, num+1):
    if num%i==0:
        contador+=1
if contador!=2:
    print("el numero ingresado no es un numero primo")
else:
    print("el numero ingresado es un numero primo")
