"""""""""""""""""""""
Desarrollar una función que reemplaza una palabra específica por otra
en una cadena.
"""""""""""""""""""""
def remplaza_palabra(cadena:str, reemplazo:str, reemplazada:str):
    print(cadena)
    print(reemplazo)
    print(reemplazada)
    print(cadena.replace(reemplazada,reemplazo))

cadena_real=str(input("ingrese una cadena: "))
palabra_reemplazada=str(input("ingrese la palabra que quiere reemplazar: "))
palabra_reemplazo=str(input("ingrese la palabra para reemplazar: "))
remplaza_palabra(cadena_real, palabra_reemplazo, palabra_reemplazada)