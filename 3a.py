'''

2 - Crea un código para generar una lista que almacene el tercer elemento de cada tupla contenida 
en la siguiente lista de tuplas:
'''
# 2-

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]


lista = []
for tupla in lista_de_tuplas:
    lista.append(tupla[2])
print(lista)

'''
[81, 67, 83]

El método .append() es una función fundamental utilizada en Python para modificar listas, 
añadiendo un nuevo elemento al final de la lista existente.

Aquí tienes una definición más detallada y sus características clave:

Definición:

El método .append() toma un único argumento (el elemento que se desea agregar) y lo añade al final 
de la lista sobre la cual se invoca. La lista original es modificada directamente; no se crea una 
nueva lista.

Características principales:

Modifica la lista original: A diferencia de algunas operaciones que crean una nueva lista, .append() 
altera la lista existente en memoria.

Añade al final: El nuevo elemento siempre se coloca en la última posición de la lista, incrementando 
su longitud en uno.

Acepta cualquier tipo de dato: Puedes agregar cualquier tipo de objeto a una lista usando .append(), 
incluyendo números, strings, booleanos, otras listas, tuplas, diccionarios, objetos personalizados, 
etc.

No devuelve un nuevo valor: El método .append() no retorna una nueva lista ni ningún otro valor 
específico (formalmente, devuelve None). Su efecto principal es la modificación de la lista.

Es un método de objeto lista: .append() solo puede ser llamado en objetos que son de tipo list en 
Python.

Analogía:
--------
Imagina una fila de personas. El método .append() sería como añadir una nueva persona al final de 
esa fila. La fila original ahora es más larga y la nueva persona está al final.

Ejemplos:

Python

mi_lista = [1, 2, 3]
mi_lista.append(4)
print(mi_lista)  # Salida: [1, 2, 3, 4]

otra_lista = ["manzana", "banana"]
otra_lista.append("naranja")
print(otra_lista)  # Salida: ['manzana', 'banana', 'naranja']

lista_mixta = [10, "hola", True]
lista_mixta.append([5, 6])
print(lista_mixta)  # Salida: [10, 'hola', True, [5, 6]]


.append() es la manera más común y eficiente de extender una lista existente añadiendo un solo 
elemento al final. Es una operación fundamental para construir y manipular listas dinámicamente 
en Python.
'''