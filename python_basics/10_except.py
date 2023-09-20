#%% División de 2 numeros
num1 = int(input("Ingrese un numero"))
num2 = int(input("Ingrese otro numero"))

try:
    resultado = num1/num2
except ZeroDivisionError:
    print("No se puede dividir para 0")
    resultado = None

print("El resultado es:", resultado)
# %%
