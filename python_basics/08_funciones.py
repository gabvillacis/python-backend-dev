#%% Ejercicio 1: Dibujar rectángulo
"""
Escriba una función que pida la anchura y altura de un rectángulo y lo dibuje con '*':
"""
# Definición de función
def dibujar_rectangulo(anchura, altura):
    for i in range(altura):
        for j in range(anchura):
            print("* ", end="")
        print()

# Programa principal
anchura = int(input("Anchura del rectángulo: "))
altura = int(input("Altura del rectángulo: "))
dibujar_rectangulo(anchura, altura)


#%% Ejercicio 2: Validación de email
"""
Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".
"""
# Definición de función
def es_direccion_valida(direccion):
    return "@" in direccion

# Programa principal
direccion_email = input("Ingresa tu dirección de correo electrónico: ")

if es_direccion_valida(direccion_email):
    print("La dirección de correo es válida.")
else:
    print("La dirección de correo no es válida.") 