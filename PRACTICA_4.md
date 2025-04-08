### Curso de Python para Data Science: trabajar con funciones, estructuras de datos y excepciones

## Realice este curso para Data Science y:
Entiende las funciones de las bibliotecas y paquetes en el lenguaje Python.
Conoce las funciones integradas (built-in functions) y sus utilidades.
Crea funciones personalizadas.
Trabaja con estructuras de datos compuestas y anidadas.
Construye listas y diccionarios siguiendo patrones mediante list y dict comprehension.
Aprende a manejar los tipos de errores y excepciones en códigos Python.
Maneja errores y comportamientos indeseados en tu código.

# 
Desafío: hora de practicar
 Siguiente pregunta

Vamos practicar lo que hemos aprendido hasta ahora resolviendo los problemas propuestos en código.

Calentamiento

1 - Haz un programa que solicite a la persona usuaria ingresar dos números decimales y calcular la división entre estos números. El código debe incluir un manejo de error, indicando el tipo de error que se generó si la división no es posible.

Prueba el programa con el segundo valor numérico de la entrada igual a 0. También prueba usando caracteres textuales en la entrada para verificar los tipos de errores que ocurren.

2 - Haz un programa que solicite a la persona usuaria ingresar un texto que será una clave a buscar en el siguiente diccionario: edades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}, almacenando el resultado del valor en una variable. El código debe incluir un manejo de error KeyError, imprimiendo la información 'Nombre no encontrado' en caso de error, e imprimir el valor si no ocurre ninguno.

Prueba el programa con un nombre presente en una de las claves del diccionario y con uno que no esté en el diccionario para verificar el mensaje de error.

3 - Crea una función que reciba una lista como parámetro y convierta todos los valores de la lista a flotantes. La función debe incluir un manejo de error indicando el tipo de error generado y devolver la lista si no ha ocurrido ningún error. Por último, debe tener la cláusula finally para imprimir el texto: 'Fin de la ejecución de la función'.

4 - Crea una función que reciba dos listas como parámetros y agrupe los elementos uno a uno de las listas, formando una lista de tuplas de 3 elementos. El primer y segundo elemento de la tupla son los valores en la posición i de las listas y el tercer elemento es la suma de los valores en la posición i de las listas.

La función debe incluir un manejo de error indicando el tipo de error generado y devolver como resultado la lista de tuplas. Si las listas enviadas como parámetro tienen tamaños diferentes, la función debe devolver un IndexError con la frase: 'La cantidad de elementos en cada lista es diferente.'.

Datos para probar la función:

Valores sin error:

lista1 = [4, 6, 7, 9, 10]
lista2 = [-4, 6, 8, 7, 9]
Copia el código
Listas con tamaños diferentes:

lista1 = [4, 6, 7, 9, 10, 4]
lista2 = [-4, 6, 8, 7, 9]
Copia el código
Listas con valores incoherentes:

lista1 = [4, 6, 7, 9, 'A']
lista2 = [-4, 'E', 8, 7, 9]
Copia el código
Aplicando a proyectos

5 - Como desafío, se te ha asignado la tarea de desarrollar un código que contabiliza las puntuaciones de estudiantes de una institución educativa de acuerdo con sus respuestas en una prueba. Este código debe ser probado para un ejemplo de 3 estudiantes con una lista de listas en la que cada lista tiene las respuestas de 5 preguntas objetivas de cada estudiante. Cada pregunta vale un punto y las alternativas posibles son A, B, C o D.

Si alguna alternativa en una de las pruebas no está entre las alternativas posibles, debes lanzar un ValueError con el mensaje "La alternativa [alternativa] no es una opción de alternativa válida". El cálculo de las 3 notas solo se realizará mediante las entradas con las alternativas A, B, C o D en todas las pruebas. Si no se lanza la excepción, se mostrará una lista con las notas en cada prueba.

Datos para la prueba del código:

Respuestas de la prueba:

respuestas = ['D', 'A', 'B', 'C', 'A']
Copia el código
A continuación, hay 2 listas de listas que puedes usar como prueba:

Notas sin excepción:

tests_sin_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
Copia el código
Notas con excepción:

tests_con_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

Copia el código

6 - Estás trabajando con procesamiento de lenguaje natural (NLP) y, en esta ocasión, tu líder te pidió que crees un fragmento de código que reciba una lista con las palabras separadas de una frase generada por ChatGPT.

Necesitas crear una función que evalúe cada palabra de este texto y verifique si el tratamiento para quitar los símbolos de puntuación (',', '.', '!' y '?') se realizó. De lo contrario, se lanzará una excepción del tipo ValueError señalando el primer caso en que se detectó el uso de una puntuación a través de la frase "El texto presenta puntuaciones en la palabra "[palabra]"". Esta solicitud se centra en el análisis del patrón de frases generadas por la inteligencia artificial.

Datos para probar el código:

Lista tratada:

lista_tratada = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación', 'poderoso', 'versátil',
                  'y', 'fácil', 'de', 'aprender', 'utilizado', 'en', 'diversos', 'campos', 'desde',
                  'análisis', 'de', 'datos', 'hasta', 'inteligencia', 'artificial']
Copia el código
Lista no tratada:

lista_no_tratada = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación', 'poderoso,', 'versátil',
                  'y', 'fácil,', 'de', 'aprender', 'utilizado', 'en', 'diversos', 'campos,', 'desde',
                  'análisis', 'de', 'datos', 'hasta', 'inteligencia', 'artificial!']
Copia el código
Ver opinión del instructor

### Opinión del instructor
--------------------------

A continuación te presentamos las posibles respuestas al desafío propuesto:

1 -

try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 / num2
    print("El resultado de la división es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError as e:
    print(f"Error: {e}")

Copia el código

2 -

try:
    nombre = input("Ingrese un nombre para buscar en el diccionario: ")
    edad = edades[nombre]
    print(f"La edad de {nombre} es {edad} años.")
except KeyError:
    print("Error: Nombre no encontrado.")

Copia el código

3 -

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

Copia el código

4 - Datos para probar la función:

Valores sin error:

lista1 = [4, 6, 7, 9, 10]
lista2 = [-4, 6, 8, 7, 9]
Copia el código
Listas con tamaños diferentes:

lista1 = [4, 6, 7, 9, 10, 4]
lista2 = [-4, 6, 8, 7, 9]
Copia el código
Listas con valores incoherentes:

lista1 = [4, 6, 7, 9, 'A']
lista2 = [-4, 'E', 8, 7, 9]

Copia el código

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

Copia el código

5 - Datos para la prueba del código:

Respuesta de la prueba:

respuesta = ['D', 'A', 'B', 'C', 'A']
Copia el código
A continuación, hay 2 listas de listas que puedes usar como prueba:

Notas sin excepción:

tests_sin_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
Copia el código
Notas con excepción:

tests_con_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]
Copia el código
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

Copia el código

Y se procede a probar la función con excepción:

corrector(tests_con_ex)
Copia el código
Y sin excepción:

corrector(tests_sin_ex)

Copia el código

6 - Lista tratada:

lista_tratada = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación', 'poderoso', 'versátil',
                  'y', 'fácil', 'de', 'aprender', 'utilizado', 'en', 'diversos', 'campos', 'desde',
                  'análisis', 'de', 'datos', 'hasta', 'inteligencia', 'artificial']
Copia el código
Lista no tratada:

lista_no_tratada = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación', 'poderoso,', 'versátil',
                  'y', 'fácil,', 'de', 'aprender', 'utilizado', 'en', 'diversos', 'campos,', 'desde',
                  'análisis', 'de', 'datos', 'hasta', 'inteligencia', 'artificial!']
Copia el código
Definimos la función:

def evaluar_puntuacion(lista_palabras):
    try:
        for palabra in lista_palabras:
            if any(puntuacion in palabra for puntuacion in [',', '.', '!', '?']):
                raise ValueError(f"El texto presenta puntuaciones en la palabra '{palabra}'.")
    except ValueError as e:
        print(f"Error: {e}")
Copia el código
La probamos con la lista tratada:

evaluar_puntuacion(lista_tratada)
Copia el código
Y con la lista no tratada:

evaluar_puntuacion(lista_no_tratada)
Copia el código
7 - Función de división de columnas y manejo de excepciones:

# Creando la función que recibe las dos listas y la operación a realizar
def divide_columnas(lista_1: list, lista_2: list) -> list:
  # try-except que verifica si es posible calcular la división y lanza una excepción si las listas tienen tamaños diferentes
  # o si hay alguna división por cero en uno de los cálculos entre los números de las listas
  try:
    if len(lista_1) != len(lista_2):  # Verificando si las listas tienen el mismo tamaño, si no, lanza una excepción
      raise ValueError("Las listas deben tener el mismo tamaño")

    # La función zip empareja los elementos de las listas y se genera una lista mediante la división entre las parejas
    resultado = [round(a / b, 2) for a, b in zip(lista_1, lista_2)]
  except ValueError as e:
    print(e)
  except ZeroDivisionError as e:
    print(f"{e}: La 2ª lista no puede tener un valor igual a 0")
  else:
    return resultado
Copia el código
Probando sin excepciones:

# Probando en el ejemplo que no lanza excepciones
presiones = [100, 120, 140, 160, 180]
temperaturas = [20, 25, 30, 35, 40]

divide_columnas(presiones, temperaturas)
Copia el código
Salida:

[5.0, 4.8, 4.67, 4.57, 4.5]
Copia el código
Probando con excepción (Caso 1):

# Probando en el ejemplo que lanza una excepción (ZeroDivisionError)
presiones = [60, 120, 140, 160, 180]
temperaturas = [0, 25, 30, 35, 40]

divide_columnas(presiones, temperaturas)
Copia el código
Salida:

division by zero: La 2ª lista no puede tener un valor igual a 0
Copia el código
Probando con excepción (Caso 2):

# Probando en el ejemplo que lanza una excepción (ValueError)
presiones = [100, 120, 140, 160]
temperaturas = [20, 25, 30, 35, 40]

divide_columnas(presiones, temperaturas)
Copia el código
Salida:

Las listas deben tener el mismo tamaño