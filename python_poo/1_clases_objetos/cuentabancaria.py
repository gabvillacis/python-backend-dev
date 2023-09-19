"""
Crear una clase en Python que se llame “CuentaBancaria” la cual represente una cuenta de ahorros en un banco.
La clase debe tener los atributos: número de cuenta, titular y saldo.

Crear un constructor con los parámetros número de cuenta, titular y saldo e inicializar los atributos.

Crear un método depositar que maneje la acción de depositar dinero en la cuenta.

Crear un método retirar que maneje la acción de retirar dinero de la cuenta, considerando que cada vez que se hace un retiro el banco cobra una comisión del 5% del valor retirado y lo descuenta del saldo. (No se puede retirar si el saldo es insuficiente, mostrar los mensajes de error correspondientes).

Crear un método display que permita mostrar los detalles de la cuenta.
"""
class CuentaBancaria:
    
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor_dep):
        if valor_dep > 0:
            self.saldo = self.saldo + valor_dep
            print(f'Valor Depositado: {valor_dep}. El saldo actual es: {self.saldo}')
        else:
            print(f'Valor a Depositar es inválido')
            
    def retirar(self, valor_retiro):
        if valor_retiro > 0:        
            valor_comision = valor_retiro * 0.05;
            if self.saldo > valor_retiro + valor_comision:
                self.saldo = self.saldo - (valor_retiro + valor_comision)
                print(f'Valor Retirado: {valor_retiro}. El saldo actual es: {self.saldo}')
            else:
                print('Saldo insuficiente')
        else:
            print(f'Valor a Retirar es inválido')
    
    def display(self):
        print(f'El número de cuenta es: {self.numero}')
        print(f'El titular es: {self.titular}')
        print(f'El saldo actual es: {self.saldo}', end='\n\n')
        

"""
Utilizar la clase CuentaBancaria para instanciar objetos y transaccionar.
"""
cuenta1 = CuentaBancaria("CUENTA001", "Gabriel Villacis", 20)
cuenta1.display()
cuenta1.depositar(50)
cuenta1.retirar(20)
cuenta1.retirar(100)
cuenta1.display()
