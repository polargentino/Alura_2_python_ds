'''
8 - Para diversificar y atraer nuevos clientes, una lanchonete creó un ítem misterioso en su 
menú llamado "ensalada de frutas sorpresa". En este ítem, se eligen aleatoriamente 3 frutas de 
una lista de 12 para componer la ensalada de frutas del cliente. Crea el código que realice esta 
selección aleatoria según la lista dada.
'''

import random

frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", 
          "fresa", "naranja", "maracuya", "kiwi", "cereza"]
seleccion_frutas = random.sample(frutas, 3) # Sin reemplazo: Cada fruta se selecciona solo una vez.
print("Ensalada de frutas sorpresa:", seleccion_frutas)

'''
La función random.sample() del módulo random en Python se utiliza para seleccionar una 
muestra aleatoria de elementos únicos de una secuencia (como una lista, tupla o conjunto) 
sin reemplazo. Esto significa que cada elemento de la secuencia original puede aparecer como 
máximo una vez en la muestra seleccionada.

Ensalada de frutas sorpresa: ['coco', 'uva', 'manzana']
'''