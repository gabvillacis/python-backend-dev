#%% Ejercicio 1: Contador Regresivo
"""
Escribe un programa que solicite al usuario ingresar un número positivo. Luego, utiliza un bucle while para contar regresivamente desde ese número hasta 1 e imprimir cada número en la pantalla.
"""

numero = int(input("Ingresa un número positivo: "))

while numero > 0:
    print(numero)
    numero -= 1
    
#%% Ejercicio 2: Suma de Números Enteros
"""
Escribe un programa que solicite al usuario ingresar una serie de números enteros. Utiliza un bucle while para sumar los números ingresados hasta que el usuario ingrese un número negativo. Luego, muestra la suma total.
"""

suma = 0
while True:
    numero = int(input("Ingresa un número entero (ingresa un número negativo para finalizar): "))    
    if numero < 0:
        break
    
    suma += numero
print(f"La suma de los números enteros es: {suma}")

#%% Ejercicio 3: Suma de Números Enteros Con Total Máx.
"""
Escriba un algoritmo que sume n números ingresados por el usuario y cuando la suma sea superior a 100 deje de pedir números y muestre el total.
"""

suma = 0
while True:
    numero = int(input("Ingrese un número"))
    suma += numero
    if (suma>100):
        break    

print(f"Suma total: {suma}")
# %%
