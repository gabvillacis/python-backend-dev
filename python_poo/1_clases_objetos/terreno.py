"""
Realizar un programa que permita calcular el precio de venta de terrenos.
Considere que los terrenos que están a la venta tienen forma rectangular.
"""
class Terreno:
    def __init__(self, ancho, largo, precio_unidad=1):
        self.ancho = ancho
        self.largo = largo
        self.precio_unidad = precio_unidad
    
    def obtener_area(self):
        return self.ancho * self.largo
    
    def calcular_precio(self):
        area = self.obtener_area()
        return area * self.precio_unidad

"""
Se utiliza la clase Terreno para calcular el precio de varios terrenos de distintos tamaños.
"""        
terreno_1 = Terreno(200, 150, 50)
precio_t1 = terreno_1.calcular_precio()
print(f"El terreno con área de: {terreno_1.obtener_area()} vale: {precio_t1}")

terreno_2 = Terreno(50, 50, 45)
precio_t2 = terreno_2.calcular_precio()
print(f"El terreno con área de: {terreno_2.obtener_area()} vale: {precio_t2}")