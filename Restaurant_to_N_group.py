import pandas as pd

archivo = 'Restaurant.csv'
df = pd.read_csv(archivo)

# Extraer el valor de 'neighbourhood_group' desde la columna 'Address'
df['neighbourhood_group'] = df['Address'].str.split(',').str[-2].str.strip()

unique_neighbourhood_groups = df['neighbourhood_group'].drop_duplicates()

unique_neighbourhood_groups.to_csv('Restaurant_neighbourhood_groups.csv', index=False)