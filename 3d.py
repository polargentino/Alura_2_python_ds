'''
5 - Crea un diccionario usando la comprensión de diccionarios (dict comprehension) en el que las
claves estén en la lista meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 
'Out', 'Nov', 'Dez'] y los valores estén en gasto = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 
560, 840, 360].
'''
# 5 -

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 
'Out', 'Nov', 'Dez']

gasto = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 
560, 840, 360]


diccionario = {meses[i]: gasto[i] for i in range(len(meses))}
print(diccionario)

'''
{'Jan': 860, 'Fev': 490, 'Mar': 1010, 'Abr': 780, 'Mai': 900, 'Jun': 630, 'Jul': 590, 'Ago': 770, 
'Set': 620, 'Out': 560, 'Nov': 840, 'Dez': 360}


Gemini 2.0 Flash: 
¡Entendido! Vamos a analizar este código Python paso a paso:

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']:

Se crea una lista llamada meses que contiene las abreviaturas de los meses del año en portugués.

gasto = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]:

Se crea una lista llamada gasto que contiene doce números enteros, presumiblemente representando los 
gastos correspondientes a cada mes de la lista meses.

diccionario = {meses[i]: gasto[i] for i in range(len(meses))}:

Esta línea utiliza una construcción llamada comprensión de diccionario para crear un diccionario 
llamado diccionario. Vamos a desglosarla:

{... for ... in ...}: Esta es la sintaxis básica para la comprensión de diccionarios.

for i in range(len(meses)): Itera a través de los índices de la lista meses. len(meses) devuelve 
la longitud de la lista (que es 12), y range(len(meses)) genera una secuencia de números desde 0 
hasta 11. En cada iteración, la variable i tomará uno de estos valores, representando el índice actual.

meses[i]: Accede al elemento de la lista meses en el índice actual i. Este valor se utilizará como 
la clave del diccionario.

gasto[i]: Accede al elemento de la lista gasto en el mismo índice i. Este valor se utilizará como 
el valor asociado a la clave en el diccionario.

meses[i]: gasto[i]: Define la pareja clave-valor para cada entrada del diccionario.
print(diccionario):

Finalmente, esta línea imprime el diccionario diccionario que se ha creado.
En resumen:

El código toma dos listas paralelas (meses y gasto) y las utiliza para crear un diccionario. 

La comprensión de diccionario itera a través de los índices de la lista de meses y utiliza el mes 
en la posición actual como la clave y el gasto en la misma posición de la lista de gastos como el 
valor asociado a esa clave. El resultado es un diccionario donde las claves son los meses y los 
valores son los gastos correspondientes.

Resultado de la ejecución:

Dado el contenido de las listas meses y gasto, la salida del código será el siguiente diccionario:

{'Jan': 860, 'Fev': 490, 'Mar': 1010, 'Abr': 780, 'Mai': 900, 'Jun': 630, 'Jul': 590, 'Ago': 770, 
'Set': 620, 'Out': 560, 'Nov': 840, 'Dez': 360}

Este diccionario asocia cada mes con su respectivo gasto.
'''