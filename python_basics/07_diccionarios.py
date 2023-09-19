#%% Ejercicio 1: Iteración de un diccionario
persona = {'nombre': 'Gabriel', 'edad': 36, 'ciudad': 'Gye'}
for clave, valor in persona.items():
    print(f'Clave: {clave} - Valor: {valor}')

for item in persona.items():
    print(f'Item: {item}')
# %%

#%% Ejercicio 2: Contador de Letras
"""
Crea un programa que cuente la cantidad de veces que aparece cada letra en una cadena de texto ingresada por el usuario y almacene los resultados en un diccionario.
"""
texto = input("Ingresa un texto: ")
contador_letras = {}

for letra in texto:
    if letra.isalpha():
        letra = letra.lower()
        if letra in contador_letras:
            contador_letras[letra] += 1
        else:
            contador_letras[letra] = 1

print("Contador de Letras:")
for letra, frecuencia in contador_letras.items():
    print(f"{letra}: {frecuencia}")
    
    
#%% Ejercicio 3: Diccionario de Precios
"""
Crea un programa que almacene los precios de varios productos en un diccionario y permita al usuario buscar el precio de un producto ingresando su nombre.
"""
productos = {"manzanas": 2.0, "bananas": 1.5, "naranjas": 2.5, "uvas": 3.0}

while True:
    print("1. Buscar precio de producto")
    print("2. Salir")
    
    opcion = input("Selecciona una opción (1/2): ")
    
    if opcion == "1":
        producto = input("Ingresa el nombre del producto: ").lower()
        if producto in productos:
            print(f"El precio de {producto} es ${productos[producto]:.2f}.")
        else:
            print("Producto no encontrado.")
    elif opcion == "2":
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
    

