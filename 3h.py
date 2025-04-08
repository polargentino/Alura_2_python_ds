'''
9 - Una empresa tiene sucursales distribuidas en los estados de la región Sudeste de Brasil. 
En una de las tablas de registro de las sucursales, hay una columna que contiene la información de a 
qué estado pertenece: estados =['CMX', 'OAX', 'PUE', 'PUE', 'CMX', 'PUE', 'OAX', 'OAX', 'OAX', 
'CMX', 'CMX', 'PUE', 'OAX', 'CMX', 'VER', 'PUE', 'VER', 'CMX', 'PUE', 'CMX', 'OAX', 'CMX', 'PUE'].

La empresa siempre está abriendo nuevas sucursales, por lo que la tabla está constantemente 
recibiendo nuevos registros y al gerente le gustaría tener la información actualizada de la cantidad 
de sucursales en cada estado.

A partir de la columna con la información de los estados, crea un diccionario utilizando la 
comprensión de diccionarios (dict comprehension) con la clave siendo el nombre de un estado y el 
valor siendo la cantidad de veces que aparece el estado en la lista.

Consejo: Puedes hacer un paso intermedio para generar una lista de listas en la que cada una de las 
listas tenga el nombre de solo un estado con valores repetidos.

'''


# 9 -
estados =['CMX', 'OAX', 'PUE', 'PUE', 'CMX', 'PUE', 'OAX', 'OAX', 'OAX', 
'CMX', 'CMX', 'PUE', 'OAX', 'CMX', 'VER', 'PUE', 'VER', 'CMX', 'PUE', 'CMX', 'OAX', 'CMX', 'PUE']

# Almacenando los estados sin repetición de valor
estados_unicos = list(set(estados))

# Creando una lista de listas con valores repetidos de cada estado
lista_de_listas = []
for estado in estados_unicos:
    lista = [e for e in estados if e == estado]
    lista_de_listas.append(lista)
print(lista_de_listas)

# Creando un diccionario en el que la clave es el nombre de cada estado único y el valor es la 
# cantidad de elementos
conteo_valores = {estados_unicos[i]: len(lista_de_listas[i]) for i in range(len(estados_unicos))}
print(conteo_valores)

'''
[['VER', 'VER'], ['CMX', 'CMX', 'CMX', 'CMX', 'CMX', 'CMX', 'CMX', 'CMX'], 
['PUE', 'PUE', 'PUE', 'PUE', 'PUE', 'PUE', 'PUE'], ['OAX', 'OAX', 'OAX', 'OAX', 'OAX', 'OAX']]
{'VER': 2, 'CMX': 8, 'PUE': 7, 'OAX': 6}
                                          
'''
#------------------------------------------------------------------------------------------------------

estados =['CMX', 'OAX', 'PUE', 'PUE', 'CMX', 'PUE', 'OAX', 'OAX', 'OAX',
'CMX', 'CMX', 'PUE', 'OAX', 'CMX', 'VER', 'PUE', 'VER', 'CMX', 'PUE', 'CMX', 'OAX', 'CMX', 'PUE']

# Almacenando los estados sin repetición de valor
estados_unicos = list(set(estados))
print(f"Estados únicos encontrados: {estados_unicos}")

# Creando una lista de listas con valores repetidos de cada estado
lista_de_listas = []
for estado in estados_unicos:
    lista = [e for e in estados if e == estado]
    lista_de_listas.append(lista)
print(f"\nLista de listas por estado: {lista_de_listas}")

# Creando un diccionario en el que la clave es el nombre de cada estado único y el valor es la
# cantidad de elementos
conteo_valores = {estados_unicos[i]: len(lista_de_listas[i]) for i in range(len(estados_unicos))}
print(f"\nConteo de ocurrencias por estado: {conteo_valores}")

'''
Estados únicos encontrados: ['VER', 'OAX', 'CMX', 'PUE']

Lista de listas por estado: [['VER', 'VER'], ['OAX', 'OAX', 'OAX', 'OAX', 'OAX', 'OAX'], ['CMX', 'CMX', 'CMX', 'CMX', 'CMX', 'CMX', 'CMX', 'CMX'], ['PUE', 'PUE', 'PUE', 'PUE', 'PUE', 'PUE', 'PUE']]

Conteo de ocurrencias por estado: {'VER': 2, 'OAX': 6, 'CMX': 8, 'PUE': 7}


Gemini 2.0 Flash:
Explicación del código:
----------------------

estados = [...]: Se define una lista llamada estados que contiene una serie de códigos de estado 
(strings), con algunos valores repetidos.

estados_unicos = list(set(estados)):

Se utiliza la función set() para convertir la lista estados en un conjunto. Los conjuntos en Python 
automáticamente eliminan los elementos duplicados, por lo que set(estados) contendrá solo los códigos 
de estado únicos.

Luego, se utiliza list() para convertir el conjunto resultante nuevamente en una lista.

Se imprime la lista estados_unicos para mostrar los códigos de estado sin repetición.

lista_de_listas = []: Se inicializa una lista vacía llamada lista_de_listas. Esta lista se utilizará 
para almacenar listas, donde cada lista contendrá todas las ocurrencias de un estado único de la 
lista original estados.

for estado in estados_unicos:: Se inicia un bucle for que itera a través de cada código de estado 
único en la lista estados_unicos.

lista = [e for e in estados if e == estado]:

Dentro del bucle, para cada estado único, se utiliza una comprensión de lista para crear una nueva 
lista llamada lista.

for e in estados: Itera a través de cada elemento (e) en la lista original estados.

if e == estado: Verifica si el elemento actual e es igual al estado único actual del bucle exterior.

[e for ... if ...]: Si la condición es verdadera (el elemento de la lista original coincide con el 
estado único), ese elemento (e) se agrega a la nueva lista lista.

En resumen, esta línea crea una lista que contiene todas las ocurrencias del estado único actual 
dentro de la lista estados original.

lista_de_listas.append(lista): La lista lista (que contiene todas las repeticiones de un estado único) 
se añade a la lista lista_de_listas.

Se imprime la lista_de_listas para mostrar cómo se han agrupado las ocurrencias de cada estado único 
en listas separadas.

conteo_valores = {estados_unicos[i]: len(lista_de_listas[i]) for i in range(len(estados_unicos))}:

Se crea un diccionario llamado conteo_valores utilizando una comprensión de diccionario.

for i in range(len(estados_unicos)): Itera a través de los índices de la lista estados_unicos.

estados_unicos[i]: Utiliza el índice i para acceder a un código de estado único de la lista 
estados_unicos. Esta será la clave del diccionario.

len(lista_de_listas[i]): Utiliza el mismo índice i para acceder a la lista correspondiente en 
lista_de_listas. len() calcula la longitud de esta lista, que representa la cantidad de veces 
que el estado único aparece en la lista original estados. Este será el valor asociado a la clave en 
el diccionario.

{clave: valor for ... in ...}: La comprensión de diccionario crea el diccionario conteo_valores 
donde cada estado único es una clave y su valor es la cantidad de veces que aparece en la lista 
original.

Se imprime el diccionario conteo_valores para mostrar el conteo de ocurrencias de cada estado único.

En resumen, el código toma una lista de estados con repeticiones y realiza los siguientes pasos:

* Identifica los estados únicos.
* Crea una lista de listas, donde cada sublista contiene todas las ocurrencias de un estado único.
* Crea un diccionario que mapea cada estado único a la cantidad de veces que aparece en la lista 
original.

* Se han añadido print() con f-strings para que la salida sea más descriptiva y cumpla con la solicitud 
de explicación.
'''