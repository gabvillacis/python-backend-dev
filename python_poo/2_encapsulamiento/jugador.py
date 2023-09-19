"""
Definición de la clase Jugador e implementar métodos getter/setter vía @property
"""
class Jugador:
    
    def __init__(self, nombre: str, nro_camiseta: int) -> None:
        self.__nombre = nombre
        self.__nro_camiseta = nro_camiseta

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        if nombre != "":
            self.__nombre = nombre
        else:
            raise ValueError("El nombre no debe estar vacío")

    @property
    def nro_camiseta(self) -> int:
        return self.__nro_camiseta
    
    @nro_camiseta.setter
    def nro_camiseta(self, nro_camiseta: int) -> None:
        if nro_camiseta > 0:
            self.__nro_camiseta = nro_camiseta
        else:
            raise ValueError("El número de camiseta debe ser positivo")    

jugador = Jugador("Moises Caicedo", 23)
print(jugador.nombre)
print(jugador.nro_camiseta)

jugador.nombre = "Jhegson Mendez"
jugador.nro_camiseta = 20
print(jugador.nombre)
print(jugador.nro_camiseta)