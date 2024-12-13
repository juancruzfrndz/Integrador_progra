# Importar la lista de superhéroes
from data_stark import lista_personajes

# Función para listar ordenado por nombre
def listar_ordenado_por_nombre(lista):
    lista_ordenada = sorted(lista, key=lambda x: x["nombre"])
    for heroe in lista_ordenada:
        print(heroe)

# Función para listar el héroe masculino más débil
def listar_masculinos_debiles(lista):
    masculinos = [heroe for heroe in lista if heroe["genero"] == "M"]
    mas_debil = min(masculinos, key=lambda x: int(x["fuerza"]))
    print(mas_debil)

# Función para contar superhéroes por color de ojos
def cantidad_por_color_ojos(lista):
    colores = {}
    for heroe in lista:
        color = heroe["color_ojos"]
        colores[color] = colores.get(color, 0) + 1
    print(colores)

# Función para listar por color de pelo
def listar_por_color_pelo(lista):
    colores = {}
    for heroe in lista:
        color = heroe["color_pelo"]
        colores.setdefault(color, []).append(heroe)
    for color, heroes in colores.items():
        print(f"Color: {color}")
        for heroe in heroes:
            print(heroe)

# Función para listar por tipo de inteligencia
def listar_por_inteligencia(lista):
    tipos = {}
    for heroe in lista:
        tipo = heroe["inteligencia"]
        tipos.setdefault(tipo, []).append(heroe)
    for tipo, heroes in tipos.items():
        print(f"Inteligencia: {tipo}")
        for heroe in heroes:
            print(heroe)

# Función para listar héroes que superan la fuerza promedio femenina
def listar_promedio(lista):
    femeninas = [heroe for heroe in lista if heroe["genero"] == "F"]
    fuerza_promedio = sum(int(heroe["fuerza"]) for heroe in femeninas) / len(femeninas)
    for heroe in lista:
        if int(heroe["fuerza"]) > fuerza_promedio:
            print(heroe["nombre"], heroe["peso"])

# Función para asignar IMC
def asignar_imc(lista):
    for heroe in lista:
        peso = float(heroe["peso"])
        altura = float(heroe["altura"]) / 100  # Convertir a metros
        heroe["IMC"] = round(peso / (altura ** 2), 2)
    for heroe in lista:
        print(heroe["nombre"], "IMC:", heroe["IMC"])

# Menú principal
def menu():
    while True:
        print("Opciones del Menú:")
        print("A. Listar ordenado por Nombre")
        print("B. Listar Masculinos débiles")
        print("C. Cantidad por color de ojos")
        print("D. Listar por color de Pelo")
        print("E. Listar inteligencia")
        print("F. Listar Promedio")
        print("G. Asignar IMC")
        print("H. Salir")

        opcion = input("Elige una opción: ").upper()
        if opcion == "A":
            listar_ordenado_por_nombre(lista_personajes)
        elif opcion == "B":
            listar_masculinos_debiles(lista_personajes)
        elif opcion == "C":
            cantidad_por_color_ojos(lista_personajes)
        elif opcion == "D":
            listar_por_color_pelo(lista_personajes)
        elif opcion == "E":
            listar_por_inteligencia(lista_personajes)
        elif opcion == "F":
            listar_promedio(lista_personajes)
        elif opcion == "G":
            asignar_imc(lista_personajes)
        elif opcion == "H":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el menú
menu()
