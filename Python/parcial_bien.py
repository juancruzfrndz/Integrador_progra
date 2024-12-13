def contar_caracteres(caracter_esperado):
    lista = ["a", "b", "c", "a", "e", "h", "a","a","b","c","f"]
    contador = 0
    for i in lista:
        if i == caracter:
            contador += 1
    return contador

caracter = input("Ingrese una letra de la 'a' a la 'h': ")
while caracter < "a" or caracter > "h":
    caracter = input("caracter no valido, Ingrese una letra de la 'a' a la 'h': ")

veces= contar_caracteres(caracter)
print("El caracter", caracter, "se repite", veces, "veces en la lista")