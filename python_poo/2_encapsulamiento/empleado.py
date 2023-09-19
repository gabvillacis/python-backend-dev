class Empleado:
    def __init__(self) -> None:
        self.__sueldo = 425
    
    # Método getter para atributo sueldo
    @property
    def sueldo(self) -> float:
        return self.__sueldo

    # Método setter para atributo sueldo
    @sueldo.setter
    def sueldo(self, nuevo_sueldo: float) -> None:
        if nuevo_sueldo > 0:            
            if nuevo_sueldo > self.__sueldo:                
                self.__sueldo = nuevo_sueldo
            else:
                raise ValueError("El valor del nuevo sueldo debe ser mayor que el actual")
        else:
            raise ValueError("El valor del sueldo debe ser mayor que 0")
        
            

emp = Empleado()
print(emp.sueldo)
emp.sueldo = 1500
print(emp.sueldo)
emp.sueldo = 1000
print(emp.sueldo)
emp.sueldo = -300
print(emp.sueldo)