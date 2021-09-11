import pandas as pd
import plotly_express as px

df = pd.read_csv('CSV Files/filtered.csv')

df.drop(["Unnamed: 0"], axis=1, inplace=True)

name_list = df["Name"].tolist()
distance_list = df["Distance"].tolist()
mass_list = df["Mass"].tolist()
radius_list = df["Radius"].tolist()
gravity_list = df["Gravity"].tolist()

name_vs_mass = px.bar(x = name_list, y = mass_list)
#name_vs_mass.show()

name_vs_distance = px.bar(x = name_list, y = distance_list)
#name_vs_distance.show()

name_vs_radius = px.bar(x = name_list, y = radius_list)
#name_vs_radius.show()

name_vs_gravity = px.bar(x=name_list, y=gravity_list)
#name_vs_gravity.show()