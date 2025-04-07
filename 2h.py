'''
9 - Te han desafiado a crear un código que calcule los gastos de un viaje a una de las cuatro 
ciudades desde Recife, siendo ellas: Salvador, Fortaleza, Natal y Aracaju.

El costo diario del hotel es de 150 reales en todas ellas y el consumo de gasolina en el viaje en 
coche es de 14 km/l, siendo que el precio de la gasolina es de 5 reales por litro. Los gastos con 
paseos y alimentación a realizar en cada una de ellas por día serían [200, 400, 250, 300], 
respectivamente.

Sabiendo que las distancias entre Recife y cada una de las ciudades son aproximadamente 
[850, 800, 300, 550] km, crea tres funciones: la primera función calcula los gastos de hotel 
(gasto_hotel), la segunda calcula los gastos de gasolina (gasto_gasolina) y la tercera los gastos 
de paseo y alimentación (gasto_paseo).

Para probar, simula un viaje de 3 días a Salvador desde Recife. Considera el viaje de ida y vuelta 
en coche.

# Texto probablemente mostrado:
# Con base en los gastos definidos, un viaje de [dias] días a [ciudad] desde 
# Recife costaría [gastos] reales.
'''
# 9 - Una posible solución a este punto la encuentras a continuación:

dias = int(input("¿Cuántas diarias? "))
ciudad = input("¿Cuál es la ciudad? [Salvador, Fortaleza, Natal o Aracaju]: ")
distancias = [850, 800, 300, 550]
paseo = [200, 400, 250, 300]
km_l = 14
gasolina = 5

def gasto_hotel(dias):
    return 150 * dias

def gasto_gasolina(ciudad):
    if ciudad == "Salvador":
        return (2 * distancias[0] * gasolina) / km_l 
    elif ciudad == "Fortaleza":
        return (2 * distancias[1] * gasolina) / km_l 
    elif ciudad == "Natal":
        return (2 * distancias[2] * gasolina) / km_l 
    elif ciudad == "Aracaju":
        return (2 * distancias[3] * gasolina) / km_l 

def gasto_paseo(ciudad, dias):
    if ciudad=="Salvador":
        return paseo[0] * dias
    elif ciudad=="Fortaleza":
        return paseo[1] * dias
    elif ciudad=="Natal":
        return paseo[2] * dias 
    elif ciudad=="Aracaju":
        return paseo[3] * dias 

gastos = gasto_hotel(dias) + gasto_gasolina(ciudad) + gasto_paseo(ciudad, dias)
print(f"Con base en los gastos definidos, un viaje de {dias} días a {ciudad} desde Recife costaría {round(gastos, 2)} reales")

'''
¿Cuántas diarias? 23
¿Cuál es la ciudad? [Salvador, Fortaleza, Natal o Aracaju]: Salvador
Con base en los gastos definidos, un viaje de 23 días a Salvador desde Recife costaría 8657.14 reales


Gemini 2.0 Flash:
¡Entendido! Vamos a desglosar este código Python paso a paso para entender cómo calcula el costo 
total de un viaje:

1. Entrada de datos por el usuario:
----------------------------------
dias = int(input("¿Cuántas diarias? ")): Solicita al usuario que ingrese la cantidad de días de la 
estadía y la convierte a un número entero, almacenándolo en la variable dias.

ciudad = input("¿Cuál es la ciudad? [Salvador, Fortaleza, Natal o Aracaju]: "): Solicita al usuario 
que ingrese la ciudad de destino (Salvador, Fortaleza, Natal o Aracaju) y la almacena como una cadena 
en la variable ciudad.

2. Definición de listas de datos:
--------------------------------
distancias = [850, 800, 300, 550]: Define una lista llamada distancias que contiene las distancias 
(en km) desde Recife a cada una de las ciudades mencionadas, en el mismo orden: Salvador, Fortaleza, 
Natal y Aracaju.

paseo = [200, 400, 250, 300]: Define una lista llamada paseo que contiene el costo diario estimado 
de los paseos en cada una de las ciudades, en el mismo orden: Salvador, Fortaleza, Natal y Aracaju.

km_l = 14: Define una variable km_l que representa el rendimiento del vehículo en kilómetros por 
litro de gasolina (14 km/litro).

gasolina = 5: Define una variable gasolina que representa el precio por litro de gasolina 
(5 reales/litro).

3. Definición de la función gasto_hotel(dias):
---------------------------------------------
def gasto_hotel(dias):: Define una función llamada gasto_hotel que toma la cantidad de dias como 
argumento.

return 150 * dias: Calcula el gasto total de hotel multiplicando la tarifa diaria de 150 reales por 
la cantidad de días y devuelve el resultado.

4. Definición de la función gasto_gasolina(ciudad):
--------------------------------------------------
def gasto_gasolina(ciudad):: Define una función llamada gasto_gasolina que toma el nombre de la 
ciudad como argumento.

Utiliza una serie de condicionales if/elif para determinar la ciudad ingresada por el usuario.

Para cada ciudad:
----------------
Accede a la distancia correspondiente desde la lista distancias utilizando el índice correcto 
(0 para Salvador, 1 para Fortaleza, 2 para Natal, 3 para Aracaju).

Calcula el gasto de gasolina para el viaje de ida y vuelta: 
(2 * distancia * precio_gasolina) / rendimiento_km_litro.

Devuelve el gasto de gasolina calculado para esa ciudad.

5. Definición de la función gasto_paseo(ciudad, dias):
-----------------------------------------------------
def gasto_paseo(ciudad, dias):: Define una función llamada gasto_paseo que toma el nombre de la 
ciudad y la cantidad de dias como argumentos.

Utiliza una serie de condicionales if/elif para determinar la ciudad ingresada por el usuario.

Para cada ciudad:
----------------
Accede al costo diario de los paseos correspondiente desde la lista paseo utilizando el índice 
correcto.

Calcula el gasto total de los paseos multiplicando el costo diario por la cantidad de dias.
Devuelve el gasto total de los paseos para esa ciudad.

6. Cálculo del gasto total:
--------------------------
gastos = gasto_hotel(dias) + gasto_gasolina(ciudad) + gasto_paseo(ciudad, dias): Calcula el gasto 
total del viaje sumando los resultados de las tres funciones: gasto_hotel, gasto_gasolina y 
gasto_paseo.

7. Impresión del resultado:
---------------------------
print(f"Con base en los gastos definidos, un viaje de {dias} días a {ciudad} desde Recife costaría 
{round(gastos, 2)} reales"): Imprime un mensaje formateado que muestra la cantidad de días del viaje, 
la ciudad de destino y el costo total estimado (redondeado a 2 decimales usando round()).

En resumen:
----------
El código calcula el costo estimado de un viaje desde Recife a una de las cuatro ciudades brasileñas 
(Salvador, Fortaleza, Natal o Aracaju) basándose en la duración de la estadía, el costo del hotel por 
noche, el gasto de gasolina para el viaje de ida y vuelta (calculado según la distancia y el 
rendimiento del vehículo), y el costo diario de los paseos en la ciudad de destino. El usuario 
ingresa la cantidad de días y la ciudad, y el programa calcula y muestra el costo total estimado del 
viaje.
'''