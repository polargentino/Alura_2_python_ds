'''
6 - Para cumplir con una demanda de una institución educativa para el análisis del rendimiento de 
sus estudiantes, necesitas crear una función que reciba una lista de 4 notas y devuelva:
'''

def analisis_notas(notas):
    mayor = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas)
    situacion = "Aprobado" if media >= 6 else "Reprobado"
    return mayor, menor, media, situacion


# Uso de la función
notas_estudiante = [float(input(f"Ingrese la nota {i + 1}: ")) for i in range(4)]
resultado = analisis_notas(notas_estudiante)
print(f"El estudiante obtuvo una media de {resultado[2]:.2f}, con la mayor nota de {resultado[0]:.2f} puntos y la menor nota de {resultado[1]:.2f} puntos y fue {resultado[3]}")

'''
Ingrese la nota 1: 8
Ingrese la nota 2: 9
Ingrese la nota 3: 6
Ingrese la nota 4: 5
El estudiante obtuvo una media de 7.00, con la mayor nota de 9.00 puntos y la menor nota 
de 5.00 puntos y fue Aprobado


Claro, vamos a desglosar este código Python paso a paso para entender qué hace:

1. Definición de la función analisis_notas(notas):
------------------------------------------------
def analisis_notas(notas):: Define una función llamada analisis_notas que toma una lista de notas 
como argumento.

mayor = max(notas): Utiliza la función max() para encontrar la nota más alta dentro de la lista 
notas y la almacena en la variable mayor.

menor = min(notas): Utiliza la función min() para encontrar la nota más baja dentro de la lista 
notas y la almacena en la variable menor.

media = sum(notas) / len(notas): Calcula la media (promedio) de las notas.

sum(notas): Suma todos los elementos de la lista notas.

len(notas): Obtiene la cantidad de elementos (notas) en la lista.

El resultado de la división se almacena en la variable media.

situacion = "Aprobado" if media >= 6 else "Reprobado": Determina la situación del estudiante 
basándose en la media.

Si la media es mayor o igual a 6, la variable situacion se establece en la cadena "Aprobado".

En caso contrario (si la media es menor que 6), la variable situacion se establece en la cadena 
"Reprobado". Esto es un ejemplo de un operador condicional ternario.

return mayor, menor, media, situacion: La función devuelve una tupla conteniendo la nota más alta, 
la nota más baja, la media y la situación del estudiante.

2. Uso de la función:
--------------------
notas_estudiante = [float(input(f"Ingrese la nota {i + 1}: ")) for i in range(4)]: Esta línea 
utiliza una comprensión de lista para solicitar al usuario que ingrese 4 notas y las almacena en 
una lista llamada notas_estudiante.

for i in range(4): Itera 4 veces, con i tomando valores de 0 a 3.

input(f"Ingrese la nota {i + 1}: "): Muestra un mensaje en la consola solicitando al usuario que 
ingrese cada nota (Nota 1, Nota 2, Nota 3, Nota 4).

float(...): Convierte la entrada del usuario (que es una cadena de texto) a un número decimal (float).
[...]: Crea una lista con las 4 notas ingresadas por el usuario.

resultado = analisis_notas(notas_estudiante): Se llama a la función analisis_notas con la lista 
notas_estudiante como argumento. El valor de retorno (la tupla con la mayor nota, la menor nota, 
la media y la situación) se almacena en la variable resultado.

print(f"El estudiante obtuvo una media de {resultado[2]:.2f}, con la mayor nota de {resultado[0]:.2f} 
puntos y la menor nota de {resultado[1]:.2f} puntos y fue {resultado[3]}"): Finalmente, esta línea 
imprime un mensaje en la consola con los resultados del análisis.

f"...": Es una cadena f, que permite insertar variables directamente dentro de la cadena de texto.
{resultado[2]:.2f}: Accede al tercer elemento de la tupla resultado (la media) y la formatea para 
mostrarla con 2 decimales.

{resultado[0]:.2f}: Accede al primer elemento de la tupla resultado (la mayor nota) y la formatea 
para mostrarla con 2 decimales.

{resultado[1]:.2f}: Accede al segundo elemento de la tupla resultado (la menor nota) y la formatea 
para mostrarla con 2 decimales.

{resultado[3]}: Accede al cuarto elemento de la tupla resultado (la situación del estudiante).

En resumen:

El código define una función que toma una lista de notas, calcula la nota más alta, la nota más baja, 
la media y determina si el estudiante está aprobado o reprobado (considerando una media de 6 o 
superior como aprobado). Luego, solicita al usuario que ingrese 4 notas, llama a la función para 
analizarlas e imprime un resumen de los resultados.

Ejemplo de ejecución:

Si el usuario ingresa las notas 7.5, 5.0, 8.0 y 6.5, la salida podría ser:

El estudiante obtuvo una media de 6.75, con la mayor nota de 8.00 puntos y la menor nota de 5.00 
puntos y fue Aprobado
'''
