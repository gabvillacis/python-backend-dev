"""
Definición de la clase Persona
"""

class Persona:
    
    def __init__(self, p_nombre, p_edad, p_sexo):
        self.nombre = p_nombre
        self.edad = p_edad
        self.sexo = p_sexo
    
    
    def trabajar(self):
        print("trabajando")
        
    
    def estudiar(self):
        print("estudiando")
        
    
    def comer(self, menu):
        print(f"{self.nombre} está comiendo {menu}")
        

"""
Crear objetos de la clase Persona
"""
luis = Persona("Luis Sola", 35, "Hombre")
print(luis.nombre)
luis.trabajar()
luis.comer("Encebollado")

mauricio = Persona("Mauricio Suarez", 35, "Hombre")
mauricio.comer("Hamburguesa")
