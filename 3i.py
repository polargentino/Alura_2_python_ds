'''
10 - En esa misma tabla de registro de sucursales, hay una columna con la información de la 
cantidad de personas empleadas y el gerente quisiera tener un agrupamiento de la suma de esas 
personas para cada estado. Las informaciones contenidas en la tabla son:

empleados = [('CMX', 16), ('OAX', 8), ('PUE', 9), ('PUE', 6), ('CMX', 10), ('PUE', 4), ('OAX',9),  
('OAX', 7), ('OAX', 12), ('CMX', 7), ('CMX', 11), ('PUE',8), ('OAX',8), ('CMX',9), ('VER', 13), 
('PUE', 5),  ('VER', 9), ('CMX', 12), ('PUE', 10), ('CMX', 7), ('OAX', 14), ('CMX', 10), 
('PUE', 12)]

A partir de la lista de tuplas, crea un diccionario en el que las claves son los nombres de los 
estados únicos y los valores son las listas con el número de empleados referentes al estado. 
También crea un diccionario en el que las claves son los nombres de los estados y los valores son 
la suma de empleados por estado.
'''

# 10 -
empleados = [('CMX', 16), ('OAX', 8), ('PUE', 9), ('PUE', 6), ('CMX', 10), ('PUE', 4), ('OAX',9),  
             ('OAX', 7), ('OAX', 12), ('CMX', 7), ('CMX', 11), ('PUE',8), ('OAX',8), ('CMX',9), ('VER', 13), 
             ('PUE', 5),  ('VER', 9), ('CMX', 12), ('PUE', 10), ('CMX', 7), ('OAX', 14), ('CMX', 10), 
             ('PUE', 12)]

# Almacenando los estados sin repetición de valor
estados_unicos = list(set([tupla[0] for tupla in empleados]))

# Creando una lista de listas con valores de empleados de cada estado
lista_de_listas = []
for estado in estados_unicos:
    lista = [tupla[1] for tupla in empleados if tupla[0] == estado]
    lista_de_listas.append(lista)
print(lista_de_listas)

# Creando un diccionario con datos agrupados de empleados por estado
agrupamiento_por_estado = {estados_unicos[i]: lista_de_listas[i] for i in range(len(estados_unicos))}
print(agrupamiento_por_estado)

# Creando un diccionario con la suma de empleados por estado
suma_por_estado = {estados_unicos[i]: sum(lista_de_listas[i]) for i in range(len(estados_unicos))}
print(suma_por_estado)

'''
[[13, 9], [8, 9, 7, 12, 8, 14], [9, 6, 4, 8, 5, 10, 12], [16, 10, 7, 11, 9, 12, 7, 10]]

{'VER': [13, 9], 'OAX': [8, 9, 7, 12, 8, 14], 'PUE': [9, 6, 4, 8, 5, 10, 12], 
'CMX': [16, 10, 7, 11, 9, 12, 7, 10]}
{'VER': 22, 'OAX': 58, 'PUE': 54, 'CMX': 82}
'''

#--------------------------------------------------------------------------------------------------------------------
# Gemini 2.0 Flash:
# 10 -
empleados = [('CMX', 16), ('OAX', 8), ('PUE', 9), ('PUE', 6), ('CMX', 10), ('PUE', 4), ('OAX', 9),
             ('OAX', 7), ('OAX', 12), ('CMX', 7), ('CMX', 11), ('PUE', 8), ('OAX', 8), ('CMX', 9),
             ('VER', 13), ('PUE', 5), ('VER', 9), ('CMX', 12), ('PUE', 10), ('CMX', 7), ('OAX', 14),
             ('CMX', 10), ('PUE', 12)]

# Almacenando los estados sin repetición de valor
estados_unicos = list(set([tupla[0] for tupla in empleados]))
print(f"Estados únicos encontrados: {estados_unicos}")

# Creando un diccionario en el que las claves son los nombres de los
# estados únicos y los valores son las listas con el número de empleados referentes al estado.
agrupamiento_por_estado = {}
for estado, cantidad in empleados:
    if estado not in agrupamiento_por_estado:
        agrupamiento_por_estado[estado] = []
    agrupamiento_por_estado[estado].append(cantidad)
print(f"\nAgrupamiento de empleados por estado: {agrupamiento_por_estado}")

# Creando un diccionario en el que las claves son los nombres de los estados
# y los valores son la suma de empleados por estado.
suma_por_estado = {}
for estado, cantidad in empleados:
    if estado not in suma_por_estado:
        suma_por_estado[estado] = 0
    suma_por_estado[estado] += cantidad
print(f"\nSuma de empleados por estado: {suma_por_estado}")

'''
Estados únicos encontrados: ['OAX', 'CMX', 'VER', 'PUE']

Agrupamiento de empleados por estado: {'CMX': [16, 10, 7, 11, 9, 12, 7, 10], 
'OAX': [8, 9, 7, 12, 8, 14], 'PUE': [9, 6, 4, 8, 5, 10, 12], 'VER': [13, 9]}

Suma de empleados por estado: {'CMX': 82, 'OAX': 58, 'PUE': 54, 'VER': 22}



Explicación del código:
-----------------------
empleados = [...]: Se define la lista de tuplas empleados, donde cada tupla contiene el código del 
estado (string) y la cantidad de empleados (integer) en una sucursal de ese estado.

estados_unicos = list(set([tupla[0] for tupla in empleados])):

Se crea una lista llamada estados_unicos que contiene los códigos de estado sin repetición.

[tupla[0] for tupla in empleados] es una comprensión de lista que extrae el primer elemento 
(el estado) de cada tupla en la lista empleados.

set(...) convierte esta lista en un conjunto, eliminando los duplicados.

list(...) convierte el conjunto resultante nuevamente en una lista.

Se imprime la lista de estados únicos para verificar.

# Creando un diccionario en el que las claves son los nombres de los estados únicos y los valores 
# son las listas con el número de empleados referentes al estado.:


Se inicializa un diccionario vacío llamado agrupamiento_por_estado.

Se itera a través de cada tupla (estado, cantidad) en la lista empleados.

if estado not in agrupamiento_por_estado:: Se verifica si el estado actual ya es una clave en el 
diccionario agrupamiento_por_estado.

agrupamiento_por_estado[estado] = []: Si el estado no es una clave, se crea una nueva entrada en el 
diccionario con el estado como clave y una lista vacía como valor. Esta lista se utilizará para 
almacenar las cantidades de empleados de ese estado.

agrupamiento_por_estado[estado].append(cantidad): Se agrega la cantidad de empleados de la tupla 
actual a la lista asociada con el estado en el diccionario.

Se imprime el diccionario agrupamiento_por_estado, que cumple con el primer requisito.

# Creando un diccionario en el que las claves son los nombres de los estados y los valores son 
# la suma de empleados por estado.:

Se inicializa un diccionario vacío llamado suma_por_estado.

Se itera a través de cada tupla (estado, cantidad) en la lista empleados.

if estado not in suma_por_estado:: Se verifica si el estado actual ya es una clave en el diccionario 
suma_por_estado.

suma_por_estado[estado] = 0: Si el estado no es una clave, se crea una nueva entrada en el 
diccionario con el estado como clave y el valor inicial de 0.

suma_por_estado[estado] += cantidad: Se suma la cantidad de empleados de la tupla actual al valor 
asociado con el estado en el diccionario.

Se imprime el diccionario suma_por_estado, que cumple con el segundo requisito.

El código ahora crea los dos diccionarios solicitados de manera clara y eficiente, iterando sobre la 
lista de empleados para agrupar y sumar la cantidad de empleados por estado. Los print() 
con f-strings hacen que la salida sea más descriptiva.
'''