import pandas as pd
import re

# Leer el archivo CSV
df = pd.read_csv("google_maps_restaurants(cleaned).csv")

# Función para extraer el neighbourhood
def extract_neighbourhood(address):
    # Usar regex para capturar la penúltima sección antes de la última coma
    match = re.search(r',\s*([^,]+)\s*,\s*\w{2}\s*\d{5}', address)
    if match:
        return match.group(1).strip()
    return None

# Crear una nueva columna 'neighbourhood' basada en la columna 'Address'
df['neighbourhood_group'] = df['Address'].apply(extract_neighbourhood)

df.rename(columns={'Price Category': 'Price_Category'}, inplace=True)

# Guardar el CSV con la nueva columna
df.to_csv("Restaurant.csv", index=False)