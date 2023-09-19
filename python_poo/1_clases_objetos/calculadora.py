class Calculadora:
    
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2    
        
    def sumar(self):
        suma = self.numero1 + self.numero2
        print(f"La suma es: {suma}")
    
    def restar(self):
        resta = self.numero1 - self.numero2
        print(f"La resta es: {resta}")

    def multiplicar(self):
        mult = self.numero1 * self.numero2
        print(f"El resultado de la multiplicación es: {mult}")
        
    def dividir(self):
        div = self.numero1 / self.numero2
        print(f"El resultado de la división es: {div}")



"""
Utilizaremos la clase Calculadora para realizar los cálculos de 2 números que se ingresan por teclado
"""

n1 = int(input("Ingrese el número 1:"))
n2 = int(input("Ingrese el número 2:"))

calc = Calculadora(n1, n2)

calc.sumar()
calc.restar()
calc.multiplicar()
calc.dividir()