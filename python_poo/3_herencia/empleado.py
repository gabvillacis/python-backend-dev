"""
Ejemplificando la sobreescritura de métodos con el cálculo de sueldo a empleados.
"""
class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def calcular_salario(self):
        return self.sueldo_base


class Vendedor(Empleado):
    def __init__(self, nombre, sueldo_base, incentivo_x_ventas):
        super().__init__(nombre, sueldo_base)
        self.incentivo_x_ventas = incentivo_x_ventas
    
    def calcular_salario(self):
        return self.sueldo_base + self.incentivo_x_ventas + 1000


john = Vendedor('John', 5000, 1500)
print(john.calcular_salario())

jane = Empleado('Jane', 3000)
print(jane.calcular_salario())