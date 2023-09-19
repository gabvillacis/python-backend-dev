"""
Ejemplificando los tipos de herencia en python mediante el caso de uso de figuras geométricas.
"""
class Rectangulo:
    def __init__(self, largo: float, ancho: float) -> None:
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self) -> float:
        return self.largo * self.ancho

    def calcular_perimetro(self) -> float:
        return 2 * self.largo + 2 * self.ancho


class Cuadrado(Rectangulo):
    def __init__(self, largo) -> None:
        super().__init__(lado, lado)
      

cuadrado = Cuadrado(4)
print(f"El área del cuadrado es: {cuadrado.calcular_area()}")
print(cuadrado.calcular_perimetro())

rectangulo = Rectangulo(5, 10)
print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
rectangulo.calcular_perimetro()