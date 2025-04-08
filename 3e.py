'''
6 - Una tienda tiene una base de datos con la información de venta de cada representante y de cada 
año y necesita filtrar solo los datos del año 2022 con ventas mayores a 6000. La tienda proporcionó 
una muestra con solo las columnas de los años y los valores de venta para que puedas ayudar a 
realizar la filtración de los datos a través de un código:

ventas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]

Crea una lista usando la comprensión de listas para filtrar los valores de 2022 que sean mayores a 
6000.

'''

# 6-
ventas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), 
          ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), 
          ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), 
          ('2022', 5616)]


filtro = [tupla[1] for tupla in ventas if tupla[0] == '2022' and tupla[1] > 6000]
print(filtro)

'''
[8883, 7688, 9544, 8190]


¡Entendido! Vamos a analizar este código Python paso a paso:

ventas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), 
('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), 
('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]:

Se crea una lista llamada ventas. Esta lista contiene tuplas, donde cada tupla representa una venta.

El primer elemento de cada tupla es el año de la venta (string).

El segundo elemento de cada tupla es el monto de la venta (entero).

filtro = [tupla[1] for tupla in ventas if tupla[0] == '2022' and tupla[1] > 6000]:

Esta línea utiliza una comprensión de lista para crear una nueva lista llamada filtro. Vamos a 
desglosarla:

for tupla in ventas: Itera a través de cada tupla en la lista ventas. En cada iteración, la variable 
tupla tomará el valor de una de las tuplas de la lista ventas.

if tupla[0] == '2022' and tupla[1] > 6000: Esta es una condición que se evalúa para cada tupla.

tupla[0] == '2022': Verifica si el primer elemento de la tupla (el año) es igual a la cadena '2022'.

tupla[1] > 6000: Verifica si el segundo elemento de la tupla (el monto de la venta) es mayor que 6000.

and: Ambos lados de la condición deben ser verdaderos para que la condición completa sea verdadera. 
Es decir, la tupla debe representar una venta del año 2022 y el monto de la venta debe ser mayor 
que 6000.

tupla[1]: Si la condición del if es verdadera (la venta es de 2022 y el monto es mayor que 6000), 
entonces se accede al segundo elemento de esa tupla, que es el monto de la venta.

[... for ... if ...]: La estructura completa de la comprensión de lista significa: "Crea una nueva 
lista conteniendo el valor de tupla[1] para cada tupla en ventas, siempre y cuando la tupla cumpla 
con la condición especificada en el if".

print(filtro):

Finalmente, esta línea imprime el contenido de la lista filtro en la consola.

En resumen:

El código itera a través de la lista ventas. Para cada venta (representada por una tupla), 
verifica si la venta ocurrió en el año 2022 y si el monto de la venta fue mayor que 6000. Si ambas 
condiciones se cumplen, el monto de esa venta se agrega a la nueva lista llamada filtro. Al final, 
se imprime la lista de los montos de las ventas del año 2022 que fueron superiores a 6000.

Resultado de la ejecución:

Dado el contenido de la lista ventas, el código producirá la siguiente salida:

[8883, 7688, 9544, 8190]

Esto se debe a que las tuplas en la lista ventas que cumplen ambas condiciones 
(año '2022' y monto > 6000) son:

('2022', 8883)
('2022', 7688)
('2022', 9544)
('2022', 8190)

Y el código ha extraído el segundo elemento (el monto) de cada una de ellas para formar la lista 
filtro.
'''