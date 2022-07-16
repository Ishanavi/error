import pandas as pd
import csv

df = pd.read_csv('total_stars.csv')

print(df.shape)

del df["Luminosity"]
del df["Star_name"]
del df["Mass"]
del df["Distance"]
del df["Radius"]
print(df.shape)

df = df.rename({
                '':"rows",
                'Star_name': "star_name", 
                'Distance': "distance", 
                'Mass': "mass", 
                'Radius': "radius", 
            }, axis='columns')
print(list(df))

df.to_csv('main.csv') 