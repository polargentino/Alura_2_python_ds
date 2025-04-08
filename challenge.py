# 📦 Cargar librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🎯 Cargar datos desde las URLs
url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

# 📊 Leer cada tienda
tienda = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

# 🔀 Unir todos los datos en un solo DataFrame
df = pd.concat([tienda, tienda2, tienda3, tienda4], ignore_index=True)

# 🧹 Limpiar nombres de columnas (por si tienen espacios)
df.columns = df.columns.str.strip()

# ✅ 1. Análisis de facturación
facturacion_total = df['Precio'].sum()
print(f"💰 Facturación total: ${facturacion_total:,.2f}")

# ✅ 2. Ventas por categoría
ventas_categoria = df['Categoría del Producto'].value_counts()
print("\n📦 Ventas por categoría:")
print(ventas_categoria)

# Visualización y guardado
plt.figure(figsize=(10, 6))
ventas_categoria.plot(kind='bar', title='Ventas por Categoría', color='skyblue')
plt.xlabel("Categoría")
plt.ylabel("Cantidad de Ventas")
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('ventas_por_categoria.png')
print("Gráfico 'ventas_por_categoria.png' guardado.")
plt.close()

# ✅ 3. Calificación promedio de la tienda
calificacion_promedio = df['Calificación'].mean()
print(f"\n⭐ Calificación promedio: {calificacion_promedio:.2f} estrellas")

# ✅ 4. Productos más y menos vendidos
productos_vendidos = df['Producto'].value_counts()
mas_vendido = productos_vendidos.idxmax()
menos_vendido = productos_vendidos.idxmin()

print(f"\n📈 Producto más vendido: {mas_vendido}")
print(f"📉 Producto menos vendido: {menos_vendido}")

# ✅ 5. Envío promedio por tienda
envio_promedio = df.groupby('Lugar de Compra')['Costo de envío'].mean()
print("\n🚚 Envío promedio por tienda:")
print(envio_promedio.round(2))

# Visualización y guardado
plt.figure(figsize=(12, 7))
envio_promedio.sort_values().plot(kind='barh', title='Costo de Envío Promedio por Tienda', color='orange')
plt.xlabel("Costo Promedio de Envío")
plt.ylabel("Ciudad")
plt.grid(axis='x')
plt.tight_layout()
plt.savefig('envio_promedio_por_tienda.png')
print("Gráfico 'envio_promedio_por_tienda.png' guardado.")
plt.close()

print("\n¡Todos los gráficos han sido guardados como archivos .png!")

'''
💰 Facturación total: $4,403,619,200.00

📦 Ventas por categoría:
Categoría del Producto
Muebles                    1886
Electrónicos               1772
Juguetes                   1290
Electrodomésticos          1149
Deportes y diversión       1113
Instrumentos musicales      753
Libros                      742
Artículos para el hogar     730
Name: count, dtype: int64
Gráfico 'ventas_por_categoria.png' guardado.

⭐ Calificación promedio: 4.01 estrellas

📈 Producto más vendido: Mesa de noche
📉 Producto menos vendido: Celular ABXY

🚚 Envío promedio por tienda:
Lugar de Compra
Armenia          22867.86
Barranquilla     22692.26
Bogotá           24532.08
Bucaramanga      26790.06
Cali             26726.81
Cartagena        22638.43
Cúcuta           28597.31
Inírida          30557.14
Leticia          25317.61
Manizales        24948.78
Medellín         25282.02
Neiva            27710.00
Pasto            27801.06
Pereira          23211.41
Riohacha         24127.61
Santa Marta      18752.32
Soacha           34768.42
Valledupar       22021.43
Villavicencio    25100.00
Name: Costo de envío, dtype: float64
Gráfico 'envio_promedio_por_tienda.png' guardado.

¡Todos los gráficos han sido guardados como archivos .png!
                                                                              
'''