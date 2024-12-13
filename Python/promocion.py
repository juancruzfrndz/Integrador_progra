def verificar_coordenadas(x: int, y: int):
    tablero = [
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1]
    ]
    contador_explosion = 0
    if tablero[x][y] == 1:
        contador_explosion += 1
        print("se encontro una mina en ese lugar")
    else:
        print("no hay minas en ese lugar ")
    
    return contador_explosion
decision="si"
totales_explosionee=0
while decision=="si":
    x = int(input("ingrese un número de fila: "))
    while x < 0 or x > 4:
        x = int(input("ingrese un numero de fila entre 0 y 4: "))
    y = int(input("ingrese un numero de columna: "))
    while y < 0 or y > 4:
        y = int(input("ingrese un numero de columna entre 0 y 4: "))
    explotadas = verificar_coordenadas(x, y)
    totales_explosionee=totales_explosionee+explotadas
    decision=input("ingrese si desea continuar ingresando coordenadas(si/no): ")
    while decision!="si" and decision!="no":
        decision=input("ingrese si desea continuar ingresando coordenadas(si/no): ")


print("la antidad de minas explotadas fue: ", explotadas)
