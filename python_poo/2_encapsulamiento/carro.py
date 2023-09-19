"""
Implemente una clase llamada Carro que tenga dos atributos privados encapsulados: la cantidad de gasolina en el tanque (de 0 a 60 litros) y la lectura del odómetro (kilometraje recorrido). El carro consume un litro de gasolina por kilómetro.

La clase también debe contener los siguientes métodos:

cargar_gasolina() que llena el tanque.
conducir(km: int) que conduce el automóvil por la distancia indicada, o por el tiempo que la gasolina en el tanque lo permita.
__str__() que devuelve una representación de cadena del carro según los ejemplos a continuación:

Carro: kilometraje recorrido: 0 km, gasolina restante: 0 litros.
Carro: kilometraje recorrido: 0 km, gasolina restante: 60 litros.
Carro: kilometraje recorrido: 20 km, gasolina restante: 40 litros.
"""

class Carro:    
    def __init__(self) -> None:
        self.__gasolina_disp = 0
        self.__kilometraje = 0
    
    def cargar_gasolina(self) -> None:
        self.__gasolina_disp = 60        
    
    def conducir(self, kms: int) -> None:
        litros_gas = kms * 1
        if self.__gasolina_disp >= litros_gas:            
            self.__gasolina_disp -= litros_gas
            self.__kilometraje += kms            
        else:
            kms_disponibles = self.__gasolina_disp * 1
            self.__gasolina_disp = 0
            self.__kilometraje += kms_disponibles
    
    def __str__(self) -> str:
        return f'Kilometraje recorrido: {self.__kilometraje}, gasolina disponible: {self.__gasolina_disp}'


jeep = Carro()
print(jeep)
jeep.cargar_gasolina()
print(jeep)
jeep.conducir(20)
print(jeep)
jeep.conducir(50)
print(jeep)