'''

1 - Haz un programa que solicite a la persona usuaria ingresar dos números decimales y calcular la 
división entre estos números. El código debe incluir un manejo de error, indicando el tipo de error 
que se generó si la división no es posible.

Prueba el programa con el segundo valor numérico de la entrada igual a 0. También prueba usando 
caracteres textuales en la entrada para verificar los tipos de errores que ocurren.

'''
# 1 -

try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 / num2
    print("El resultado de la división es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError as e:
    print(f"Error: {e}")

'''
Ingrese el primer número: 7
Ingrese el segundo número: 8
El resultado de la división es: 0.875
'''

#-----------------------------------------------------------------------------------------

# 1 -

try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 / num2
    print("El resultado de la división es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError as e:
    print(f"Error: Entrada inválida. Debe ingresar números decimales. Error específico: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

'''
Ingrese el primer número: 9
Ingrese el segundo número: 8
El resultado de la división es: 1.125



Explicación del código:
----------------------
try:: Este bloque de código contiene las instrucciones que se intentarán ejecutar. En este caso, 
se solicita al usuario que ingrese dos números, se convierten a tipo float (para permitir decimales) 
y se realiza la división.

num1 = float(input("Ingrese el primer número: ")):

input("Ingrese el primer número: "): Muestra el mensaje al usuario y espera a que ingrese algún texto.

float(...): Intenta convertir la entrada del usuario a un número decimal. Si el usuario ingresa algo 
que no se puede convertir a un número decimal (por ejemplo, letras), esto generará una excepción 
ValueError.

num2 = float(input("Ingrese el segundo número: ")):

Similar a la línea anterior, solicita y trata de convertir el segundo número ingresado por el usuario 
a un decimal. También puede generar un ValueError.

resultado = num1 / num2:

Realiza la división del primer número (num1) entre el segundo número (num2). Si num2 es igual a cero, 
esta operación generará una excepción ZeroDivisionError.

print("El resultado de la división es:", resultado):

Si la división se realiza con éxito (sin errores), se imprime el resultado.

except ZeroDivisionError::

Este bloque se ejecuta si ocurre una excepción de tipo ZeroDivisionError dentro del bloque try. 
Esto sucederá si el usuario ingresa 0 como el segundo número.

print("Error: No se puede dividir por cero."): Muestra un mensaje específico indicando que la 
división por cero no es posible.

except ValueError as e::

Este bloque se ejecuta si ocurre una excepción de tipo ValueError dentro del bloque try. Esto 
sucederá si el usuario ingresa texto u otros caracteres que no se pueden convertir a un número decimal.

print(f"Error: Entrada inválida. Debe ingresar números decimales. Error específico: {e}"): Muestra 
un mensaje de error genérico sobre la entrada inválida y también incluye el mensaje de error 
específico proporcionado por la excepción ValueError (almacenado en la variable e).

except Exception as e::

Este es un bloque de excepción más general que captura cualquier otro tipo de excepción que pueda 
ocurrir dentro del bloque try y que no haya sido capturada por los bloques except anteriores.

print(f"Ocurrió un error inesperado: {e}"): Muestra un mensaje de error genérico junto con el 
mensaje de error específico de la excepción. Esto es útil para detectar errores imprevistos 
durante la ejecución.

Cómo probar el programa:
-----------------------
Segundo valor numérico igual a 0:

Ejecuta el programa.
Ingresa un número para el primer valor (por ejemplo, 10).
Ingresa 0 para el segundo valor.
Deberías ver el mensaje: Error: No se puede dividir por cero.
Usando caracteres textuales en la entrada:

Ejecuta el programa.

Ingresa un valor numérico para el primer número (por ejemplo, 5.5).

Ingresa texto para el segundo número (por ejemplo, abc).

Deberías ver un mensaje de error ValueError similar a: Error: Entrada inválida. Debe ingresar 
números decimales. Error específico: could not convert string to float: 'abc'

Ejecuta el programa nuevamente.

Ingresa texto para el primer número (por ejemplo, xyz).

Ingresa un valor numérico para el segundo número (por ejemplo, 2.0).

Deberías ver un mensaje de error ValueError similar a: Error: Entrada inválida. Debe ingresar 
números decimales. Error específico: could not convert string to float: 'xyz'

Este código cumple con los requisitos al solicitar dos números decimales, calcular su división e 
implementar un manejo de errores específico para la división por cero y los errores de valor al 
intentar convertir la entrada del usuario a números decimales. También incluye un manejo de 
excepciones más general para cubrir otros posibles errores.
'''
