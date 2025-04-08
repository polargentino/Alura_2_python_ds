'''
6 - Estás trabajando con procesamiento de lenguaje natural (NLP) y, en esta ocasión, tu líder te 
pidió que crees un fragmento de código que reciba una lista con las palabras separadas de una frase 
generada por ChatGPT.

Necesitas crear una función que evalúe cada palabra de este texto y verifique si el tratamiento para 
quitar los símbolos de puntuación (',', '.', '!' y '?') se realizó. De lo contrario, se lanzará una 
excepción del tipo ValueError señalando el primer caso en que se detectó el uso de una puntuación a 
través de la frase "El texto presenta puntuaciones en la palabra "[palabra]"". Esta solicitud se 
centra en el análisis del patrón de frases generadas por la inteligencia artificial.

Datos para probar el código:

Lista tratada:
-------------
lista_tratada = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación', 'poderoso', 'versátil',
                  'y', 'fácil', 'de', 'aprender', 'utilizado', 'en', 'diversos', 'campos', 'desde',
                  'análisis', 'de', 'datos', 'hasta', 'inteligencia', 'artificial']

Lista no tratada:
----------------
lista_no_tratada = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación', 'poderoso,', 'versátil',
                  'y', 'fácil,', 'de', 'aprender', 'utilizado', 'en', 'diversos', 'campos,', 'desde',
                  'análisis', 'de', 'datos', 'hasta', 'inteligencia', 'artificial!']

'''
# 6 - 
# Lista tratada:

# 6 -
# Lista tratada:

lista_tratada = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación', 'poderoso', 'versátil',
                  'y', 'fácil', 'de', 'aprender', 'utilizado', 'en', 'diversos', 'campos', 'desde',
                  'análisis', 'de', 'datos', 'hasta', 'inteligencia', 'artificial']

# Lista no tratada:

lista_no_tratada = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación', 'poderoso,', 'versátil',
                  'y', 'fácil,', 'de', 'aprender', 'utilizado', 'en', 'diversos', 'campos,', 'desde',
                  'análisis', 'de', 'datos', 'hasta', 'inteligencia', 'artificial!']

# Definimos la función:

def evaluar_puntuacion(lista_palabras):
    try:
        for palabra in lista_palabras:
            for puntuacion in [',', '.', '!', '?']:
                if puntuacion in palabra:
                    raise ValueError(f"El texto presenta puntuaciones en la palabra '{palabra}'.")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("El texto no presenta símbolos de puntuación.")

# La probamos con la lista tratada:
print("Evaluando lista tratada:")
evaluar_puntuacion(lista_tratada)

# Y con la lista no tratada:
print("\nEvaluando lista no tratada:")
evaluar_puntuacion(lista_no_tratada)

'''
Evaluando lista tratada:
El texto no presenta símbolos de puntuación.

Evaluando lista no tratada:
Error: El texto presenta puntuaciones en la palabra 'poderoso,'.
                                                                  



Explicación del código:
----------------------
lista_tratada y lista_no_tratada: Se definen dos listas de palabras, una que se supone que ya ha sido 
procesada para eliminar la puntuación y otra que contiene algunos símbolos de puntuación.

def evaluar_puntuacion(lista_palabras):: Se define una función llamada evaluar_puntuacion que toma 
una lista de palabras (lista_palabras) como argumento.

try:: Se inicia un bloque try. El código dentro de este bloque es el que se intentará ejecutar para 
verificar la presencia de puntuación.

for palabra in lista_palabras:: Se itera a través de cada palabra en la lista_palabras.

for puntuacion in [',', '.', '!', '?']:: Para cada palabra, se itera a través de la lista de símbolos 
de puntuación que se deben verificar.

if puntuacion in palabra:: Se verifica si alguno de los símbolos de puntuacion está presente dentro 
de la palabra actual. El operador in devuelve True si la subcadena puntuacion se encuentra dentro 
de la cadena palabra.

raise ValueError(f"El texto presenta puntuaciones en la palabra '{palabra}'."): Si se encuentra un 
símbolo de puntuación en una palabra, se lanza una excepción ValueError con el mensaje especificado, 
indicando la primera palabra donde se detectó la puntuación. Al lanzarse la excepción, la ejecución 
del bloque try se detiene y se pasa al bloque except.

except ValueError as e:: Se define un bloque except para capturar la excepción ValueError que se 
lanza si se encuentra puntuación.

print(f"Error: {e}"): Se imprime el mensaje de error de la excepción, que indica la palabra con 
puntuación.

else:: Se define un bloque else. Este bloque se ejecuta solo si no se lanza ninguna excepción dentro 
del bloque try. Esto significa que se recorrieron todas las palabras de la lista sin encontrar 
ninguno de los símbolos de puntuación especificados.

print("El texto no presenta símbolos de puntuación."): Si no se encuentra puntuación, se imprime 
este mensaje.

Pruebas de la función:
---------------------
evaluar_puntuacion(lista_tratada): Se llama a la función con la lista que se supone que no tiene 
puntuación. En este caso, el bloque try se ejecutará completamente sin lanzar ninguna excepción, 
por lo que se imprimirá el mensaje del bloque else: "El texto no presenta símbolos de puntuación.".

evaluar_puntuacion(lista_no_tratada): Se llama a la función con la lista que contiene puntuación. 
La función iterará a través de las palabras y, cuando llegue a la palabra 'poderoso,', 
la condición ',' in 'poderoso,' será True, lo que provocará que se lance la excepción ValueError 
con el mensaje "El texto presenta puntuaciones en la palabra 'poderoso,'. ". La ejecución saltará 
al bloque except, donde se imprimirá este mensaje de error. La función se detendrá en la primera 
detección de puntuación, cumpliendo con el requisito de señalar el primer caso.

Este código cumple con los requisitos al evaluar cada palabra de la lista y lanzar un ValueError 
en la primera instancia en que se detecta uno de los símbolos de puntuación especificados. 

También proporciona una salida clara para los casos con y sin puntuación.
'''