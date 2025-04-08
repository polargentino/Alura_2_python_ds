'''
7 - Una clínica analiza datos de pacientes y almacena el valor numérico de la glucosa en una base 
de datos y le gustaría etiquetar los datos de la siguiente manera:

Glucosa igual o inferior a 70: 'Hipoglicemia'
Glucosa entre 70 y 99: 'Normal'
Glucosa entre 100 y 125: 'Alterada'
Glucosa superior a 125: 'Diabetes'
La clínica proporcionó parte de los valores y tu tarea es crear una lista de tuplas usando la 
comprensión de listas que contenga la etiqueta y el valor de la glucemia en cada tupla.

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
'''

# 7 -
glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]


etiquetas = [('Hipoglicemia', glucosa) if glucosa<= 70 else ('Normal', glucosa) 
             if glucosa< 100 else ('Alterada', glucosa) if glucosa< 125 
             else ('Diabetes', glucosa) for glucosa in glicemia]
print(etiquetas)

'''
[('Diabetes', 129), ('Normal', 82), ('Hipoglicemia', 60), ('Normal', 97), ('Alterada', 101), 
('Hipoglicemia', 65), ('Hipoglicemia', 62), ('Diabetes', 167), ('Normal', 87), ('Hipoglicemia', 53), 
('Hipoglicemia', 58), ('Normal', 92), ('Hipoglicemia', 66), ('Alterada', 120), ('Alterada', 109), 
('Hipoglicemia', 62), ('Normal', 86), ('Normal', 96), ('Alterada', 103), ('Normal', 88), 
('Diabetes', 155), ('Hipoglicemia', 52), ('Normal', 89), ('Normal', 73)]



¡Entendido! Vamos a analizar este código Python paso a paso:

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 
155, 52, 89, 73]:

Se crea una lista llamada glicemia que contiene una serie de valores numéricos, presumiblemente 
representando niveles de glucemia en la sangre.

etiquetas = [('Hipoglicemia', glucosa) if glucosa<= 70 else ('Normal', glucosa) 
             if glucosa< 100 else ('Alterada', glucosa) if glucosa< 125 
             else ('Diabetes', glucosa) for glucosa in glicemia]:

Esta línea utiliza una comprensión de lista con operadores condicionales ternarios anidados para 
crear una nueva lista llamada etiquetas. Vamos a desglosarla:

for glucosa in glicemia: Itera a través de cada valor de glucemia en la lista glicemia. En cada 
iteración, la variable glucosa tomará el valor de un nivel de glucemia.

('Hipoglicemia', glucosa) if glucosa<= 70: Si el valor de glucosa es menor o igual a 70, se crea 
una tupla con la etiqueta 'Hipoglicemia' y el valor de glucosa.

else ('Normal', glucosa) if glucosa< 100: Si la condición anterior es falsa (es decir, glucosa es 
mayor que 70), se evalúa esta segunda condición. Si glucosa es menor que 100, se crea una tupla 
con la etiqueta 'Normal' y el valor de glucosa.

else ('Alterada', glucosa) if glucosa< 125: Si las dos condiciones anteriores son falsas 
(es decir, glucosa es 100 o mayor), se evalúa esta tercera condición. Si glucosa es menor que 125, 
se crea una tupla con la etiqueta 'Alterada' y el valor de glucosa.

else ('Diabetes', glucosa): Si ninguna de las condiciones anteriores es verdadera 
(es decir, glucosa es 125 o mayor), se crea una tupla con la etiqueta 'Diabetes' y el valor de 
glucosa.

[...] for glucosa in glicemia: La estructura completa de la comprensión de lista significa: 

"Crea una nueva lista donde cada elemento es una tupla que contiene una etiqueta 
(basada en el valor de glucosa según las condiciones) y el valor de glucosa correspondiente, 
para cada valor de glucosa en la lista glicemia".

print(etiquetas):

Finalmente, esta línea imprime el contenido de la lista etiquetas en la consola.
En resumen:

El código toma una lista de niveles de glucemia y crea una nueva lista llamada etiquetas. 

Para cada nivel de glucemia, se evalúan una serie de condiciones para asignarle una etiqueta 
categórica ('Hipoglicemia', 'Normal', 'Alterada' o 'Diabetes') según los rangos definidos. La nueva 
lista etiquetas contiene tuplas, donde cada tupla asocia la etiqueta correspondiente con el valor de 
glucemia original.

Resultado de la ejecución:

Dado el contenido de la lista glicemia, la salida del código será la siguiente lista de tuplas:

[('Diabetes', 129), ('Normal', 82), ('Hipoglicemia', 60), ('Normal', 97), ('Alterada', 101), 
('Hipoglicemia', 65), ('Hipoglicemia', 62), ('Diabetes', 167), ('Normal', 87), ('Hipoglicemia', 53), 
('Hipoglicemia', 58), ('Normal', 92), ('Hipoglicemia', 66), ('Alterada', 120), ('Alterada', 109), 
('Hipoglicemia', 62), ('Normal', 86), ('Normal', 96), ('Alterada', 103), ('Normal', 88), 
('Diabetes', 155), ('Hipoglicemia', 52), ('Normal', 89), ('Normal', 73)]

Cada tupla en la lista etiquetas indica la categoría de nivel de glucemia y el valor original de 
glucosa.
'''