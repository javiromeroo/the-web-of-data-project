import pandas as pd

archivo = 'AB_NYC_2019.csv'
df = pd.read_csv(archivo)

subset = df[['neighbourhood_group', 'neighbourhood']]

result = subset.drop_duplicates()

result.to_csv('AB_neighbourhoods.csv', index=False)