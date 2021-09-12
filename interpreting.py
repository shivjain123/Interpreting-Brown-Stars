import pandas as pd
import plotly_express as px
from matplotlib import pyplot as plt

df = pd.read_csv('CSV Files/filtered.csv')

df.drop(["Unnamed: 0"], axis=1, inplace=True)

name_list = df["Name"].tolist()
distance_list = df["Distance"].tolist()
mass_list = df["Mass"].tolist()
radius_list = df["Radius"].tolist()
gravity_list = df["Gravity"].tolist()

name_vs_mass = plt.figure(figsize=(10, 5))
name_vs_mass = plt.bar(name_list, mass_list)

plt.xlabel("Planet Names")
plt.ylabel("Planet Masses")
plt.title("Name Vs Mass")
plt.show()

name_vs_distance = plt.figure(figsize=(10, 5))
name_vs_distance = plt.bar(name_list, distance_list)

plt.xlabel("Planet Names")
plt.ylabel("Planet Distances")
plt.title("Name Vs Distance")
plt.show()

name_vs_radius = plt.figure(figsize=(10, 5))
name_vs_radius = plt.bar(name_list, radius_list)

plt.xlabel("Planet Names")
plt.ylabel("Planet Radiuses")
plt.title("Name Vs Radius")
plt.show()

name_vs_gravity = plt.figure(figsize=(10, 5))
name_vs_gravity = plt.bar(name_list, gravity_list)

plt.xlabel("Planet Names")
plt.ylabel("Planet Gravities")
plt.title("Name Vs Gravity")
plt.show()

""" name_vs_mass = px.bar(x = name_list, y = mass_list)
name_vs_mass.show()

name_vs_distance = px.bar(x = name_list, y = distance_list)
name_vs_distance.show()

name_vs_radius = px.bar(x = name_list, y = radius_list)
name_vs_radius.show()

name_vs_gravity = px.bar(x=name_list, y=gravity_list)
name_vs_gravity.show() """
