"""
Ejemplificando la sobreescritura de métodos con el cálculo de sueldo a empleados.
"""
# Clase Empleado
class Empleado:
    def __init__(self, nombre: str, sueldo_base: float) -> None:
        self.__nombre = nombre
        self.__sueldo_base = sueldo_base

    @property
    def nombre(self) -> str:
        return self.__nombre
  
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self.__nombre = nuevo_nombre
        
    @property
    def sueldo_base(self) -> float:
        return self.__sueldo_base
  
    @sueldo_base.setter
    def sueldo_base(self, nuevo_sueldo_base: float) -> None:
        self.__sueldo_base = nuevo_sueldo_base

    def calcular_salario(self) -> float:
        return self.__sueldo_base
    
# Clase Empleado (hereda de Empleado)
class Vendedor(Empleado):
    def __init__(self, nombre: str, sueldo_base: float, comision_x_ventas: float):
        super().__init__(nombre, sueldo_base)
        self.__comision_x_ventas = comision_x_ventas
    
    def calcular_salario(self, monto_ventas: float) -> float:
        return self.sueldo_base + (monto_ventas * self.__comision_x_ventas/100)

jane = Empleado('Jane', 3000)
print(jane.calcular_salario())

john = Vendedor('John', 5000, 10)
print(john.calcular_salario(50000))

