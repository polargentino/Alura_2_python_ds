'''
Challenge Alura Store ayuda de DeepSeek-ri
'''
import pandas as pd

# Cargar los datos
url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda1 = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

# Agregar columna de tienda y asumir 1 venta por registro (ya que no hay columna de ventas)
for df, name in zip([tienda1, tienda2, tienda3, tienda4], ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4']):
    df['Tienda'] = name
    df['Ventas_estimadas'] = 1  # Asumimos 1 venta por registro

# Definir nombres de columnas según los datos
columna_precio = 'Precio'
columna_ventas = 'Ventas_estimadas'
columna_calificacion = 'Calificación'
columna_costo_envio = 'Costo de envío'
columna_categoria = 'Categoría del Producto'

## 1. Facturación total por tienda
def calcular_facturacion(df):
    return (df[columna_precio] * df[columna_ventas]).sum()

facturacion = {
    'Tienda 1': calcular_facturacion(tienda1),
    'Tienda 2': calcular_facturacion(tienda2),
    'Tienda 3': calcular_facturacion(tienda3),
    'Tienda 4': calcular_facturacion(tienda4)
}

## 2. Categorías más populares por tienda (basado en frecuencia de ventas)
def categorias_populares(df):
    return df[columna_categoria].value_counts().head(3)

categorias_tienda1 = categorias_populares(tienda1)
categorias_tienda2 = categorias_populares(tienda2)
categorias_tienda3 = categorias_populares(tienda3)
categorias_tienda4 = categorias_populares(tienda4)

## 3. Promedio de calificación por tienda
def promedio_calificacion(df):
    return df[columna_calificacion].mean()

calificacion = {
    'Tienda 1': promedio_calificacion(tienda1),
    'Tienda 2': promedio_calificacion(tienda2),
    'Tienda 3': promedio_calificacion(tienda3),
    'Tienda 4': promedio_calificacion(tienda4)
}

## 4. Productos más y menos vendidos (basado en frecuencia)
def productos_extremos(df):
    conteo_productos = df['Producto'].value_counts()
    return {
        'más_vendido': conteo_productos.idxmax(),
        'menos_vendido': conteo_productos.idxmin()
    }

productos_tienda1 = productos_extremos(tienda1)
productos_tienda2 = productos_extremos(tienda2)
productos_tienda3 = productos_extremos(tienda3)
productos_tienda4 = productos_extremos(tienda4)

## 5. Costo promedio de envío por tienda
def costo_promedio_envio(df):
    return df[columna_costo_envio].mean()

envio = {
    'Tienda 1': costo_promedio_envio(tienda1),
    'Tienda 2': costo_promedio_envio(tienda2),
    'Tienda 3': costo_promedio_envio(tienda3),
    'Tienda 4': costo_promedio_envio(tienda4)
}

# Determinar la tienda menos rentable (facturación más baja)
tienda_menos_rentable = min(facturacion, key=facturacion.get)

# Crear informe para el señor Juan
print("\n" + "="*50)
print("INFORME DE ANÁLISIS DE TIENDAS".center(50))
print("="*50 + "\n")

print("1. FACTURACIÓN TOTAL ESTIMADA POR TIENDA (asumiendo 1 venta por producto):")
for tienda, fact in facturacion.items():
    print(f"{tienda}: ${fact:,.2f}")
print(f"\n→ La tienda con MENOR facturación es: {tienda_menos_rentable}\n")

print("\n2. CATEGORÍAS MÁS POPULARES POR TIENDA (por frecuencia de productos vendidos):")
print("Tienda 1:", categorias_tienda1.to_dict())
print("Tienda 2:", categorias_tienda2.to_dict())
print("Tienda 3:", categorias_tienda3.to_dict())
print("Tienda 4:", categorias_tienda4.to_dict())

print("\n3. PROMEDIO DE CALIFICACIÓN DE CLIENTES:")
for tienda, calif in calificacion.items():
    print(f"{tienda}: {calif:.2f}/5")

print("\n4. PRODUCTOS MÁS Y MENOS VENDIDOS (por frecuencia):")
print("Tienda 1 - Más vendido:", productos_tienda1['más_vendido'], "| Menos vendido:", productos_tienda1['menos_vendido'])
print("Tienda 2 - Más vendido:", productos_tienda2['más_vendido'], "| Menos vendido:", productos_tienda2['menos_vendido'])
print("Tienda 3 - Más vendido:", productos_tienda3['más_vendido'], "| Menos vendido:", productos_tienda3['menos_vendido'])
print("Tienda 4 - Más vendido:", productos_tienda4['más_vendido'], "| Menos vendido:", productos_tienda4['menos_vendido'])

print("\n5. COSTO PROMEDIO DE ENVÍO:")
for tienda, costo in envio.items():
    print(f"{tienda}: ${costo:,.2f}")

print("\n" + "="*50)
print("RECOMENDACIÓN FINAL".center(50))
print("="*50)
print(f"\nBasado en el análisis de facturación estimada, categorías populares, calificaciones de clientes,")
print(f"productos más/menos vendidos y costos de envío, la tienda que menos lucro genera es:")
print(f"\n🔥 {tienda_menos_rentable} 🔥")
print("\nSe recomienda considerar la venta o reestructuración de esta tienda.")
print("="*50)
