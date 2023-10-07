# Ejercicios de POO
## Ejercicio #1
Crear una clase en Python que se llame “CuentaBancaria” la cual represente una cuenta de ahorros en un banco.
La clase debe tener los atributos: número de cuenta, titular y saldo.

Crear un constructor con los parámetros número de cuenta, titular y saldo e inicializar los atributos.

Crear un método depositar que maneje la acción de depositar dinero en la cuenta.

Crear un método retirar que maneje la acción de retirar dinero de la cuenta, considerando que cada vez que se hace un retiro el banco cobra una comisión del 5% del valor retirado y lo descuenta del saldo. (No se puede retirar si el saldo es insuficiente, mostrar los mensajes de error correspondientes).

Crear un método display que permita mostrar los detalles de la cuenta.

## Ejercicio #2

Crea una jerarquía de clases para modelar vehículos. Comienza con una clase base llamada `Vehiculo` que tenga los siguientes atributos y métodos:

Clase Vehiculo:
- Atributos:
  - `marca` (cadena de texto): La marca del vehículo.
  - `modelo` (cadena de texto): El modelo del vehículo.
  - `anio` (entero): El año de fabricación del vehículo.
  - `precio` (float): El precio del vehículo en dólares.
- Métodos:
  - `_init_(self, marca, modelo, anio, precio)`: Constructor que inicializa los atributos del vehículo.
  - `obtener_informacion(self)`: Un método que devuelve una cadena de texto con la información completa del vehículo.
  - `calcular_seguro(self)`: Un método que calcula el costo del seguro basado en el precio del vehículo siguiendo estas reglas:
    - Si el precio del vehículo es menor o igual a $10,000, el costo del seguro es el 5% del precio.
    - Si el precio del vehículo está entre $10,001 y $30,000, el costo del seguro es el 8% del precio.
    - Si el precio del vehículo es mayor a $30,000, el costo del seguro es el 12% del precio.

Luego, crea al menos dos clases derivadas de `Vehiculo`: `Automovil` y `Motocicleta`. Estas clases deben heredar de `Vehiculo` y agregar atributos y métodos específicos:

Clase Automóvil (derivada de Vehiculo):
- Atributos adicionales:
  - `numero_puertas` (entero): El número de puertas del automóvil.
- Métodos adicionales:
  - `obtener_tipo(self)`: Un método que devuelve la cadena "Automóvil".
- Sobrescribe el método `calcular_seguro` para considerar el número de puertas. Si el automóvil tiene más de dos puertas, el costo del seguro se reduce en un 2%.

Clase Motocicleta (derivada de Vehiculo):
- Atributos adicionales:
  - `cilindrada` (entero): La cilindrada de la motocicleta en cc.
- Métodos adicionales:
  - `obtener_tipo(self)`: Un método que devuelve la cadena "Motocicleta".
- Sobrescribe el método `calcular_seguro` para considerar la cilindrada. Si la cilindrada es mayor a 1000 cc, el costo del seguro se incrementa en un 5%.

Crea instancias de automóviles y motocicletas, calcula el costo del seguro para cada uno y muestra la información del vehículo junto con el costo del seguro.
