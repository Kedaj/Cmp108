#Makeda Joseph
#03/29/2017


import folium

#Create a map, centered (0,0) and zoomed out a bit:
mapWorld = folium.Map(location=[0, 0],zoom_start=3)
import folium

mapCUNY = folium.Map(location=[40.75, -74.125],zoom_start=10)

folium.Marker(location = [14.0101, -60.9875], popup = "Castries,St Lucia").add_to(mapWorld)
folium.Marker(location = [18.1096, -77.2975], popup = "Kingston, Jamaica").add_to(mapWorld)
folium.Marker(location = [40.7128, -74.0059], popup = "New York City").add_to(mapWorld)
folium.Marker(location = [34.0522, -118.2437], popup = "Los Angles").add_to(mapWorld)
folium.Marker(location = [41.8719, 12.5674], popup = "Italy").add_to(mapWorld)
#Save the map:
mapWorld.save(outfile='tempMap.html')
