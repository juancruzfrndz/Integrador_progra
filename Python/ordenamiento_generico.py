lista = [
    {"nombre": "ana", "edad": 23, "nota": 10},
    {"nombre": "pablo", "edad": 13, "nota": 8},
    {"nombre": "juan", "edad": 29, "nota": 1},
    {"nombre": "julia", "edad": 32, "nota": 6}
]

def ordenamiento_generico(lista: list, clave: str, orden: int):
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if orden == 1:
                if lista[i][clave] > lista[j][clave]:
                    intercambiar(lista, i, j)
            elif orden == -1:
                if lista[i][clave] < lista[j][clave]:
                    intercambiar(lista, i, j)

def intercambiar(lista: list, posicion1: int, posicion2: int):
    aux = lista[posicion1]
    lista[posicion1] = lista[posicion2]
    lista[posicion2] = aux

print("Sin ordenar:")
print("nombre  edad  nota")
for item in lista:
    print(item["nombre"], "   ", item["edad"], "   ", item["nota"])

ordenamiento_generico(lista, "edad", -1)

print("Ordenado ")
print("nombre  edad  nota")
for item in lista:
    print(item["nombre"], "   ", item["edad"], "   ", item["nota"])
