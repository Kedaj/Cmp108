#Makeda Joseph
#04/03/2017


import folium
from folium.plugins import MarkerCluster
import pandas as pd

collisions = pd.read_csv("NYPD_Motor_Vehicle_Collisions-3.csv")

mapNYCOPENDATA = folium.Map(location=[40.8140, -73.9375])

coords = []
popups = []
icons = []

for index, row in collisions.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["LOCATION"]
                           
    coords.append([lat,lon])
    popups.append(name)

    if "TAXI" == row["VEHICLE TYPE CODE 2"] :
        icons.append(folium.Icon(color='yellow'))
    else:
        icons.append(folium.Icon(color='green'))

print (coords)
        
mapNYCOPENDATA.add_child(MarkerCluster(locations=coords, popups = popups, icons=icons))
                   
mapNYCOPENDATA.save(outfile='cunyLocations1.html')
