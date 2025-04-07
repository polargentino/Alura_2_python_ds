'''
3 - Crea una función que lea la siguiente lista y devuelva una nueva lista con los 
múltiplos de 3:
'''
def multiplos_de_tres(lista):
    return [num for num in lista if num % 3 == 0]

# Uso de la función
lista_original = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
mult_3 = multiplos_de_tres(lista_original)
print(mult_3)

'''
[24, 99]

Claro, vamos a desglosar este código Python paso a paso para entender qué hace:

1. Definición de la función multiplos_de_tres(lista):

def multiplos_de_tres(lista):: Esto define una función llamada multiplos_de_tres que toma una 
lista como argumento.

return [num for num in lista if num % 3 == 0]: Esta es una comprensión de lista que hace lo 
siguiente:
Itera a través de cada número (num) en la lista proporcionada.
Verifica si el número es divisible por 3 usando el operador módulo (%). Si el resto de la 
división es 0, significa que el número es múltiplo de 3.
Crea una nueva lista que contiene solo los números que son múltiplos de 3.
return devuelve la lista de multiplos de 3.

2. Uso de la función:

lista_original = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]: Aquí, se crea una lista llamada 
lista_original que contiene números enteros.

mult_3 = multiplos_de_tres(lista_original): Se llama a la función multiplos_de_tres con la lista 
lista_original como argumento. El resultado (la lista de múltiplos de 3) se almacena en la variable 
mult_3.

print(mult_3): Finalmente, se imprime la lista mult_3 en la consola.
En resumen:

La función multiplos_de_tres toma una lista de números y devuelve una nueva lista que contiene 
solo los números que son múltiplos de 3.

El código crea una lista de números y luego usa la función para encontrar los múltiplos de 3 en 
esa lista.
El resultado se imprime en la consola.

Resultado de la ejecución:

La salida del código será:

[24, 99]
Esto se debe a que 24 y 99 son los únicos números en la lista original que son múltiplos de 3.

Regla de divisibilidad del 3:

Existe una regla simple para determinar si un número es múltiplo de 3: si la suma de sus 
dígitos es un múltiplo de 3, entonces el número original también es un múltiplo de 3.

Para 24: 2 + 4 = 6, y 6 es múltiplo de 3.
Para 99: 9 + 9 = 18 y 1 + 8 = 9, y 9 es multiplo de 3.

'''