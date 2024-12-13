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
            print("opcion A")
           # listar_ordenado_por_nombre(lista_personajes)
        elif opcion == "B":
            print("opcion B")
          #  listar_masculinos_debiles(lista_personajes)
        elif opcion == "C":
            print("opcion C")
           # cantidad_por_color_ojos(lista_personajes)
        elif opcion == "D":
            print("opcion D")
            #listar_por_color_pelo(lista_personajes)
        elif opcion == "E":
            print("opcion E")
           # listar_por_inteligencia(lista_personajes)
        elif opcion == "F":
            print("opcion F")
           # listar_promedio(lista_personajes)
        elif opcion == "G":
            print("opcion G")
           # asignar_imc(lista_personajes)
        elif opcion == "H":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el menú
menu()
