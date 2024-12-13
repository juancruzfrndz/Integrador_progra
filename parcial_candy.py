import random

def rellenar_lista(columnas: int):
    lista = [
        {"piezas": []},
        {"piezas": []},
        {"piezas": []},
        {"piezas": []}
    ]
    for diccionario in lista:
        diccionario["piezas"] = [random.randint(1, 3) for _ in range(columnas)]
    return lista

def recorrer_lista(lista: list, fila: int, columna: int):
    numero_elegido = lista[fila]["piezas"][columna]
    cont_puntos = 0

   
    if fila > 0 and fila < len(lista) - 1:  
        if numero_elegido == lista[fila + 1]["piezas"][columna] and numero_elegido == lista[fila - 1]["piezas"][columna]:
            cont_puntos += 10
    if fila > 1:  
        if numero_elegido == lista[fila - 1]["piezas"][columna] and numero_elegido == lista[fila - 2]["piezas"][columna]:
            cont_puntos += 10
    if fila < len(lista) - 2:  
        if numero_elegido == lista[fila + 1]["piezas"][columna] and numero_elegido == lista[fila + 2]["piezas"][columna]:
            cont_puntos += 10

    
    if columna > 0 and columna < len(lista[fila]["piezas"]) - 1: 
        if numero_elegido == lista[fila]["piezas"][columna + 1] and numero_elegido == lista[fila]["piezas"][columna - 1]:
            cont_puntos += 10
    if columna > 1:
        if numero_elegido == lista[fila]["piezas"][columna - 1] and numero_elegido == lista[fila]["piezas"][columna - 2]:
            cont_puntos += 10
    if columna < len(lista[fila]["piezas"]) - 2:  
        if numero_elegido == lista[fila]["piezas"][columna + 1] and numero_elegido == lista[fila]["piezas"][columna + 2]:
            cont_puntos += 10

    return cont_puntos


    
columnas = int(input("Ingrese las columas que va querer: "))
lista = rellenar_lista(columnas)

fila = int(input(f"Ingrese una fila valida que va querer buscar: "))
while fila<0 or fila>(len(lista)):
    fila=int(input("ingrese una fila valida: "))
columna = int(input("Ingrese una columna valida que va querer buscar:  "))
while columna<0 or columna>columnas:
    columna=int(input("ingrese una columna valida: "))

puntos = recorrer_lista(lista, fila, columna)
print("Puntos obtenidos: ", puntos)