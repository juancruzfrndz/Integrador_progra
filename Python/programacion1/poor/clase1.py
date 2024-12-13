"""""""""
class persona:
    def __init__(self) -> None:
        self.nombre="JuanCruz"
        self.pais="Argentina"
        self.numero=1135601232
    def mostrarpersona(self, nombre, pais, ):
        print("nombre: "+ self.nombre)
        print("pais: "+ self.pais )
persona_uno=persona()   
persona_uno.mostrarpersona("Juan Cruz", "Argentina")

"""""""""

"""""""""
class persona:
    def __init__(self, nombre, pais, numero) -> None:
        self.nombre= nombre
        self.pais=pais
        self.numero=numero  
    def mostrarpersona(self):
        print("nombre: "+ self.nombre)
        print("pais: "+ self.pais )

persona_uno=persona("Juan Cruz", "Pais", 113456789)
persona_2=persona("Paulo", "Peru", 1109865542)
persona_2.mostrarpersona()
"""""""""

cadena="hola mundo"
cadena2="142435l"
array=["h" "o" "l" "a"]
print(cadena)
print(cadena.upper())
print(cadena.lower())
print(cadena.capitalize())
print(cadena.title())
print(cadena.replace(" ", "ldm"))
print(cadena.split("a"))
print("".join(array))
print(cadena.zfill(20))
print(cadena.find("o",2,len(cadena)))
print(cadena.count("o"))
print(cadena.isalpha())
print(cadena2.isalnum())