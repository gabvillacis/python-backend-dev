#%% Ejercicio 1: Eliminar Duplicados en una Lista:
"""
Crea una lista con elementos duplicados.
Escribe un programa que elimine los elementos duplicados y muestre la lista sin duplicados.
"""
lista = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = []

for elemento in lista:
    if elemento not in lista_sin_duplicados:
        lista_sin_duplicados.append(elemento)

print("Lista original:", lista)
print("Lista sin duplicados:", lista_sin_duplicados)


#%%Ejercicio 2: Ordenar una Lista de Palabras:
"""
Crea una lista de palabras.
Escribe un programa que ordene la lista alfabéticamente.
Muestra la lista ordenada en pantalla.
"""
palabras = ["manzana", "cereza", "banana", "kiwi", "uva", "pera"]
palabras.sort()

print("Lista ordenada alfabéticamente:", palabras)

#%%Ejercicio 3: Lista de Compras con Total:
"""
Crea una lista de tuplas, donde cada tupla contiene el nombre de un producto y su precio.
Escribe un programa que calcule el total de la lista de compras sumando los precios de los productos.
Muestra la lista de compras y el total en pantalla.
"""
lista_compras = [("Manzanas", 2.0), ("Leche", 1.5), ("Pan", 1.0), ("Huevos", 3.0)]
total = sum(precio for _,precio in lista_compras)

print("Lista de Compras:")
for producto, precio in lista_compras:
    print(f"{producto}: ${precio:.2f}")

print(f"Total: ${total:.2f}")


#%%Ejercicio 4: Dividir una Tupla en Mitades:
"""
Crea una tupla con un número par de elementos.
Escribe un programa que divida la tupla en dos mitades y las muestre en pantalla.
"""
tupla = (1, 2, 3, 4, 5, 6)
mitad1 = tupla[:len(tupla) // 2]
mitad2 = tupla[len(tupla) // 2:]

print("Tupla original:", tupla)
print("Mitad 1:", mitad1)
print("Mitad 2:", mitad2)

#%%Ejercicio 5: Contar Elementos en una Tupla:
"""
Crea una tupla con elementos repetidos.
Escribe un programa que cuente cuántas veces aparece un elemento específico en la tupla.
Muestra el resultado en pantalla.
"""
tupla = (1, 2, 2, 3, 4, 4, 4, 5)
elemento_a_contar = 4
conteo = tupla.count(elemento_a_contar)

print(f"La cantidad de veces que {elemento_a_contar} aparece en la tupla es: {conteo}")

#%%Ejercicio 6: Unir Varias Tuplas:
"""Crea varias tuplas con diferentes elementos.
Escribe un programa que las una en una sola tupla.
Muestra la tupla resultante en pantalla."""
tupla1 = (1, 2, 3)
tupla2 = ("a", "b", "c")
tupla3 = (True, False)

tupla_resultante = tupla1 + tupla2 + tupla3

print("Tupla Resultante:", tupla_resultante)