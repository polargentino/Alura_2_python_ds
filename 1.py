'''
1 - Escribe un código para instalar la versión 3.7.1 de la biblioteca matplotlib.

Creamos un enterono virtual en visual estudio code con la versión 3,10 de Python:

$ python3.10 -m venv ds_alura
$ source ds_alura/bin/activate
$ pip install --upgrade pip
$ pip install matplotlib==3.7.1
$ pip list

Package         Version
--------------- -----------
contourpy       1.3.1
cycler          0.12.1
fonttools       4.57.0
kiwisolver      1.4.8
matplotlib      3.7.1
numpy           2.2.4
packaging       24.2
pillow          11.1.0
pip             25.0.1
pyparsing       3.2.3
python-dateutil 2.9.0.post0
setuptools      65.5.0
six             1.17.0
'''
# Ejemplo 1: Vamos a probar la biblioteca Matplotlib para un ejemplo sobre el cálculo de los promedios de notas de los estudiantes de una clase.
# (https://matplotlib.org/stable/tutorials/introductory/pyplot.html)

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt


estudiantes = ['Juan','María','José']
notas = [9,8.5,6.5]


plt.bar(x= estudiantes, height=notas)
plt.savefig('grafico_notas.png')  # Guarda la gráfica como un archivo PNG
# plt.show()  # No es necesario con el backend Agg

'''
¡Excelente! Me da muchísimo gusto saber que la opción de usar el backend Agg y guardar la figura 
como grafico_notas.png funcionó perfectamente.

¿Qué significa esto?

Como mencionamos antes, el backend Agg es una implementación no interactiva que renderiza las 
figuras como archivos de imagen. Esto es muy útil en entornos donde no hay una interfaz gráfica 
disponible o cuando el objetivo es simplemente guardar la visualización para su posterior revisión 
o inclusión en un informe.
¿Dónde puedes encontrar la gráfica?

El archivo grafico_notas.png se habrá creado en el mismo directorio desde donde ejecutaste tu 
script 1.py (es decir, en /home/pol/Escritorio/Alura_2_python_ds/). Puedes abrir este archivo con 
cualquier visor de imágenes en tu sistema para ver el gráfico de barras con los nombres de los 
estudiantes y sus respectivas notas.

Próximos pasos:

Ahora que tienes una forma funcional de generar gráficos, puedes seguir explorando las capacidades 
de Matplotlib:

Personalización: Puedes modificar muchos aspectos del gráfico, como los colores de las barras, 
las etiquetas de los ejes, el título, la rotación de las etiquetas, etc.

Diferentes tipos de gráficos: Matplotlib te permite crear una gran variedad de visualizaciones, 
como gráficos de líneas (plt.plot()), gráficos de dispersión (plt.scatter()), 
histogramas (plt.hist()), gráficos de pastel (plt.pie()), y muchos más.

Subplots: Puedes crear múltiples gráficos dentro de una misma figura utilizando plt.subplot().
Si en algún momento necesitas una visualización interactiva dentro de una ventana, podríamos 
intentar nuevamente configurar los backends interactivos como TkAgg o Qt5Agg, pero al menos ahora 
tienes una solución sólida para generar las gráficas.

¡Felicidades por haberlo hecho funcionar! ¿Hay algo más en lo que te pueda ayudar con Matplotlib o 
con tus estudios de Data Science?
'''