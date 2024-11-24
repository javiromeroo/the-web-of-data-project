import pandas as pd

df1 = pd.read_csv('AB_neighbourhoods.csv')  # Contiene 'neighbourhood_group' y 'neighbourhood'
df2 = pd.read_csv('Restaurant_neighbourhood_groups.csv')  # Contiene solo 'neighbourhood_group'

df2['neighbourhood'] = None  # Agrega la columna 'neighbourhood' con valores nulos

df_combinado = pd.concat([df1, df2], ignore_index=True)

df_combinado.to_csv('Neighbourhood.csv', index=False)