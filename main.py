import folium
import pandas as pd

m = folium.Map(location=[50.04908088464327, 21.981612615229974], title='Stamen Terrain', zoom_start=6, width=950, height=650)

# to mozna for z jakiegos arraya zamiast pojedynczo
m.add_child(folium.Marker(location=[50.04908088464327, 21.981612615229974], popup="nasz marker: Rzeszów", icon=folium.Icon("red")))
m.add_child(folium.Marker(location=[49.949890921270715, 22.058874020398942], popup="nasz marker: Kielnarowa ", icon=folium.Icon("green")))
m.add_child(folium.Marker(location=[50.08951265233697, 21.520494332301062], popup="nasz marker: Paszczyna", icon=folium.Icon("blue")))

# simple way
# with open("Volcanoes.txt", mode='r') as v:
#         for volcano in v.readlines()[1:]:
#             params = volcano.strip().split(',')
#             folium.map.Marker([float(params[-2]), float(params[-1])], popup=params[3], icon=folium.Icon("orange")).add_to(m)
# m.save('map.html')
#

# pandas
data = pd.read_csv('Volcanoes.txt')
# data series, i loc, 2 wiersze data frame
print(data['LAT'])
print(data['NAME'].iloc[3])

lat = list(data['LAT'])
lon = list(data['LON'])
names = list(data['NAME'])
elev = list(data['ELEV'])

fg1 = folium.FeatureGroup('w 1 - wulkany')
fg2 = folium.FeatureGroup('w 2 - panstwa')

def set_color(elev):
    if elev < 1000:
        return 'green'
    elif elev < 2000:
        return 'orange'
    else:
        return 'red'

def set_color_json(pop):
    if pop < 1000000:
        return 'green'
    elif pop < 2000000:
        return 'orange'
    else:
        return 'red'

for lat, lon, name, elev in zip(lat, lon, names, elev):

    folium.CircleMarker(
        [float(lat), float(lon)],
        popup=elev,
        radius=5,
        color=set_color(elev),
        fill_opacity=0.75,
        fill_color=set_color(elev)).add_to(fg1)
fg2.add_child(folium.GeoJson(data=open('world.json').read(), style_function=lambda x:{'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if x['properties']['POP2005'] < 20000000 else 'red'}))

m.add_child(fg1)
m.add_child(fg2)

m.add_child(folium.LayerControl())
m.save('map.html')



