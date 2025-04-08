'''
5 - Como desafío, se te ha asignado la tarea de desarrollar un código que contabiliza las 
puntuaciones de estudiantes de una institución educativa de acuerdo con sus respuestas en una prueba. 
Este código debe ser probado para un ejemplo de 3 estudiantes con una lista de listas en la que cada 
lista tiene las respuestas de 5 preguntas objetivas de cada estudiante. Cada pregunta vale un punto 
y las alternativas posibles son A, B, C o D.

Si alguna alternativa en una de las pruebas no está entre las alternativas posibles, debes lanzar 
un ValueError con el mensaje "La alternativa [alternativa] no es una opción de alternativa válida". 
El cálculo de las 3 notas solo se realizará mediante las entradas con las alternativas A, B, C o D 
en todas las pruebas. Si no se lanza la excepción, se mostrará una lista con las notas en cada prueba.

Datos para la prueba del código:

Respuestas de la prueba:

respuestas = ['D', 'A', 'B', 'C', 'A']

A continuación, hay 2 listas de listas que puedes usar como prueba:

Notas sin excepción:

tests_sin_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]

Notas con excepción:

tests_con_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]
'''
# 5 - Datos para la prueba del código:

# Respuesta de la prueba:

respuesta = ['D', 'A', 'B', 'C', 'A']

# A continuación, hay 2 listas de listas que puedes usar como prueba:

# Notas sin excepción:

tests_sin_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]

# Notas con excepción:

tests_con_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

def corrector(tests: list):
  puntuaciones = [] 
  try:
    for test in tests:
      nota = 0 
      for i in range(len(test)):
        if test[i] not in ['A', 'B', 'C', 'D']:
          raise ValueError(f'La alternativa {test[i]} no es una opción de alternativa válida')
        elif test[i] == respuesta[i]: 
          nota += 1
      puntuaciones.append(nota) 
  except Exception as e:
    print(e)
  else:
    return puntuaciones 



# Y se procede a probar la función con excepción:

corrector(tests_con_ex)

# Y sin excepción:

corrector(tests_sin_ex)

'''
La alternativa E no es una opción de alternativa válida
'''

#---------------------------------------------------------------------------------------------

# 5 - Datos para la prueba del código:

# Respuesta de la prueba:

respuesta = ['D', 'A', 'B', 'C', 'A']

# A continuación, hay 2 listas de listas que puedes usar como prueba:

# Notas sin excepción:

tests_sin_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]

# Notas con excepción:

tests_con_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

def corrector(tests: list):
  puntuaciones = []
  try:
    for test in tests:
      nota = 0
      for i in range(len(test)):
        if test[i] not in ['A', 'B', 'C', 'D']:
          raise ValueError(f'La alternativa {test[i]} no es una opción de alternativa válida')
        elif test[i] == respuesta[i]:
          nota += 1
      puntuaciones.append(nota)
  except ValueError as e:
    print(e)
  else:
    return puntuaciones

# Y se procede a probar la función con excepción:

print("Prueba con notas con excepción:")
resultado_con_ex = corrector(tests_con_ex)
if resultado_con_ex is not None:
    print(f"Puntuaciones (con excepción): {resultado_con_ex}")

# Y sin excepción:

print("\nPrueba con notas sin excepción:")
resultado_sin_ex = corrector(tests_sin_ex)
if resultado_sin_ex is not None:
    print(f"Puntuaciones (sin excepción): {resultado_sin_ex}")

'''
Prueba con notas con excepción:
La alternativa E no es una opción de alternativa válida

Prueba con notas sin excepción:
Puntuaciones (sin excepción): [5, 3, 3]



Explicación del código:
----------------------
respuesta = ['D', 'A', 'B', 'C', 'A']: Se define una lista llamada respuesta que contiene las 
respuestas correctas para las 5 preguntas de la prueba.

tests_sin_ex = [...]: Se define una lista de listas llamada tests_sin_ex. Cada lista interna 
representa las respuestas de un estudiante, y todas las alternativas son válidas 
('A', 'B', 'C', o 'D').

tests_con_ex = [...]: Se define otra lista de listas llamada tests_con_ex. En la respuesta del 
segundo estudiante, hay una alternativa inválida ('E').

def corrector(tests: list):: Define una función llamada corrector que toma una lista de listas tests 
como argumento. Se espera que cada lista interna represente las respuestas de un estudiante.

puntuaciones = []: Se inicializa una lista vacía llamada puntuaciones. Esta lista se utilizará 
para almacenar la puntuación de cada estudiante.

try:: Se inicia un bloque try. El código dentro de este bloque es el que se intentará ejecutar y 
donde podría ocurrir la excepción ValueError.

for test in tests:: Se itera a través de cada lista test dentro de la lista tests (es decir, a través 
de las respuestas de cada estudiante).

nota = 0: Para cada estudiante, se inicializa una variable nota en 0.

for i in range(len(test)):: Se itera a través de las respuestas de cada pregunta para el estudiante 
actual (utilizando el índice i).

if test[i] not in ['A', 'B', 'C', 'D']:: Se verifica si la respuesta del estudiante para la pregunta 
actual (test[i]) no está dentro de las alternativas válidas ('A', 'B', 'C', 'D').

raise ValueError(f'La alternativa {test[i]} no es una opción de alternativa válida'): Si se encuentra 
una alternativa inválida, se lanza explícitamente una excepción ValueError con un mensaje 
informativo que incluye la alternativa incorrecta. Si esta excepción se lanza, el resto del 
bloque try se omitirá y se pasará al bloque except.

elif test[i] == respuesta[i]:: Si la alternativa es válida, se compara con la respuesta correcta 
para la misma pregunta (respuesta[i]).

nota += 1: Si la respuesta del estudiante coincide con la respuesta correcta, se incrementa la nota 
del estudiante.

puntuaciones.append(nota): Después de revisar todas las respuestas de un estudiante, se añade la 
nota del estudiante a la lista puntuaciones.

except ValueError as e:: Se define un bloque except específico para capturar la excepción ValueError 
que se lanza si se encuentra una alternativa inválida.

print(e): Se imprime el mensaje de error de la excepción ValueError.

else:: Se define un bloque else. Este bloque se ejecutará solo si no se lanza ninguna excepción 
dentro del bloque try.

return puntuaciones: Si todas las alternativas en todas las pruebas son válidas, la función devuelve 
la lista puntuaciones con las notas de cada estudiante.

Prueba con tests_con_ex: Se llama a la función corrector con la lista de pruebas que contiene una 
alternativa inválida. Esto provocará que se lance la excepción ValueError y se imprima el mensaje 
de error. El bloque else no se ejecutará y la función devolverá None implícitamente.

Prueba con tests_sin_ex: Se llama a la función corrector con la lista de pruebas que solo contiene 
alternativas válidas. La función calculará las puntuaciones de cada estudiante y devolverá la lista 
de puntuaciones, que luego se imprimirá.

Este código cumple con todos los requisitos del desafío: contabiliza las puntuaciones, lanza un 
ValueError si encuentra una alternativa inválida, y muestra las notas solo si no se lanza la 
excepción. La salida muestra claramente el error cuando hay una alternativa inválida y las 
puntuaciones cuando todas las alternativas son válidas.
'''