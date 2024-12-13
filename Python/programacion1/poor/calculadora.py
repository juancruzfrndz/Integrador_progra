class calculadora: 


    def __init__(self, numero1:int, numero2:int):
        self.num1=numero1
        self.num2=numero2


    def suma(self):
        suma=self.num1+self.num2
        print(suma)


    def multi(self):
        multi=self.num1*self.num2
        print(multi)


    def resta(self):
        resta=self.num1-self.num2
        print(resta)


    def division(self):
        division=self.num1/self.num2
        print(division)


num_ing1=int(input("ingrese su primer numero: "))
num_ing2=int(input("ingrese su segundo numero: "))

numeros=calculadora(num_ing1, num_ing2)
numeros.suma()
numeros.resta()
numeros.division()
numeros.multi()

        