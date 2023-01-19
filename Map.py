import folium
import pandas
import pandas as pd

#add basemap
map = folium.Map(location=[52,21], zoom_start=6, tiles="Stamen Terrain")

#open "Volcanoes" database and classify Volcanoes based on elevation
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation <1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return "red"

#add "Volcanoes" point layer with feature group method
fgv = folium.FeatureGroup(name="Volcanoes")

#add multicolor multiple cirlcle markers to "Volcanoes" layer
for lt, ln, el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=15, popup=str(el)+"m", fill_color=color_producer(el), color='black', fill_opacity=0.7))

#add "Population" poligon layer (json) with feature group method
fgp = folium.FeatureGroup(name="Population")

#classify json layer based on population
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x: {"fillColor": "yellow" if x["properties"]["POP2005"] <10000000
else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000
else 'red'}))


#add layers and control panel to map
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
map
