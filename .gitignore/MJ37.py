#Makeda Joseph
#04/03/2017


import folium
from folium.plugins import MarkerCluster
import pandas as pd

collisions = pd.read_csv("NYPD_Motor_Vehicle_Collisions-2.csv")

mapNYCOPENDATA = folium.Map(location=[40.8448, -73.8648])

coords = []
popups = []
icons = []

for index, row in collisions.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["LOCATION"]
                           
    coords.append([lat,lon])
    popups.append(name)
    icons.append(folium.Icon(icon='cloud'))

mapNYCOPENDATA.add_children(MarkerCluster(locations=coords, popups = popups, icons=icons))
                   
mapNYCOPENDATA.save(outfile='cunyLocations.html')
