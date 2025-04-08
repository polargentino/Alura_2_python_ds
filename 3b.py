'''
3 - A partir de la lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crea un código para 
generar una lista de tuplas en la que cada tupla tenga el primer elemento como la posición del 
nombre en la lista original y el segundo elemento siendo el propio nombre.
'''
# 3-

lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']


lista_de_tuplas = []
for i in range(len(lista)):
    lista_de_tuplas.append((i, lista[i]))
print(lista_de_tuplas)

'''
[(0, 'Pedro'), (1, 'Júlia'), (2, 'Otávio'), (3, 'Eduardo')]


¡Entendido! Vamos a analizar este código Python paso a paso:

lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']:

Se crea una lista llamada lista que contiene cuatro nombres (strings).
lista_de_tuplas = []:

Se inicializa una lista vacía llamada lista_de_tuplas. Esta lista se utilizará para almacenar las 
tuplas que se crearán.

for i in range(len(lista))::

Se inicia un bucle for que itera a través de los índices de la lista lista.

len(lista) devuelve la longitud de la lista lista, que es 4.

range(len(lista)) genera una secuencia de números desde 0 hasta 3 (0, 1, 2, 3).

En cada iteración del bucle, la variable i tomará uno de estos valores, representando el índice 
actual de la lista lista.

lista_de_tuplas.append((i, lista[i])):

Dentro del bucle, en cada iteración, se realiza lo siguiente:

i: Toma el valor del índice actual (0, 1, 2 o 3).

lista[i]: Accede al elemento de la lista lista en el índice actual.

(i, lista[i]): Se crea una nueva tupla que contiene dos elementos: el índice i y el nombre 
correspondiente de la lista lista.

lista_de_tuplas.append(...): Se utiliza el método .append() para añadir la tupla recién creada al 
final de la lista lista_de_tuplas.

print(lista_de_tuplas):

Después de que el bucle for ha terminado de iterar a través de todos los elementos de la lista lista, 
esta línea imprime el contenido de la lista lista_de_tuplas.

En resumen:

El código toma una lista de nombres y crea una nueva lista llamada lista_de_tuplas. Itera a través 
de la lista original utilizando sus índices. En cada iteración, crea una tupla que contiene el 
índice del nombre y el nombre en sí, y luego añade esta tupla a la nueva lista.

Resultado de la ejecución:

La salida del código será la siguiente lista de tuplas:

[(0, 'Pedro'), (1, 'Júlia'), (2, 'Otávio'), (3, 'Eduardo')]

Cada tupla en la lista resultante contiene el índice del nombre en la lista original y el nombre
 correspondiente.
'''