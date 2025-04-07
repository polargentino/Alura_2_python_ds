'''
10 - Haz un programa para una tienda que vende césped para jardines. Esta tienda trabaja con 
jardines circulares y el precio del metro cuadrado de césped es de R$ 25,00. Pide a la persona 
usuaria el radio del área circular y devuelve el valor en reales de cuánto tendrá que pagar.
'''

import math

precio_metro_cuadrado = 25.00
radio = float(input("Ingrese el radio del área circular en metros: "))
area = math.pi * math.pow(radio, 2)
costo_total = precio_metro_cuadrado * area

print(f"El costo total es de R$ {round(costo_total,2)}")

'''
Ingrese el radio del área circular en metros: 7
El costo total es de R$ 3848.45

Claro, vamos a desglosar este código Python paso a paso para entender qué hace:

import math:

Esta línea importa el módulo math de Python. El módulo math proporciona funciones matemáticas, 
incluyendo math.pi (el valor de π) y math.pow() (para calcular potencias).

precio_metro_cuadrado = 25.00:

Aquí, se define una variable llamada precio_metro_cuadrado y se le asigna el valor 25.00. Este valor 
representa el precio por metro cuadrado del área circular.

radio = float(input("Ingrese el radio del área circular en metros: ")):

Esta línea solicita al usuario que ingrese el radio del área circular en metros.
input() muestra el mensaje "Ingrese el radio del área circular en metros: " en la consola y espera 
a que el usuario escriba algo y presione Enter.
float() convierte la entrada del usuario (que es una cadena de texto) a un número decimal y lo 
almacena en la variable radio.

area = math.pi * math.pow(radio, 2):

Esta línea calcula el área del círculo.
math.pi proporciona el valor de π (aproximadamente 3.14159).
math.pow(radio, 2) calcula el radio al cuadrado (radio * radio).
El resultado de esta multiplicación (π * radio^2) se almacena en la variable area.

costo_total = precio_metro_cuadrado * area:

Esta línea calcula el costo total multiplicando el precio por metro cuadrado por el área del círculo.
El resultado se almacena en la variable costo_total.

print(f"El costo total es de R$ {round(costo_total, 2)}"):

Finalmente, esta línea imprime el costo total en la consola.
f"..." es una cadena f, que permite insertar variables directamente dentro de la cadena de texto.
round(costo_total, 2) redondea el valor de costo_total a 2 decimales.
La salida mostrará una frase como "El costo total es de R$ 3848.45".
En resumen:

El código calcula el costo total de un área circular dado su radio y el precio por metro cuadrado.
Solicita al usuario que ingrese el radio del círculo.
Calcula el área del círculo usando la fórmula π * radio^2.
Multiplica el área por el precio por metro cuadrado para obtener el costo total.
Imprime el costo total redondeado a 2 decimales.
Espero que esta explicación sea útil.
'''