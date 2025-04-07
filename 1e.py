'''
6 - Se debe escribir un programa para sortear a un seguidor de una red social para ganar 
un premio. La lista de participantes está numerada y debemos elegir aleatoriamente un número 
según la cantidad de participantes. Pide a la persona usuaria que proporcione el número de 
participantes del sorteo y devuelve el número sorteado.
'''
import random

cantidad_participantes = int(input("Ingrese la cantidad de participantes: "))
numero_sorteado = random.randint(1, cantidad_participantes)
print(f"El número sorteado es: {numero_sorteado}")

'''
¿Qué pasa si cambias el 1?

Si cambias el 1 por otro número, digamos 5, la función se convertiría en random.randint(5, cantidad_participantes).
Esto significa que el número aleatorio generado estará dentro del rango de 5 hasta cantidad_participantes, inclusive.
Por lo tanto, los números del 1 al 4 nunca serán generados.

Ingrese la cantidad de participantes: 45
El número sorteado es: 19
'''