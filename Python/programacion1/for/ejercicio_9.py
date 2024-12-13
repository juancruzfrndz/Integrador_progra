contador=0
num=int(input("ingrese un numero: "))
for i in range (1, num):
    if num%i==0:
        print(i)
        contador+=1
print("la cantidad de numeros divisores es: "+str(contador))