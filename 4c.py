'''
4 - Crea una función que reciba dos listas como parámetros y agrupe los elementos uno a uno de las 
listas, formando una lista de tuplas de 3 elementos. El primer y segundo elemento de la tupla son 
los valores en la posición i de las listas y el tercer elemento es la suma de los valores en la 
posición i de las listas.

La función debe incluir un manejo de error indicando el tipo de error generado y devolver como 
resultado la lista de tuplas. Si las listas enviadas como parámetro tienen tamaños diferentes, 
la función debe devolver un IndexError con la frase: 'La cantidad de elementos en cada lista es 
diferente.'.

Datos para probar la función:

Valores sin error:

lista1 = [4, 6, 7, 9, 10]
lista2 = [-4, 6, 8, 7, 9]


Listas con tamaños diferentes:

lista1 = [4, 6, 7, 9, 10, 4]
lista2 = [-4, 6, 8, 7, 9]

Listas con valores incoherentes:

lista1 = [4, 6, 7, 9, 'A']
lista2 = [-4, 'E', 8, 7, 9]

Aplicando a proyectos
'''

# 4 - Datos para probar la función:

# Valores sin error:

lista1 = [4, 6, 7, 9, 10]
lista2 = [-4, 6, 8, 7, 9]

# Listas con tamaños diferentes:

lista1 = [4, 6, 7, 9, 10, 4]
lista2 = [-4, 6, 8, 7, 9]

# Listas con valores incoherentes:

lista1 = [4, 6, 7, 9, 'A']
lista2 = [-4, 'E', 8, 7, 9]



def agrupar_listas(lista1, lista2):
    try:
        if len(lista1) != len(lista2):
            raise IndexError("La cantidad de elementos en cada lista es diferente.")
        
        lista_resultado = [(lista1[i], lista2[i], lista1[i] + lista2[i]) for i in range(len(lista1))]
        return lista_resultado
    except TypeError as e:
        print(f"Error: {e}")
    except IndexError as e:
        print(f"Error: {e}")

# Ejemplos de uso:
try:
    resultado_sin_error = agrupar_listas([4, 6, 7, 9, 10], [-4, 6, 8, 7, 9])
    print(resultado_sin_error)
    
    resultado_tamanos_diferentes = agrupar_listas([4, 6, 7, 9, 10, 4], [-4, 6, 8, 7, 9])
    print(resultado_tamanos_diferentes)
    
    resultado_valores_incoherentes = agrupar_listas([4, 6, 7, 9, 'A'], [-4, 'E', 8, 7, 9])
    print(resultado_valores_incoherentes)
except Exception as e:
    print(f"Error general: {e}")

'''
[(4, -4, 0), (6, 6, 12), (7, 8, 15), (9, 7, 16), (10, 9, 19)]
Error: La cantidad de elementos en cada lista es diferente.
None
Error: unsupported operand type(s) for +: 'int' and 'str'
None



Explicación del código:
----------------------
Definición de las listas de prueba: Se definen las tres parejas de listas proporcionadas para probar

la función en diferentes escenarios: sin error, con tamaños diferentes y con valores incoherentes.

def agrupar_listas(lista1, lista2):: Define una función llamada agrupar_listas que toma dos listas 
(lista1 y lista2) como parámetros.

try:: Inicia un bloque try. El código dentro de este bloque es el que se intentará ejecutar.

if len(lista1) != len(lista2):: Se verifica si la longitud de las dos listas es diferente.

raise IndexError("La cantidad de elementos en cada lista es diferente."): Si las longitudes son 
diferentes, se lanza explícitamente una excepción IndexError con el mensaje especificado en el 
requisito.

lista_resultado = [(lista1[i], lista2[i], lista1[i] + lista2[i]) for i in range(len(lista1))]: 
Si las longitudes de las listas son iguales, se utiliza una comprensión de lista para crear la 
lista_resultado.

for i in range(len(lista1)): Itera a través de los índices de la lista1 
(que tiene la misma longitud que lista2 en este punto).

(lista1[i], lista2[i], lista1[i] + lista2[i]): Para cada índice i, se crea una tupla de tres 
elementos: el elemento en la posición i de lista1, el elemento en la posición i de lista2, y la suma 
de estos dos elementos.

return lista_resultado: Si la agrupación se realiza con éxito (sin errores), la función devuelve la 
lista_resultado de tuplas.

except TypeError as e:: Define un bloque except específico para capturar la excepción TypeError. 
Esta excepción ocurrirá si se intenta sumar elementos de tipos incompatibles 
(por ejemplo, un número y una cadena).

print(f"Error de tipo: No se pueden sumar elementos de diferentes tipos. Error específico: {e}"): 
Imprime un mensaje de error indicando el problema y el error específico.

return None: Devuelve None para indicar que la operación falló.
except IndexError as e:: Define un bloque except específico para capturar la excepción IndexError. 
Esta excepción ocurrirá si se intenta acceder a un índice fuera del rango de la lista 
(aunque en este código, la IndexError para tamaños diferentes se lanza explícitamente).

print(f"Error de índice: {e}"): Imprime el mensaje de error específico del IndexError.

return None: Devuelve None para indicar que la operación falló.

Ejemplos de uso: Se llama a la función agrupar_listas con cada una de las parejas de listas de 
prueba y se imprime el resultado o el mensaje de error correspondiente. Se han añadido print() 
descriptivos para identificar cada prueba.

Este código cumple con todos los requisitos: agrupa los elementos de las dos listas en tuplas de 
tres elementos (valor de lista1, valor de lista2, suma), maneja el error IndexError para listas de 
diferentes tamaños devolviendo el mensaje específico, y maneja el error TypeError que puede ocurrir 
al intentar sumar valores incoherentes. La función devuelve la lista de tuplas si no hay errores y 
None en caso de error.
'''