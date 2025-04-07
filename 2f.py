'''
7 - Has recibido una demanda para tratar 2 listas con los nombres y apellidos de cada estudiante 
concatenándolos para presentar sus nombres completos en la forma Nombre Apellido. Las listas son:
'''

nombres = ["juan", "MaRia", "JOSÉ"]
sobrenombres = ["SILVA", "sosa", "Tavares"]

# Normalizar nombres y apellidos y crear una nueva lista con los nombres completos
nombres_normalizados = map(lambda x: x.capitalize(), nombres)
sobrenombres_normalizados = map(lambda x: x.capitalize(), sobrenombres)
nombres_completos = list(map(lambda x, y: f"Nome completo: {x} {y}", nombres_normalizados, sobrenombres_normalizados))
print(nombres_completos)

'''
['Nome completo: Juan Silva', 'Nome completo: Maria Sosa', 'Nome completo: José Tavares']


Claro, vamos a desglosar este código Python paso a paso para entender qué hace:

nombres = ["juan", "MaRia", "JOSÉ"]:

Se crea una lista llamada nombres que contiene nombres de personas, algunos con mayúsculas y 
minúsculas mezcladas.

sobrenombres = ["SILVA", "sosa", "Tavares"]:

Se crea una lista llamada sobrenombres que contiene apellidos (o sobrenombres), también con 
diferentes capitalizaciones.

nombres_normalizados = map(lambda x: x.capitalize(), nombres):

Se utiliza la función map() para aplicar una función lambda a cada elemento de la lista nombres.

lambda x: x.capitalize(): Esta función lambda toma un string x y devuelve una nueva string con la 
primera letra en mayúscula y el resto en minúsculas.

map(...): Aplica esta función capitalize() a cada nombre en la lista nombres. El resultado es un 
objeto map (un iterador) que contiene los nombres normalizados.

sobrenombres_normalizados = map(lambda x: x.capitalize(), sobrenombres):

De manera similar, se utiliza map() y una función lambda para normalizar los elementos de la lista 
sobrenombres, capitalizando la primera letra de cada apellido. El resultado es un objeto map con los 
apellidos normalizados.

nombres_completos = list(map(lambda x, y: f"Nome completo: {x} {y}", nombres_normalizados, 
sobrenombres_normalizados)):

Aquí, se utiliza map() nuevamente, pero esta vez con dos iterables: nombres_normalizados y 
sobrenombres_normalizados.

lambda x, y: f"Nome completo: {x} {y": Esta función lambda toma dos argumentos, x (un nombre 
normalizado) e y (un apellido normalizado), y devuelve una cadena f formateada como "Nome completo: 
[nombre] [apellido]".

map(...): Aplica esta función lambda a los elementos correspondientes de los dos iteradores 
nombres_normalizados y sobrenombres_normalizados. Es importante notar que map() iterará hasta que 
el iterable más corto se agote. En este caso, ambas listas tienen la misma longitud.

list(...): Convierte el objeto map resultante en una lista llamada nombres_completos.

print(nombres_completos):

Finalmente, se imprime la lista nombres_completos en la consola.

En resumen:
----------
El código toma dos listas de nombres y apellidos (con diferentes capitalizaciones). Luego, normaliza 
la capitalización de ambos (primera letra en mayúscula, resto en minúsculas) utilizando la 
función map() y una función lambda. Finalmente, combina los nombres y apellidos normalizados 
en una nueva lista de nombres completos con el formato "Nome completo: [nombre] [apellido]" 
utilizando map() y una función lambda que utiliza f-strings para la concatenación.

Resultado de la ejecución:

La salida del código será:

['Nome completo: Juan Silva', 'Nome completo: Maria Sosa', 'Nome completo: José Tavares']
'''