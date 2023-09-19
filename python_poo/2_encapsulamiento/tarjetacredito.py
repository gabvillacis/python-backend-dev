"""
Definición de la clase TarjetaCredito
"""
class TarjetaCredito:
    
    # Los atributos numero y saldo son privados, mientras que el atributo nombre es público
    def __init__(self, numero: str, nombre: str) -> None:
        self.__numero = numero
        self.nombre = nombre
        self.__saldo = 0
    
    def comprar(self, valor_compra: float) -> None:
        if valor_compra <= self.__saldo:
            self.__saldo -= valor_compra
        else:
            print("Saldo insuficiente")
    
    def depositar_pago(self, valor_pago: float) -> None:
        if valor_pago > 0:
            self.__saldo += valor_pago
    
    def consultar_saldo(self) -> float:
        return self.__saldo

    def __str__(self) -> str:
        return f'Tarjeta #: {self.__numero}, Titular: {self.nombre}, Saldo: {self.consultar_saldo()}'
    
"""
Creando objetos de la clase TarjetaCredito y manipular sus atributos/métodos:
"""

"""
tarjeta1 = TarjetaCredito("123456789", "Armando Valencia")
print(tarjeta1.nombre)
tarjeta1.nombre = "Armando Valencia Torres"
print(tarjeta1.nombre)
print(tarjeta1.consultar_saldo())
"""

tarjeta2 = TarjetaCredito("987654321", "Marcos Tenorio")
tarjeta2.depositar_pago(500)
print(tarjeta2)
tarjeta2.comprar(50)
print(tarjeta2)
tarjeta2.comprar(1000)