import csv
def menu():
    while True:
        print("Opciones del Menú:")
        print("1. Leer archivo")
        print("2. Buscar un producto")
        print("3. Ordenar el inventario")
        print("4. Listar inventario")
        print("5. Actualizar el inventario")
        print("6. Escribir un archivo")
        print("7. Salir")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            print("Opción 1: Leer archivo")
            inventario = leer_archivo()
        elif opcion == "2":
            print("Opción 2: Buscar un producto")
            productos = input("Ingrese el producto que desea buscar: ")
            buscar_producto(inventario, productos)
        elif opcion == "3":
            print("Opción 3: Ordenar el inventario")
            claves = int(input("Ingrese 0 si quiere ordenar por precio o ingrese 1 si quiere ordenar por cantidad: "))
            ordenes = int(input("Ingrese 1 si quiere ordenar de manera ascendente o ingrese 2 si quiere ordenar de manera descendente: "))
            ordenamiento_de_productos(inventario, claves, ordenes) 
        elif opcion == "4":
            print("Opción 4: Listar inventario")
            listar_inventario(inventario)
        elif opcion == "5":
            print("Opción 5: Actualizar el inventario")
            actualizar_inventario(inventario)
        elif opcion == "6":
            print("Opción 6: Escribir un archivo")
            guardar_en_archivo(inventario)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
menu()


def leer_archivo():
    inventario = []
    ruta="inventario.csv"
    with open(ruta, 'r') as archivo:
        for mercaderia in archivo:
            datos = mercaderia.strip().split(",")
            if datos[0] != 'Nombre':  
                datos[1] = float (datos[1])
                datos[2] = int(datos[2])    
                inventario.append(datos)

    return inventario
inventario=leer_archivo()
#print(inventario)

def buscar_producto(inventario, producto):
    cont_produ = 0
    for producto_en_inventario in inventario:
        if producto_en_inventario[0].lower() == producto.lower():
            print(producto, producto_en_inventario)
            cont_produ += 1
    if cont_produ == 0:
        print("Este producto no se encuentra disponible.")

#buscar_producto(inventario)
def ordenamiento_de_productos(inventario, clave, orden):
    for i in range(len(inventario) - 1):
        for j in range(i + 1, len(inventario)):
            if orden == 1 and inventario[i][clave] > inventario[j][clave]:
                inventario[i], inventario[j] = inventario[j], inventario[i]
            elif orden == 2 and inventario[i][clave] < inventario[j][clave]:
                inventario[i], inventario[j] = inventario[j], inventario[i]

def listar_inventario(inventarios):
    for p in inventarios:
        print("Producto: {:30} Precio: ${} cantidad: {}".format(p[0], p[1], p[2]))
#Listar_inventario(inventario)

def actualizar_inventario(inventarios):
    venta=input("ingrese el producto que desea comprar: ")
    cantidad=int(input("ingrese la cantidad de producto que desea comprar: "))
    for producto_en_inventario in inventarios:
        if producto_en_inventario[0].lower() == venta.lower():
            if producto_en_inventario[2]>=cantidad:
                print("El total por esa cantidad de producto es", producto_en_inventario[1]*producto_en_inventario[2])
                producto_en_inventario[2]-=cantidad
            else:
                print("la cantidad de producto solicitada no esta disponible")
    print(inventarios)
        
#actualizar_inventario(inventario)

def guardar_en_archivo(inventarios):
    with open("Ventas.csv", "w") as archivo:
        for item in inventarios:
            linea = f"{item[0]} {item[1]} {item[2]}\n"
            archivo.write(linea)

#guardar_en_archivo(inventario)

menu()



    


