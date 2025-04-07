'''
4 - Crea una lista de los cuadrados de los números de la siguiente lista 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Recuerda utilizar las funciones lambda y map() para calcular 
el cuadrado de cada elemento de la lista.
'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)

'''
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Claro, vamos a desglosar este código Python paso a paso para entender qué hace:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:

Aquí, se crea una lista llamada numeros que contiene los números enteros del 1 al 10.

cuadrados = list(map(lambda x: x**2, numeros)):

Esta línea utiliza la función map() junto con una función lambda para calcular el cuadrado de 
cada número en la lista numeros.

map(funcion, secuencia): Aplica la función proporcionada a cada elemento de la secuencia y 
devuelve un iterador con los resultados.

lambda x: x**2: Es una función lambda (función anónima) que toma un argumento x y devuelve su 
cuadrado (x**2).

list(...): Convierte el iterador devuelto por map() en una lista llamada cuadrados.
print(cuadrados):

Finalmente, esta línea imprime la lista cuadrados en la consola.
En resumen:
----------
El código toma una lista de números.
Calcula el cuadrado de cada número en la lista utilizando map() y una función lambda.
Imprime la lista de cuadrados en la consola.
Resultado de la ejecución:

La salida del código será:

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Esto se debe a que cada número en la lista original se eleva al cuadrado.
'''