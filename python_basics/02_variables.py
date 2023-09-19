# Ejemplo de variables y tipos de datos en Python

# Entero (int)
edad = 30

# Flotante (float)
altura = 1.75

# Cadena de Caracteres (str)
nombre = "Juan"
apellido = 'Pérez'

# Booleano (bool)
es_mayor_de_edad = True
esMayorEdad = False

# Lista (list)
numeros = [1, 2, 3, 4, 5]

# Tupla (tuple)
coordenadas = (10, 20)

# Diccionario (dict)
persona = {'nombre': 'Ana', 'edad': 25, 'profesion': 'Ingeniero', 12: 450 }

# None (NoneType)
resultado = None

# Imprimir los valores de las variables
print("Edad:", edad)
print("Altura:", altura)
print("Nombre:", nombre)
print("Apellido:", apellido)
print("¿Es mayor de edad?", es_mayor_de_edad)
print("Números:", numeros)
print("Coordenadas:", coordenadas)
print("Información de la persona:", persona)
print("Resultado:", resultado)

print("El tipo de dato de la variable numeros es: ", type(numeros))


#%% Ingreso de datos por teclado
nombre = input("Ingrese su nombre")
print("Nombre: ", nombre)
edad = input("Ingrese su edad")
print(type(edad), edad)
edad = int(edad)
print(type(edad), edad)
