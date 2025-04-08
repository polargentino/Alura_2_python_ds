'''
8 - Un comercio electrónico tiene información de id de venta, cantidad vendida y precio del producto 
divididos en las siguientes listas:

id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cantidad = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
precio = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]


La plataforma necesita estructurar estos datos en una tabla que contenga el valor total de la venta, 
que se obtiene multiplicando la cantidad por el precio unitario. Además, la tabla debe contener un 
encabezado indicando las columnas: 'id', 'cantidad', 'precio' y 'total'.

Crea una lista de tuplas en la que cada tupla tenga id, cantidad, precio y valor total, siendo la 
primera tupla el encabezado de la tabla.
'''


# 8 -
id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cantidad = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
precio = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

tabla = [('id', 'cantidad', 'precio', 'total')]
tabla += [(id[i], cantidad[i], precio[i], cantidad[i]*precio[i]) for i in range(len(id))]

# Imprimir la tabla de forma legible
print("Estructura de Ventas:")
print("{:<4} {:<10} {:<8} {:<10}".format(*tabla[0])) # Imprimir encabezado formateado
print("-" * 32) # Imprimir separador

for fila in tabla[1:]:
    print("{:<4} {:<10} {:<8.2f} {:<10.2f}".format(*fila)) # Imprimir datos formateados

'''
Estructura de Ventas:
id   cantidad   precio   total     
--------------------------------
0    15         93.00    1395.00   
1    12         102.00   1224.00   
2    1          18.00    18.00     
3    15         41.00    615.00    
4    2          122.00   244.00    
5    11         14.00    154.00    
6    2          71.00    142.00    
7    12         48.00    576.00    
8    2          14.00    28.00     
9    4          144.00   576.00




Explicación del código:

id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], cantidad = [...], precio = [...]: Estas líneas definen las tres 
listas con la información de las ventas: el ID de la venta, la cantidad vendida y el precio unitario 
del producto, respectivamente.

tabla = [('id', 'cantidad', 'precio', 'total')]:

Se inicializa una lista llamada tabla.

La primera tupla que se agrega a esta lista es el encabezado de la tabla: ('id', 'cantidad', 
'precio', 'total'). Esto cumple con el requisito de que la primera tupla sea el encabezado.

tabla += [(id[i], cantidad[i], precio[i], cantidad[i]*precio[i]) for i in range(len(id))]:

Esta línea utiliza una comprensión de lista para crear las filas de datos de la tabla y las agrega a 
la lista tabla.

for i in range(len(id)): Itera a través de los índices de la lista id (que tiene la misma longitud 
que cantidad y precio).

(id[i], cantidad[i], precio[i], cantidad[i]*precio[i]): Para cada índice i, se crea una tupla que 
contiene:

El elemento correspondiente de la lista id (id[i]).
El elemento correspondiente de la lista cantidad (cantidad[i]).
El elemento correspondiente de la lista precio (precio[i]).
El valor total de la venta, que se calcula multiplicando la cantidad[i] por el precio[i].

tabla += [...]: El operador += se utiliza para extender la lista tabla agregando todos los elementos 
de la lista de tuplas generada por la comprensión de lista.

print("Estructura de Ventas:"): Imprime un título para la tabla.

print("{:<4} {:<10} {:<8} {:<10}".format(*tabla[0])):

Imprime el encabezado de la tabla.

"{:<4} {:<10} {:<8} {:<10}".format(...): Es una forma de formatear la salida de strings.
{:<4}: Alinea el texto a la izquierda y reserva un espacio de 4 caracteres.
{:<10}: Alinea el texto a la izquierda y reserva un espacio de 10 caracteres.
{:<8}: Alinea el texto a la izquierda y reserva un espacio de 8 caracteres.
{:<10}: Alinea el texto a la izquierda y reserva un espacio de 10 caracteres.

*tabla[0]: Desempaqueta los elementos de la primera tupla de tabla (el encabezado) para que se pasen 
como argumentos individuales a la función format().

print("-" * 32): Imprime una línea de guiones para separar el encabezado de los datos.

for fila in tabla[1:]::

Itera a través de las filas de datos de la tabla, comenzando desde el segundo elemento de la lista 
tabla (índice 1) hasta el final.

print("{:<4} {:<10} {:<8.2f} {:<10.2f}".format(*fila)):

Imprime cada fila de datos formateada de manera similar al encabezado.

{:<8.2f} y {:<10.2f}: Formatean los valores de precio y total para que se muestren como números de 
punto flotante con dos decimales.

*fila: Desempaqueta los elementos de la tupla fila para pasarlos como argumentos individuales a la 
función format().

Este código crea la lista de tuplas tabla tal como se solicitó, con el encabezado en la primera tupla 
y las filas de datos con el ID, la cantidad, el precio y el valor total de cada venta en las tuplas 
siguientes. Además, la sección de impresión formatea la tabla para que sea más fácil de leer en la 
consola.
'''