"""""""""
Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su sueldo para esa persona.
"""""""""
nombre=input("ingrese su nombre: ")
sueldo=int(input("ingrese su sueldo: "))
cuenta_sueldo=sueldo+(sueldo*10)/100
print("su nombre es "+nombre+ " y su sueldo incrementado es "+ str(cuenta_sueldo))