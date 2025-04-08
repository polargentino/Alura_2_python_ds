'''
3 - Crea una función que reciba una lista como parámetro y convierta todos los valores de la 
lista a flotantes. La función debe incluir un manejo de error indicando el tipo de error generado y 
devolver la lista si no ha ocurrido ningún error. Por último, debe tener la cláusula finally para 
imprimir el texto: 'Fin de la ejecución de la función'.
'''
# 3 -



def convertir_a_float(lista):
    try:
        nueva_lista = [float(valor) for valor in lista]
        return nueva_lista
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Fin de la ejecución de la función")

       # Ejemplo de uso:
lista_original = ['4.5', '2.3', '7.8', '1.2']
lista_convertida = convertir_a_float(lista_original)
print(lista_convertida)
 
'''
Fin de la ejecución de la función
[4.5, 2.3, 7.8, 1.2]
'''

#--------------------------------------------------------------------------------------

# 3 -

def convertir_a_float(lista):
    try:
        nueva_lista = [float(valor) for valor in lista]
        return nueva_lista
    except ValueError as e:
        print(f"Error: No se pudieron convertir todos los elementos a float. Error específico: {e}")
        return None  # Es buena práctica devolver algo para indicar el fallo
    finally:
        print("Fin de la ejecución de la función")

# Ejemplo de uso:
lista_original_correcta = ['4.5', '2.3', '7.8', '1.2']
lista_convertida_correcta = convertir_a_float(lista_original_correcta)
print(f"Lista convertida (correcta): {lista_convertida_correcta}")

lista_original_incorrecta = ['4.5', 'texto', '7.8', '1.2']
lista_convertida_incorrecta = convertir_a_float(lista_original_incorrecta)
print(f"Lista convertida (incorrecta): {lista_convertida_incorrecta}")

lista_original_mixta = [1, '2.5', 3.0, 'cuatro']
lista_convertida_mixta = convertir_a_float(lista_original_mixta)
print(f"Lista convertida (mixta): {lista_convertida_mixta}")

'''
Fin de la ejecución de la función
Lista convertida (correcta): [4.5, 2.3, 7.8, 1.2]

Error: No se pudieron convertir todos los elementos a float. Error específico: could not convert 
string to float: 'texto'

Fin de la ejecución de la función
Lista convertida (incorrecta): None

Error: No se pudieron convertir todos los elementos a float. Error específico: could not convert 
string to float: 'cuatro'

Fin de la ejecución de la función
Lista convertida (mixta): None



Explicación del código:
----------------------
def convertir_a_float(lista):: Define una función llamada convertir_a_float que toma una lista como 
argumento.

try:: Inicia un bloque try. El código dentro de este bloque es el que se intentará ejecutar.

nueva_lista = [float(valor) for valor in lista]: Utiliza una comprensión de lista para iterar a 
través de cada valor en la lista proporcionada y trata de convertir cada valor a un número de punto 
flotante (float()). Los resultados se almacenan en una nueva lista llamada nueva_lista. Si algún 
valor en la lista no puede ser convertido a float (por ejemplo, una cadena de texto que no representa 
un número), se generará una excepción ValueError.

return nueva_lista: Si la conversión de todos los elementos a float se realiza con éxito 
(sin errores), la función devuelve la nueva_lista con los valores convertidos.

except ValueError as e:: Define un bloque except específico para capturar la excepción ValueError. 
Este bloque se ejecutará si ocurre un ValueError dentro del bloque try (es decir, si algún elemento 
de la lista no pudo ser convertido a float).

print(f"Error: No se pudieron convertir todos los elementos a float. Error específico: {e}"): 
Imprime un mensaje de error indicando que la conversión falló y muestra el mensaje de error 
específico proporcionado por la excepción ValueError (almacenado en la variable e).

return None: En caso de error, es una buena práctica que la función devuelva un valor que indique el 
fallo. None es una opción común para esto.

finally:: Define una cláusula finally. El código dentro de este bloque siempre se ejecutará, 
independientemente de si ocurrió una excepción en el bloque try o no.

print("Fin de la ejecución de la función"): Imprime el texto "Fin de la ejecución de la función" al 
final de la ejecución de la función, tanto si la conversión fue exitosa como si ocurrió un error.

Ejemplos de uso:

lista_original_correcta = ['4.5', '2.3', '7.8', '1.2']: Una lista de cadenas que pueden ser 
convertidas a float. La función devolverá [4.5, 2.3, 7.8, 1.2] y luego imprimirá "Fin de la ejecución 
de la función".

lista_original_incorrecta = ['4.5', 'texto', '7.8', '1.2']: Una lista que contiene una cadena que 
no puede ser convertida a float. La función capturará el ValueError, imprimirá el mensaje de error, 
devolverá None, y luego imprimirá "Fin de la ejecución de la función".

lista_original_mixta = [1, '2.5', 3.0, 'cuatro']: Otra lista con un tipo de dato que no se puede 
convertir directamente a float como cadena. La función se comportará de manera similar al caso 
anterior, capturando el ValueError, imprimiendo el error, devolviendo None, y finalmente 
imprimiendo el mensaje.

Este código cumple con los requisitos al intentar convertir todos los valores de la lista a 
flotantes, incluir un manejo de errores específico para ValueError, devolver la lista convertida si 
no hay errores y siempre ejecutar la cláusula finally para imprimir el mensaje indicado. 
La modificación incluye un return None en el bloque except para indicar explícitamente que la 
conversión falló.
'''