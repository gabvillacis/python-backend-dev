# Ejercicios de Manipulación de Cadenas

#%% Ejercicio 1: Longitud de una Cadena
cadena = "Hola, mundo"
longitud = len(cadena)
print("La longitud de la cadena es:", longitud)

#%% Ejercicio 2: Concatenación de Cadenas
nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido
print("Nombre completo:", nombre_completo)

#%% Ejercicio 3: Mayúsculas y Minúsculas
frase = "Python es divertido"
mayusculas = frase.upper()
minusculas = frase.lower()
print("Mayúsculas:", mayusculas)
print("Minúsculas:", minusculas)

#%% Ejercicio 4: Reemplazar Caracteres
mensaje = "Hola, mundo"
mensaje_modificado = mensaje.replace("mundo", "Python")
print("Mensaje modificado:", mensaje_modificado)

#%% Ejercicio 5: Dividir una Cadena
frase = "Python es un lenguaje de programación"
palabras = frase.split(" ")
print("Palabras:", palabras)

#%% Ejercicio 6: Solicitar una Cadena al Usuario
cadena = input("Ingrese una frase: ")
print(cadena)

#%% Ejercicio 7: Conteo de Palabras
oracion = input("Ingresa una oración: ")
palabras = oracion.split()
cantidad_palabras = len(palabras)
print("Cantidad de palabras:", cantidad_palabras)

#%% "F-String"
animal = "perro"
nombre = "Ashley"
edad = 3
valor = 3500.459
comida = "croquetas", "pollo"
print(f"Mi {animal} se llama {nombre} y tiene {edad} años y cuesta {valor:.5f} y come {comida[0]} y {comida[1]} ")