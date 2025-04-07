'''
2 - Escribe una función que genere la tabla de multiplicar de un número entero del 1 al 10, según 
la elección del usuario. Como ejemplo, para el número 7, la tabla de multiplicar se debe mostrar 
en el siguiente formato:
'''
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(11):
        print(f"{numero} x {i} = {numero * i}")

# Uso de la función
tabla_multiplicar(7)

'''
Tabla de multiplicar del 7:
7 x 0 = 0
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
'''