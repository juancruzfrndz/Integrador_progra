"""""""""""
Ejercicio 2:
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años), adolescente (entre 13 y 17 años) o niño (menor a 13 años).
"""""""""""
edad=int(input("ingrese su edad: "))
if edad>17:
    print("Mayor de edad")
elif edad>12:
    print("es adolescente")
else:
    print("es un niño")