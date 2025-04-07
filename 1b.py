'''
3 - Crea un programa que lea la siguiente lista de números y elija uno al azar.
'''
import random

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
numero_aleatorio = random.choice(lista) # para seleccionar un número al azar de esa lista.
print(numero_aleatorio)
