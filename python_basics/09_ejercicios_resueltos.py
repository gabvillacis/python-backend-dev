#%% Ejercicio #1
"""
Tabla de Multiplicación: Escribe un programa que muestre la tabla de multiplicación de un número específico ingresado por el usuario.
"""
numero = int(input("Ingresa un número para mostrar su tabla de multiplicación: "))

print(f"Tabla de multiplicación del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


#%% Ejercicio #2
"""
Suma de Dígitos: Escribe una función que tome un número entero y calcule la suma de sus dígitos.
"""
def suma_digitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma

numero = int(input("Ingresa un número entero: "))
resultado = suma_digitos(numero)
print(f"La suma de los dígitos es: {resultado}")

#%% Ejercicio #3
"""
Potencia de un Número: Crea una función que tome dos números, base y exponente, y calcule la potencia. Utilice un bucle for.
"""
def potencia(base, exponente):
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado

base = float(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))
resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")


#%% Ejercicio #4
"""
Invertir Lista: Crea una función que tome una lista y la devuelva invertida.
"""
def invertir_lista(lista):
    return lista[::-1]

lista = [1, 2, 3, 4, 5]
resultado = invertir_lista(lista)
print(f"Lista invertida: {resultado}")


#%% Ejercicio #5
"""
Conteo de Elementos en una Tupla: Crea una función que tome una tupla y devuelva un diccionario que cuente cuántas veces aparece cada elemento en la tupla.
"""
def contar_elementos(tupla):
    contador = {}
    for elemento in tupla:
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1
    return contador

tupla = (1, 2, 2, 3, 4, 4, 5)
resultado = contar_elementos(tupla)
print(f"Conteo de elementos en la tupla: {resultado}")

# %%
