'''
4 - Crea una lista usando la comprensión de listas (list comprehension) que almacene solo el 
valor numérico de cada tupla en caso de que el primer elemento sea 'Apartamento', a partir de 
la siguiente lista de tuplas:

alquiler = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
'''

# 4 -
alquiler = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]


lista = [tupla[1] for tupla in alquiler if tupla[0]== 'Apartamento']
print(lista)

'''
[1700, 1400, 1900]


¡Entendido! Vamos a analizar este código Python paso a paso:

alquiler = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]:

Se crea una lista llamada alquiler. Esta lista contiene tuplas, donde cada tupla representa una 
propiedad en alquiler.

El primer elemento de cada tupla es el tipo de propiedad (string: 'Apartamento' o 'Casa').

El segundo elemento de cada tupla es el precio del alquiler (entero).

lista = [tupla[1] for tupla in alquiler if tupla[0]== 'Apartamento']:

Esta línea utiliza una construcción llamada comprensión de lista para crear una nueva lista llamada 
lista. Vamos a desglosarla:

for tupla in alquiler: Itera a través de cada tupla en la lista alquiler. En cada iteración, la 
variable tupla tomará el valor de una de las tuplas de la lista alquiler.

if tupla[0] == 'Apartamento': Esta es una condición que se evalúa para cada tupla. tupla[0] accede 
al primer elemento de la tupla (el tipo de propiedad). Si este elemento es igual a la cadena 
'Apartamento', la condición es verdadera.

tupla[1]: Si la condición del if es verdadera (es decir, si la tupla representa un apartamento), 
entonces se accede al segundo elemento de esa tupla, que es el precio del alquiler.

[... for ... if ...]: La estructura completa de la comprensión de lista significa: 
"Crea una nueva lista conteniendo el valor de tupla[1] para cada tupla en alquiler, siempre y cuando 
el primer elemento de la tupla (tupla[0]) sea igual a 'Apartamento'".

print(lista):

Finalmente, esta línea imprime el contenido de la lista lista en la consola.
En resumen:

El código itera a través de la lista alquiler. Para cada elemento (que es una tupla), verifica si el 
primer elemento de la tupla es la cadena 'Apartamento'. Si lo es, extrae el segundo elemento de esa 
tupla (el precio del alquiler) y lo agrega a la nueva lista llamada lista. Al final, imprime la lista 
de precios de alquiler de todos los apartamentos encontrados en la lista alquiler.

Resultado de la ejecución:

Dado el contenido de la lista alquiler, el código producirá la siguiente salida:

[1700, 1400, 1900]
Esto se debe a que las tuplas que representan apartamentos son ('Apartamento', 1700), 
('Apartamento', 1400), y ('Apartamento', 1900), y el código ha extraído el segundo elemento 
(el precio) de cada una de ellas para formar la nueva lista.
'''