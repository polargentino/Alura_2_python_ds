'''
1 - Crea un código para imprimir la suma de los elementos de cada una de las listas contenidas en 
la siguiente lista:
'''
# 1-

lista_de_listas = [[4, 6, 5, 9], [1, 0, 7, 2], [3, 4, 1, 8]]

for lista in lista_de_listas:
    print(sum(lista))

'''
24
10
16


¡Entendido! Vamos a analizar este código Python paso a paso:

lista_de_listas = [[4, 6, 5, 9], [1, 0, 7, 2], [3, 4, 1, 8]]:

Se crea una lista llamada lista_de_listas. Esta lista contiene otras listas como sus elementos. 

Cada una de las listas internas contiene cuatro números enteros.

for lista in lista_de_listas::

Se inicia un bucle for que itera a través de cada elemento de la lista lista_de_listas. En cada 
iteración, la variable lista tomará el valor de una de las listas internas.

En la primera iteración, lista será [4, 6, 5, 9].
En la segunda iteración, lista será [1, 0, 7, 2].
En la tercera iteración, lista será [3, 4, 1, 8].

print(sum(lista)):

Dentro del bucle, en cada iteración, se ejecuta la función sum(lista).

sum(lista) calcula la suma de todos los elementos dentro de la lista actual (la lista interna a 
la que hace referencia la variable lista).

El resultado de la suma se imprime en la consola utilizando la función print().
En resumen:

El código itera a través de una lista que contiene otras listas de números. Para cada una de estas 
listas internas, calcula la suma de sus elementos y luego imprime esa suma en la consola.

Resultado de la ejecución:

Dado el contenido de lista_de_listas, la salida del código será la siguiente:

24
10
16
Explicación de cada línea de la salida:

24: Es la suma de los elementos de la primera lista interna: 4 + 6 + 5 + 9 = 24.
10: Es la suma de los elementos de la segunda lista interna: 1 + 0 + 7 + 2 = 10.
16: Es la suma de los elementos de la tercera lista interna: 3 + 4 + 1 + 8 = 16.
'''