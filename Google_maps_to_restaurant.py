import pandas as pd

df = pd.read_csv('google_maps_restaurants(cleaned).csv')

df['neighbourhood_group'] = df['Address'].str.split(',').str[1].str.strip()

df.rename(columns={'Price Category': 'Price_Category'}, inplace=True)

df.to_csv('Restaurant.csv', index=False)