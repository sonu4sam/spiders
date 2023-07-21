import pandas as pd

planets_df = pd.read_csv("http://localhost:8080/planets_pandas.csv", index_col = 'Name')

print(planets_df)

# save the dataframe to a csv file with a simple to_csv 

from get_planet_data import get_planet_data

planets = get_planet_data()
planets_df2 = pd.DataFrame(planets).set_index('Name')
planets_df2.to_csv("03/www/plantes_pandas.csv")

