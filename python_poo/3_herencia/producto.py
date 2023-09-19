class Producto:
    def __init__(self, nombre: str, precio: float) -> None:
        self.__nombre = nombre
        self.__precio = precio
        
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre) -> None:
        self.__nombre = nuevo_nombre
        
    @property
    def precio(self) -> float:
        return self.__precio
    
    @precio.setter
    def precio(self, nuevo_precio) -> None:
        self.__precio = nuevo_precio

    def agregar_al_carrito(self) -> None:
        print(f'Se añadió el producto: {self.__nombre} al carrito')
        
    def quitar_del_carrito(self) -> None:
        print(f'Se eliminó el producto: {self.__nombre} del carrito')
    
    def __str__(self) -> str:
        return f'Producto: (Nombre: {self.__nombre}, Precio: {self.__precio})'


class Mp3(Producto):
    def __init__(self, nombre: str, precio: float, artista: str, duracion: int) -> None:
        super().__init__(nombre, precio)
        self.__artista = artista
        self.__duracion = duracion
        
    @property
    def artista(self) -> str:
        return self.__artista
    
    @artista.setter
    def artista(self, nuevo_artista) -> None:
        self.__artista = nuevo_artista
        
    @property
    def duracion(self) -> int:
        return self.__duracion
    
    @duracion.setter
    def duracion(self, nueva_duracion) -> None:
        self.__duracion = nueva_duracion
    
    def reproducir(self) -> None:
        print(f'Reproduciendo mp3 {self.nombre}')
        
    def detener(self) -> None:
        print(f'mp3 {self.nombre} detenido')
        
    def descargar(self) -> None:
        print('Descargando mp3')

mp3_imagine = Mp3("Imagine", 2, "Jhon Lenon", 5)
print(mp3_imagine)

mp3_imagine.agregar_al_carrito()
mp3_imagine.reproducir()
mp3_imagine.detener()