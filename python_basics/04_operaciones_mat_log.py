# Ejercicios de Operaciones Matemáticas y Lógicas

#%% Ejercicio 1: Suma de dos números
# Pida al usuario que ingrese dos números y muestre la suma
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
suma = num1 + num2
print("La suma es:", suma)


#%% Ejercicio 2: Número par o impar
# Pila al usuario un número e indique si es par o impar
numero = float(input("Ingresa un número: "))
if numero%2==0:
    print("El número ingresado es par")
else:
    print("El número ingresado es impar")


#%% Ejercicio 3: Área de un triángulo
"""Pide al usuario que ingrese la base y la altura de un triángulo. Calcula y muestra el área del triángulo utilizando la fórmula: Área = (base * altura) / 2."""
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))
area = (base * altura) / 2
print("El área del triángulo es:", area)


#%% Ejercicio 4: Calculadora de BMI
""" Pide al usuario que ingrese su peso en kilogramos y su altura en metros.
Calcula y muestra su BMI utilizando la fórmula: BMI = Peso / (Altura^2).
Luego, clasifica el BMI en las categorías: "Bajo peso", "Normal", "Sobrepeso" u "Obeso" según los siguientes rangos:

BMI menor que 18.5 => Bajo peso
BMI mayor o igual que 18.5 y menor que 24.9 => Peso normal
BMI mayor o igual que 24.9 y menor que 29.9 => Sobrepeso
BMI mayor que 29.9 => Obeso
"""

peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))
bmi = peso / (altura ** 2)

print("Tu BMI es:", bmi)
if bmi < 18.5:
    print("Tienes bajo peso.")
elif bmi>=18.5 and bmi < 24.9:
    print("Tienes un peso normal.")
elif bmi>=24.9 and bmi < 29.9:
    print("Tienes sobrepeso.")
else:
    print("Tienes obesidad.")

#%% Ejercicio 5: Calculadora de operaciones matemáticas básicas
"""
Pide al usuario que ingrese dos números y la operación que desea realizar (suma, resta, multiplicación o división). El programa realizará la operación seleccionada y mostrará el resultado:
"""

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Solicitar al usuario seleccionar la operación
print("Selecciona la operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
opcion = int(input("Ingresa el número de la operación deseada (1/2/3/4): "))

# Realizar la operación seleccionada
if opcion == 1:
    resultado = num1 + num2
    operacion = "suma"
elif opcion == 2:
    resultado = num1 - num2
    operacion = "resta"
elif opcion == 3:
    resultado = num1 * num2
    operacion = "multiplicación"
elif opcion == 4:
    if num2 == 0:
        print("No se puede dividir por cero.")
        resultado = None
    else:
        resultado = num1 / num2
        operacion = "división"
else:
    print("Opción no válida.")
    resultado = None

# Mostrar el resultado si la operación fue válida
if resultado is not None:
    print(f"Número 1: {num1}\nNúmero 2: {num2}")
    print(f"El resultado de la {operacion} es: {resultado}")