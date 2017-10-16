#Makeda Joseph
#04/05/2017


import folium
from folium.plugins import MarkerCluster
import pandas as pd

museum = pd.read_csv('MUSEUM.csv')

mapMuseum = folium.Map(location=[40.7128, -74.0059])
popups =[]
locations = []

for index,row in museum.iterrows():
    #Extract the data:
    geom = row["the_geom"]
    trim = geom[7:-1]
    coord = trim.split(" ")
    Lat = float(coord[1])
    Lon = float(coord[0])
    name = row["NAME"]
    folium.Marker(location = [Lat, Lon], popup = name).add_to(mapMuseum)

    #Add the [lat,lon] to list of coordinates:
    ##coords.append([lat,lon])
    #Add the names to the popup list>
    ##popups.append(museum)
    
##mapMUSEUM.add_children(MarkerCluster(locations=coords, popups = popups, icons=icons))

mapMuseum.save(outfile='CityMuseumLocations.html')

##print(popups)
