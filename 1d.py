'''
5 - Crea un programa que solicite a la persona usuaria ingresar dos números enteros y 
calcule la potencia del primer número elevado al segundo.
'''

import math
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
resultado = math.pow(num1, num2) # calcula la potencia de num1 elevado a num2.
print(f"La potencia de {num1} elevado a {num2} es {resultado}")

'''
Es importante notar que la función math.pow() siempre devuelve un valor de tipo float 
(número decimal), incluso si los números de entrada son enteros.


Ingrese el primer número entero: 2
Ingrese el segundo número entero: 3
La potencia de 2 elevado a 3 es 8.0
'''