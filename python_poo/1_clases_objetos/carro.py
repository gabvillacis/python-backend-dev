"""
Definición de la clase Carro
"""
class Carro:
    def __init__(self, marca, modelo, color, velocidad_max):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad_max = velocidad_max        
    
    def encender(self):
        print("Encendido")
    
    def acelerar(self):
        print("Acelerando...")
    
    def cambiar_velocidad(self):        
        print("Velocidad cambiada")
    
    def frenar(self):
        print("Frenando...")
        
    def apagar(self):
        print("Apagado")


"""
Creación de objetos de la clase Carro:
"""

audi_a6 = Carro("Audi", "A6", "Negro", 220)
audi_a6.encender()
audi_a6.acelerar()
audi_a6.frenar()
audi_a6.apagar()

toyota_corolla = Carro("Toyota", "Corolla", "Blanco", 180)
toyota_corolla.encender()
toyota_corolla.apagar()