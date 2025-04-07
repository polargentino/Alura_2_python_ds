'''
5 - Has sido contratado como científico(a) de datos de una asociación de skate. Para analizar las 
notas recibidas por los skaters en algunas competiciones a lo largo del año, necesitas crear un 
código que calcule la puntuación de los atletas. Para ello, tu código debe recibir 5 notas 
ingresadas por los jueces.
'''

notas = [float(input(f"Ingrese la nota {i + 1}: ")) for i in range(5)]
notas.sort()
media = sum(notas[1:4]) / 3
print(f"Nota de la maniobra: {media:.2f}")

'''
Ingrese la nota 1: 9.1
Ingrese la nota 2: 4.6
Ingrese la nota 3: 3.7
Ingrese la nota 4: 7.8
Ingrese la nota 5: 3.9
Nota de la maniobra: 5.43

Gemini 2-0 Flash: Claro, vamos a desglosar este código Python paso a paso para entender qué hace:

notas = [float(input(f"Ingrese la nota {i + 1}: ")) for i in range(5)]:

Esta línea utiliza una comprensión de lista para solicitar al usuario que ingrese 5 notas y las 
almacena en una lista llamada notas.

for i in range(5): Itera 5 veces, con i tomando valores de 0 a 4.

input(f"Ingrese la nota {i + 1}: "): Muestra un mensaje en la consola solicitando al usuario 
que ingrese cada nota (nota 1, nota 2, ..., nota 5).

float(...): Convierte la entrada del usuario (que es una cadena de texto) a un número decimal (float).
[... for i in range(5)]: Crea una lista con las 5 notas ingresadas por el usuario.

notas.sort():

Esta línea ordena la lista notas en orden ascendente (de menor a mayor).

media = sum(notas[1:4]) / 3:

Esta línea calcula la media de las 3 notas intermedias (después de ordenar la lista).

notas[1:4]: Crea una sublista que contiene las notas desde el índice 1 hasta el índice 3 
(exclusivo). Esto equivale a las 3 notas intermedias.

sum(...): Suma las notas en la sublista.

/ 3: Divide la suma por 3 para obtener la media.

El resultado se almacena en la variable media.

print(f"Nota de la maniobra: {media:.2f}"):

Finalmente, esta línea imprime la media calculada en la consola.

f"...": Es una cadena f, que permite insertar variables directamente dentro de la cadena de texto.

{media:.2f}: Formatea la media para que se muestre con 2 decimales.

La salida mostrará una frase como "Nota de la maniobra: 8.50".

En resumen:

El código solicita al usuario que ingrese 5 notas.
Ordena las notas de menor a mayor.
Calcula la media de las 3 notas intermedias.
Imprime la media calculada con 2 decimales.
Ejemplo de ejecución:

Si el usuario ingresa las notas 7, 9, 6, 8 y 10, la salida sería:

Nota de la maniobra: 8.33
Esto se debe a que las notas ordenadas son [6, 7, 8, 9, 10], y la media de las 3 notas intermedias (7, 8, 9) es 8.33.
'''