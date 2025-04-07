'''
8 - Como científico de datos en un equipo de fútbol, necesitas implementar nuevas formas de 
recopilación de datos sobre el rendimiento de los jugadores y del equipo en su conjunto. Tu primera 
acción es crear una forma de calcular la puntuación del equipo en el campeonato nacional a partir 
de los datos de goles marcados y recibidos en cada juego.

Escribe una función llamada calcula_puntos() que recibe como parámetros dos listas de números 
enteros, representando los goles marcados y recibidos por el equipo en cada partido del campeonato. 
La función debe devolver la puntuación del equipo y el rendimiento en porcentaje, teniendo en cuenta 
que la victoria vale 3 puntos, el empate 1 punto y la derrota 0 puntos.

Nota: si la cantidad de goles marcados en un partido es mayor que los recibidos, el equipo ganó. 
En caso de ser igual, el equipo empató, y si es menor, el equipo perdió. Para calcular el 
rendimiento, debemos hacer la razón entre la puntuación del equipo y la puntuación máxima que 
podría recibir.

Para la prueba, utiliza las siguientes listas de goles marcados y recibidos:

goles_marcados = [2, 1, 3, 1, 0]
goles_recibidos = [1, 2, 2, 1, 3]
# Texto probablemente mostrado:
# La puntuación del equipo fue `puntos` y su rendimiento fue `desempeno`%"


8 - Una posible solución a este punto la encuentras a continuación:
'''

goles_marcados = [2, 1, 3, 1, 0]
goles_sofridos = [1, 2, 2, 1, 3]

def calcula_puntos(goles_marcados, goles_sofridos):
  puntos = 0
  for i in range(len(goles_marcados)):
    if goles_marcados[i] > goles_sofridos[i]:
      puntos += 3
    elif goles_marcados[i] == goles_sofridos[i]:
      puntos += 1
  aprob = 100 * puntos / (len(goles_marcados) * 3)
  return (puntos, aprob)

puntos, aprob = calcula_puntos(goles_marcados, goles_sofridos)
print(f"La puntuación del equipo fue de {puntos} y su rendimiento fue de {round(aprob)}%")

'''
La puntuación del equipo fue de 7 y su rendimiento fue de 47%


¡Entendido! Vamos a desglosar este código Python paso a paso para entender cómo calcula los puntos 
de un equipo y su rendimiento:

1. Definición de las listas de goles:
------------------------------------
goles_marcados = [2, 1, 3, 1, 0]: Se crea una lista llamada goles_marcados que representa la 
cantidad de goles que el equipo anotó en cada uno de los 5 partidos.

goles_sofridos = [1, 2, 2, 1, 3]: Se crea una lista llamada goles_sofridos que representa la 
cantidad de goles que el equipo recibió en cada uno de los 5 partidos.

2. Definición de la función calcula_puntos(goles_marcados, goles_sofridos):
--------------------------------------------------------------------------
def calcula_puntos(goles_marcados, goles_sofridos):: Se define una función llamada calcula_puntos 
que toma dos listas como argumentos: goles_marcados y goles_sofridos.

puntos = 0: Se inicializa una variable llamada puntos en 0. Esta variable se utilizará para acumular 
los puntos del equipo.

for i in range(len(goles_marcados)):: Se inicia un bucle for que itera a través de los índices de la 
lista goles_marcados. len(goles_marcados) devuelve la cantidad de partidos (en este caso, 5), por 
lo que i tomará los valores 0, 1, 2, 3 y 4.

if goles_marcados[i] > goles_sofridos[i]:: Dentro del bucle, se verifica si la cantidad de goles 
marcados en el partido actual (indicado por el índice i) es mayor que la cantidad de goles sufridos en ese mismo partido.
puntos += 3: Si la condición es verdadera (el equipo ganó el partido), se suman 3 puntos a la 
variable puntos.

elif goles_marcados[i] == goles_sofridos[i]:: Si la condición anterior es falsa, se verifica si 
la cantidad de goles marcados es igual a la cantidad de goles sufridos en el partido actual.
puntos += 1: Si esta condición es verdadera (el equipo empató el partido), se suma 1 punto a la 
variable puntos.

aprob = 100 * puntos / (len(goles_marcados) * 3): Después de recorrer todos los partidos, se calcula 
el rendimiento del equipo en porcentaje.

puntos: Es la cantidad total de puntos obtenidos por el equipo.

len(goles_marcados) * 3: Calcula la cantidad máxima posible de puntos que el equipo podría haber 
obtenido (3 puntos por cada partido).

100 * ...: Multiplica el resultado de la división por 100 para obtener el porcentaje.
El resultado se almacena en la variable aprob.

return (puntos, aprob): La función devuelve una tupla que contiene la cantidad total de puntos y 
el aprob (rendimiento en porcentaje).

3. Llamada a la función y obtención de resultados:
-------------------------------------------------
puntos, aprob = calcula_puntos(goles_marcados, goles_sofridos): Se llama a la función calcula_puntos 
con las listas goles_marcados y goles_sofridos como argumentos. Los dos valores devueltos por la 
función (la cantidad de puntos y el rendimiento) se asignan a las variables puntos y aprob 
respectivamente.

4. Impresión de los resultados:
------------------------------
print(f"La puntuación del equipo fue de {puntos} y su rendimiento fue de {round(aprob)}%"): Se 
imprime un mensaje en la consola mostrando la puntuación total del equipo y su rendimiento en 
porcentaje (redondeado al número entero más cercano usando round()).

En resumen:
----------
El código toma la información de los goles marcados y sufridos por un equipo en varios partidos. 
Luego, calcula la puntuación total del equipo según las reglas de fútbol (3 puntos por victoria, 
1 punto por empate) y calcula el rendimiento del equipo como un porcentaje del máximo de puntos 
posibles. Finalmente, muestra estos resultados en un mensaje.

Considerando los datos de ejemplo:
----------------------------------
Partido 1: Marcó 2, sufrió 1 (Victoria) -> +3 puntos
Partido 2: Marcó 1, sufrió 2 (Derrota) -> +0 puntos
Partido 3: Marcó 3, sufrió 2 (Victoria) -> +3 puntos
Partido 4: Marcó 1, sufrió 1 (Empate) -> +1 punto
Partido 5: Marcó 0, sufrió 3 (Derrota) -> +0 puntos
Puntos totales: 3 + 0 + 3 + 1 + 0 = 7

Rendimiento: (7 / (5 * 3)) * 100 = (7 / 15) * 100 ≈ 46.67%

Por lo tanto, la salida del código sería:
-----------------------------------------

La puntuación del equipo fue de 7 y su rendimiento fue de 47%
'''