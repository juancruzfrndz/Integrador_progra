n = int(input("Ingresa un número: "))
contador_primos = 0

for num in range(1, n + 1):
    contador = 0  
    for i in range(1, num + 1):
        if num % i == 0:  
            contador += 1
    
    if contador == 2:  
        print(num)
        contador_primos += 1

print("Se encontraron "+ str(contador_primos) +" números primos.")

