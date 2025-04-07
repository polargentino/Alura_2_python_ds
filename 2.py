'''
1 - Escribe un código que lee la lista siguiente y realiza:
'''

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

# Leer el tamaño de la lista
tam = len(lista)

# Leer el valor máximo y mínimo
mayor = max(lista)
menor = min(lista)

# Calcular la suma de los valores de la lista
soma = sum(lista)

# Mostrar un mensaje al final
print(f"La lista tiene {tam} números, donde el mayor es {mayor} y el menor es {menor}. La suma de los valores es {soma}")

'''
La lista tiene 17 números, donde el mayor es 99 y el menor es 11. La suma de los valores es 743
'''