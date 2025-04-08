'''
2 - Haz un programa que solicite a la persona usuaria ingresar un texto que será una clave a buscar 
en el siguiente diccionario: edades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}, 
almacenando el resultado del valor en una variable. 

El código debe incluir un manejo de error KeyError, imprimiendo la información 'Nombre no encontrado' 
en caso de error, e imprimir el valor si no ocurre ninguno.

Prueba el programa con un nombre presente en una de las claves del diccionario y con uno que no esté 
en el diccionario para verificar el mensaje de error.
'''

# 2 -
edades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}

try:
    nombre = input("Ingrese un nombre para buscar en el diccionario: ")
    edad = edades[nombre]
    print(f"La edad de {nombre} es {edad} años.")
except KeyError:
    print("Error: Nombre no encontrado.")

'''
Ingrese un nombre para buscar en el diccionario: carol
Error: Nombre no encontrado.

Ingrese un nombre para buscar en el diccionario: pol
Error: Nombre no encontrado.

Ingrese un nombre para buscar en el diccionario: Carol
La edad de Carol es 23 años.



Explicación del código:(Gemini 2.0 Flash)
----------------------
edades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}: Se define un diccionario llamado 
edades que almacena nombres como claves y sus respectivas edades como valores.

try:: Se inicia un bloque try. El código dentro de este bloque es el que se intentará ejecutar y 
donde podría ocurrir un error.

nombre = input("Ingrese un nombre para buscar en el diccionario: "): Se le pide al usuario que 
ingrese un nombre y este se almacena en la variable nombre.

edad = edades[nombre]: Se intenta acceder al valor asociado a la clave ingresada por el usuario 
(nombre) en el diccionario edades. Si la clave nombre existe en el diccionario, su valor (la edad) 
se asigna a la variable edad. Si la clave no existe, esta línea generará una excepción KeyError.

print(f"La edad de {nombre} es {edad} años."): Si la clave se encuentra en el diccionario 
(no ocurrió KeyError), se imprime la edad correspondiente al nombre ingresado.

except KeyError:: Se define un bloque except específico para capturar la excepción KeyError. 
Este bloque se ejecutará solo si ocurre una KeyError dentro del bloque try.

print("Error: Nombre no encontrado."): Si se captura una KeyError (lo que significa que el nombre 
ingresado no existe como clave en el diccionario edades), se imprime el mensaje "Error: Nombre no 
encontrado.".

Cómo probar el programa:

Con un nombre presente en el diccionario:

Ejecuta el programa.
Ingresa uno de los nombres que son claves en el diccionario (por ejemplo, Júlia o Carol).
Deberías ver la edad correspondiente a ese nombre impreso en la consola (por ejemplo, "La edad de 
Júlia es 16 años.").
Con un nombre que no está en el diccionario:

Ejecuta el programa.
Ingresa un nombre que no sea una clave en el diccionario (por ejemplo, Pedro o Ana).
Deberías ver el mensaje de error: "Error: Nombre no encontrado.".

El código cumple con los requisitos al solicitar un nombre, intentar buscarlo en el diccionario, 
almacenar el valor en una variable (aunque se imprime directamente), y manejar específicamente el 
error KeyError para informar al usuario si el nombre no se encuentra.
'''