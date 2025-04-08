### Curso de Python para Data Science: trabajar con funciones, estructuras de datos y excepciones

## Realice este curso para Data Science y:
Entiende las funciones de las bibliotecas y paquetes en el lenguaje Python.
Conoce las funciones integradas (built-in functions) y sus utilidades.
Crea funciones personalizadas.
Trabaja con estructuras de datos compuestas y anidadas.
Construye listas y diccionarios siguiendo patrones mediante list y dict comprehension.
Aprende a manejar los tipos de errores y excepciones en códigos Python.
Maneja errores y comportamientos indeseados en tu código.

# Vamos a practicar lo que hemos aprendido hasta ahora resolviendo los problemas propuestos en código.

Calentamiento

1 - Escribe un código para instalar la versión 3.7.1 de la biblioteca matplotlib.

2 - Escribe un código para importar la biblioteca numpy con el alias np.

3 - Crea un programa que lea la siguiente lista de números y elija uno al azar.

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

Copia el código

4 - Crea un programa que genere aleatoriamente un número entero menor que 100.

5 - Crea un programa que solicite a la persona usuaria ingresar dos números enteros y calcule la potencia del primer número elevado al segundo.

Aplicando a proyectos

6 - Se debe escribir un programa para sortear a un seguidor de una red social para ganar un premio. La lista de participantes está numerada y debemos elegir aleatoriamente un número según la cantidad de participantes. Pide a la persona usuaria que proporcione el número de participantes del sorteo y devuelve el número sorteado.

7 - Has recibido una solicitud para generar números de token para acceder a la aplicación de una empresa. El token debe ser par y variar de 1000 a 9998. Escribe un código que solicite el nombre de la persona usuaria y muestre un mensaje junto a este token generado aleatoriamente.

print(f"Hola, {nombre_usuario}, tu token de acceso es {token_generado} ¡Bienvenido/a!")

Copia el código

8 - Para diversificar y atraer nuevos clientes, una lanchonete creó un ítem misterioso en su menú llamado "ensalada de frutas sorpresa". En este ítem, se eligen aleatoriamente 3 frutas de una lista de 12 para componer la ensalada de frutas del cliente. Crea el código que realice esta selección aleatoria según la lista dada.

frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]

Copia el código

9 - Has recibido un desafío para calcular la raíz cuadrada de una lista de números, identificando cuáles resultan en un número entero. La lista es la siguiente:

numeros = [2, 8, 15, 23, 91, 112, 256]

Copia el código

10 - Haz un programa para una tienda que vende césped para jardines. Esta tienda trabaja con jardines circulares y el precio del metro cuadrado de césped es de R$ 25,00. Pide a la persona usuaria el radio del área circular y devuelve el valor en reales de cuánto tendrá que pagar.

Ver opinión del instructor

### Opinión del instructor
--------------------------

A continuación presentamos las posibles respuestas al desafío propuesto:

1 - Escribe un código para instalar la versión 3.7.1 de la biblioteca matplotlib.

pip install matplotlib==3.7.1

Copia el código

2 - Escribe un código para importar la biblioteca numpy con el alias np.

import numpy as np

Copia el código

3 - Crea un programa que lea la siguiente lista de números y elija uno al azar.

import random

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
numero_aleatorio = random.choice(lista)
print(numero_aleatorio)

Copia el código

4 - Crea un programa que genere aleatoriamente un número entero menor que 100.

import random
numero_aleatorio = random.randrange(100)
print(numero_aleatorio)

Copia el código

5 - Crea un programa que solicite a la persona usuaria ingresar dos números enteros y calcule la potencia del primer número elevado al segundo.

import math
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
resultado = math.pow(num1, num2)
print(f"La potencia de {num1} elevado a {num2} es {resultado}")

Copia el código

6 - Se debe escribir un programa para sortear a un seguidor de una red social para ganar un premio. La lista de participantes está numerada y debemos elegir aleatoriamente un número según la cantidad de participantes. Pide a la persona usuaria que proporcione el número de participantes del sorteo y devuelve el número sorteado.

import random

cantidad_participantes = int(input("Ingrese la cantidad de participantes: "))
numero_sorteado = random.randint(1, cantidad_participantes)
print(f"El número sorteado es: {numero_sorteado}")

Copia el código

7 - Has recibido una solicitud para generar números de token para acceder a la aplicación de una empresa. El token debe ser par y variar de 1000 a 9998. Escribe un código que solicite el nombre de la persona usuaria y muestre un mensaje junto a este token generado aleatoriamente.

import random

nombre_usuario = input("Ingrese su nombre: ")
token_generado = random.randrange(1000, 9999, 2)
print(f"Hola, {nombre_usuario}, tu token de acceso es {token_generado} ¡Bienvenido/a!")

Copia el código

8 - Para diversificar y atraer nuevos clientes, una lanchonete creó un ítem misterioso en su menú llamado "ensalada de frutas sorpresa". En este ítem, se eligen aleatoriamente 3 frutas de una lista de 12 para componer la ensalada de frutas del cliente. Crea el código que realice esta selección aleatoria según la lista dada.

import random

frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]
seleccion_frutas = random.sample(frutas, 3)
print("Ensalada de frutas sorpresa:", seleccion_frutas)

Copia el código

9 - Has recibido un desafío para calcular la raíz cuadrada de una lista de números, identificando cuáles resultan en un número entero. La lista es la siguiente:

import math

numeros = [2, 8, 15, 23, 91, 112, 256]
raices_enteras = [num for num in numeros if math.sqrt(num) % 1 == 0]
print("Números con raíces enteras:", raices_enteras)

Copia el código

10 - Haz un programa para una tienda que vende césped para jardines. Esta tienda trabaja con jardines circulares y el precio del metro cuadrado de césped es de R$ 25,00. Pide a la persona usuaria el radio del área circular y devuelve el valor en reales de cuánto tendrá que pagar.

import math

precio_metro_cuadrado = 25.00
radio = float(input("Ingrese el radio del área circular en metros: "))
area = math.pi * math.pow(radio, 2)
costo_total = precio_metro_cuadrado * area

print(f"El costo total es de R$ {round(costo_total,2)}")