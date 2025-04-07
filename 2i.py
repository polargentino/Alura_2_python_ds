'''

10 - Has comenzado una pasantía en una empresa que trabaja con procesamiento de lenguaje natural 
(NLP). Tu líder te solicitó que crees un fragmento de código que reciba una frase escrita por el 
usuario y filtre solo las palabras con un tamaño mayor o igual a 5, mostrándolas en una lista. 
Esta demanda se centra en el análisis del patrón de comportamiento de las personas al escribir 
palabras de esta cantidad de caracteres o más.

Consejo: utiliza las funciones lambda y filter() para filtrar estas palabras. Recordando que la 
función integrada filter() recibe una función (en nuestro caso, una función lambda) y filtra un 
iterable según la función. Para tratar la frase, utiliza replace() para cambiar ',' '.', '!' y '?' 
por espacio.

Utiliza la frase "Aprender Python aquí en Alura es muy bueno" para probar el código.
'''

# 10 - Una posible solución a este punto la encuentras a continuación:

# Solicitando una frase y separándola por espacios. Usando replace para cambiar
# puntuaciones por espacios.
frase = input("Escribe una frase: ")
frase = frase.replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ').split()

# Filtrando la frase en formato de lista, pasando a la lista tamaño
# solo las palabras con 5 o más caracteres e imprimiéndola en pantalla
tamano = list(filter(lambda x: len(x) >= 5, frase))
print(tamano)

'''
Escribe una frase: Aprender Python aquí en Alura es muy bueno
['Aprender', 'Python', 'Alura', 'bueno']


Entendido! Vamos a desglosar este código Python paso a paso para entender cómo procesa una frase 
ingresada por el usuario:

1. Entrada de la frase por el usuario:
-------------------------------------
frase = input("Escribe una frase: "): Solicita al usuario que escriba una frase y la almacena como 
una cadena en la variable frase.

2. Preprocesamiento de la frase:
-------------------------------
frase = frase.replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ').split(): Esta 
línea realiza varias operaciones en la frase ingresada:
.replace(',',' '): Reemplaza todas las comas (,) con espacios ().
.replace('.',' '): Reemplaza todos los puntos (.) con espacios ().
.replace('!',' '): Reemplaza todos los signos de exclamación (!) con espacios ().
.replace('?',' '): Reemplaza todos los signos de interrogación (?) con espacios ().
.split(): Divide la cadena resultante en una lista de palabras, utilizando los espacios como 
delimitadores. Si hay múltiples espacios seguidos, .split() los tratará como un solo delimitador, 
evitando cadenas vacías en la lista resultante.

El resultado de todas estas operaciones (una lista de palabras limpias) se reasigna a la variable 
frase.

3. Filtrado de palabras por tamaño:
----------------------------------
tamano = list(filter(lambda x: len(x) >= 5, frase)): Esta línea utiliza la función filter() junto 
con una función lambda para crear una nueva lista llamada tamano que contiene solo las palabras de 
la lista frase que tienen 5 o más caracteres.

filter(funcion, iterable): Aplica la funcion a cada elemento del iterable y devuelve un iterador 
con los elementos para los cuales la función devuelve True.

lambda x: len(x) >= 5: Esta es una función lambda (función anónima) que toma una palabra x como 
argumento y devuelve True si la longitud de la palabra (len(x)) es mayor o igual a 5, y False en caso contrario.
list(...): Convierte el iterador devuelto por filter() en una lista llamada tamano.

4. Impresión del resultado:
--------------------------
print(tamano): Finalmente, esta línea imprime la lista tamano en la consola, mostrando solo las 
palabras de la frase original que tienen 5 o más caracteres.
En resumen:

El código toma una frase ingresada por el usuario, elimina los signos de puntuación comunes 
(coma, punto, exclamación, interrogación) reemplazándolos con espacios, luego divide la frase en 
una lista de palabras. Finalmente, filtra esta lista para conservar solo las palabras que tienen 
una longitud de 5 o más caracteres y muestra esa lista filtrada en la pantalla.

Ejemplo de ejecución:
---------------------
Si el usuario ingresa la frase:

Hola, ¿cómo estás? Bien. Gracias!
El código realizaría los siguientes pasos:

frase se convierte en: "Hola cómo estás Bien Gracias " (después de los reemplazos).
frase se divide en la lista: ['Hola', 'cómo', 'estás', 'Bien', 'Gracias'].

El filtro lambda x: len(x) >= 5 evalúa cada palabra:
'Hola': len('Hola') es 4 (False)
'cómo': len('cómo') es 5 (True)
'estás': len('estás') es 6 (True)
'Bien': len('Bien') es 4 (False)
'Gracias': len('Gracias') es 7 (True)

La lista tamano se convierte en: ['cómo', 'estás', 'Gracias'].
Finalmente, se imprime: ['cómo', 'estás', 'Gracias'].
'''
