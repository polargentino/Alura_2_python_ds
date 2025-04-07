'''
9 - Has recibido un desafío para calcular la raíz cuadrada de una lista de números, 
identificando cuáles resultan en un número entero. La lista es la siguiente:
'''

import math

numeros = [2, 8, 15, 23, 91, 112, 256]
raices_enteras = [num for num in numeros if math.sqrt(num) % 1 == 0]
print("Números con raíces enteras:", raices_enteras)

'''
Vamos a desglosar este código Python línea por línea para entender qué hace:

import math:

Esta línea importa el módulo math, que proporciona funciones matemáticas, incluida la función 
math.sqrt() para calcular raíces cuadradas.
numeros = [2, 8, 15, 23, 91, 112, 256]:

Aquí, se crea una lista llamada numeros que contiene números enteros. Esta lista representa el 
conjunto de números que se van a evaluar.

raices_enteras = [num for num in numeros if math.sqrt(num) % 1 == 0]:

Esta línea utiliza una construcción llamada "comprensión de lista" para crear una nueva lista 
llamada raices_enteras.

for num in numeros: Itera a través de cada número (num) en la lista numeros.
math.sqrt(num): Calcula la raíz cuadrada del número actual.

math.sqrt(num) % 1 == 0: Verifica si la raíz cuadrada tiene una parte decimal igual a 0. 

|En otras palabras, verifica si la raíz cuadrada es un número entero|.
|-------------------------------------------------------------------|
[num for ... if ...]: Si la condición es verdadera (la raíz cuadrada es entera), el número 
actual (num) se agrega a la nueva lista raices_enteras.
print("Números con raíces enteras:", raices_enteras):

Finalmente, esta línea imprime en la consola la frase "Números con raíces enteras:" seguida de 
la lista raices_enteras, que contiene los números de la lista original que tienen raíces cuadradas 
enteras.
En resumen:

[El código toma una lista de números.
Calcula la raíz cuadrada de cada número.
Filtra los números cuya raíz cuadrada es un número entero.
Imprime la lista de números filtrados.
Ejemplo de ejecución:

En este caso, la salida sería:

Números con raíces enteras: [256]
Esto se debe a que la raíz cuadrada de 256 es 16, que es un número entero, mientras que las 
raíces cuadradas de los demás números en la lista no son números enteros.
'''